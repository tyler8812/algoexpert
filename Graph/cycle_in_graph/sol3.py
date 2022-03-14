def cycleInGraph(edges):
    number_of_node = len(edges)
    visited = [0 for _ in range(number_of_node)]
    current_visited = [0 for _ in range(number_of_node)]
    for node in range(number_of_node):
        if visited[node] == 1:
            continue
        contain_cycle = is_contain_cycle(node, edges, visited, current_visited)
        if contain_cycle:
            return True
    return False


def is_contain_cycle(node, edges, visited, current_visited):
    visited[node] = 1
    current_visited[node] = 1
    for neighbor in edges[node]:
        if current_visited[neighbor] == 1:
            return True
        # can also add if visited for reducing computation
        if not visited[neighbor]:
            contain_cycle = is_contain_cycle(neighbor, edges, visited, current_visited)
            if contain_cycle:
                return True
    current_visited[node] = 0
    return False
