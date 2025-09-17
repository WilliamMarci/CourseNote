import heapq


def dijkstra_sssp_tree(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    prev = [-1] * n  # 记录前驱节点，用于构建树
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            new_d = d + w
            if new_d < dist[v]:
                dist[v] = new_d
                prev[v] = u  # 记录最短路径上的前驱
                heapq.heappush(heap, (new_d, v))

    # 通过prev数组构建SSSP树（邻接表形式）
    tree = [[] for _ in range(n)]
    for v in range(n):
        if prev[v] != -1:
            u = prev[v]
            tree[u].append((v, dist[v] - dist[u]))  # 存储子节点及边权
    return tree, dist


# 示例图：graph[u] = [(v, weight), ...]
graph = [
    [(1, 2), (2, 1)],  # A->B:2, A->C:1
    [(3, 3)],  # B->D:3
    [(3, 1)],  # C->D:1
    [],  # D
]
tree, dists = dijkstra_sssp_tree(graph, 0)
print("SSSP树结构:", tree)
print("最短距离:", dists)
