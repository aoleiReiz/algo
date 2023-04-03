def kruskalsAlgorithm(edges):
    # Write your code here.
    edgeList = []
    for source_index, vertex in enumerate(edges):
        for edge in vertex:
            if edge[0] > source_index:
                edgeList.append([source_index, edge[0], edge[1]])
    sorted_edges = sorted(edgeList, key=lambda edge: edge[2])

    parents = [vertex for vertex in range(len(edges))]
    ranks = [0 for _ in range(len(edges))]
    mst = [[] for _ in range(len(edges))]
    for edge in sorted_edges:
        vertex1_root = find(edge[0], parents)
        vertex2_root = find(edge[1], parents)
        if vertex1_root != vertex2_root:
            mst[edge[0]].append([edge[1], edge[2]])
            mst[edge[1]].append([edge[0], edge[2]])
            union(vertex1_root, vertex2_root, parents, ranks)
    return mst


def find(vertex, parents):
    if vertex != parents[vertex]:
        parents[vertex] = find(parents[vertex], parents)
    return parents[vertex]


def union(vertex1_root, vertex2_root, parents, ranks):
    if ranks[vertex1_root] < ranks[vertex2_root]:
        parents[vertex1_root] = vertex2_root
    elif ranks[vertex1_root] > ranks[vertex2_root]:
        parents[vertex2_root] = vertex1_root
    else:
        parents[vertex1_root] = vertex2_root
        ranks[vertex2_root] += 1
