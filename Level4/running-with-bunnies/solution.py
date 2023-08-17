def print_m(m, fill=0):
    for x in m:
        for y in x:
            print str(y).rjust(fill, ' ') + "\t",
        print


class Graph:
    # based on https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src, iterations=None):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        path_to = []
        for i in range(self.V):
            path_to.append([])
            path_to[i].append(i)
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    path_to[v] = path_to[u] + [v]

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return

        return path_to, dist


def solution(times, times_limit):
    graph = Graph(len(times))
    bun_num = graph.V - 2
    for u, weights in enumerate(times):
        for v, w in enumerate(weights):
            graph.addEdge(u, v, w)

    paths = []
    min_distances = []
    for vertex in range(graph.V):
        res = graph.BellmanFord(vertex)
        if not res:
            print("Graph contains negative weight cycle")
            return list(range(0, bun_num))
        paths.append(res[0])
        min_distances.append(res[1])

    # print_m(paths, fill=10)
    # print
    # print_m(min_distances, fill=10)
    # print

    def valid_path_with_min_bun(bun, start, total_path, total_sum):
        if bun == 0:
            return total_path[:-1] + paths[start][-1], total_sum + min_distances[start][-1]
        else:
            for nextId, distance in enumerate(min_distances[start]):
                if nextId in total_path:
                    continue
                next_path, next_dist = valid_path_with_min_bun(
                    bun - 1,
                    nextId,
                    total_path[:-1] + paths[start][nextId],
                    total_sum+distance
                )
                if times_limit >= next_dist and len(set(next_path)) >= bun + 2:
                    return next_path, next_dist

            return [], float('Inf')

    best_path = []
    for buns_to_save in range(bun_num, 0, -1):
        best_path, dist = valid_path_with_min_bun(buns_to_save, 0, [0], 0)
        if best_path:
            break

    print('best', best_path)
    return [x-1 for x in sorted(set(best_path))][1:-1]


if __name__ == "__main__":
    tests = (
        (
            (
                [[0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0]],
                3
            ),
            [0, 1]
        ),
        (
            (
                [[0, 2, 2, 2, -1],
                 [9, 0, 2, 2, -1],
                 [9, 3, 0, 2, -1],
                 [9, 3, 2, 0, -1],
                 [9, 3, 2, 2, 0]],
                1
            ),
            [1, 2]
        ),
        (
            (
                [[0, 1, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0]],
                4
            ),
            [0, 1, 2],
        ),
        (
            (
                [[0, 1, 1, 1, -3],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0]],
                -100
            ),
            [0, 1, 2],
        ),
        (
            (
                [[0, 1, 2, 1, 1],
                 [-1, 0, 10, 10, 10],
                 [-1, -1, 0, 10, 10],
                 [-1, 10, 1, 0, 1],
                 [-1, 10, 10, 10, 0]],
                20
            ),
            [0, 1, 2],
        )
    )

    for args, target in tests:
        sol = solution(*args)
        print(args)
        print("\t" + str(target))
        print("\t" + str(sol))
        print("\t" + str(sol == target))
