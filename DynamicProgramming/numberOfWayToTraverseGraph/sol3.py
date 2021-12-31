def numberOfWaysToTraverseGraph(width, height):

    graph = [[0 for _ in range(width)] for _ in range(height)]
    for widthIdx in range(width):
        for heightIdx in range(height):
            if widthIdx == 0 or heightIdx == 0:
                graph[heightIdx][widthIdx] = 1
            else:
                graph[heightIdx][widthIdx] = graph[heightIdx][widthIdx -
                                                              1] + graph[heightIdx-1][widthIdx]
    print(graph)
    print(graph[height-1][width-1])
    return graph[height-1][width-1]


numberOfWaysToTraverseGraph(4, 3)
