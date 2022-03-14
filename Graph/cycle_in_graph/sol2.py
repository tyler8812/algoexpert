WHITE, GRAY, BLACK = 0, 1, 2

# time O(v+e) | space O(v)
def cycleInGraph(edges):
    number_of_nodes = len(edges)
    colors = [WHITE for _ in range(number_of_nodes)]

    for node in range(number_of_nodes):
        if colors[node] != WHITE:
            continue
        contiain_cycle = travel_and_color_node(node, edges, colors)
        if contiain_cycle:
            return True

    return False


def travel_and_color_node(node, edges, colors):
    colors[node] = GRAY

    neighbors = edges[node]
    for neighbor in neighbors:
        if colors[neighbor] == GRAY:
            return True
        if colors[neighbor] == BLACK:
            continue
        contiain_cycle = travel_and_color_node(neighbor, edges, colors)
        if contiain_cycle:
            return True

    colors[node] = BLACK
    return False
