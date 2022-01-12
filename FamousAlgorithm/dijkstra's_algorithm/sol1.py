# O(v^2 + e) time v: vertices number, e: edges number
# O(v) space
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistance = [float("inf") for _ in range(numberOfVertices)]
    minDistance[start] = 0

    visited = set()

    while len(visited) != numberOfVertices:
        # find the min distance of all vertex that not in set()
        vertex, currentMinDistance = getVertexMinDistance(minDistance, visited)
        # if there is no vertex that belongs to other vertex then break
        if currentMinDistance == float("inf"):
            break
        # add to visited
        visited.add(vertex)
        # calculate all of the edges belong to the min distance vertex and update it
        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDistinationDistance = minDistance[destination]
            if newPathDistance < currentDistinationDistance:
                minDistance[destination] = newPathDistance

    return list(map(lambda x: -1 if x == float("inf") else x, minDistance))


def getVertexMinDistance(distances, visited):
    currentMinDistance = float("inf")
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance

    return vertex, currentMinDistance


start = 0
array = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]

print(dijkstrasAlgorithm(start, array))
