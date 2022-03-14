# time O(v+e) | space O(v)
def cycleInGraph(edges):
    number_of_nodes = len(edges)
    visited = [False for _ in range(number_of_nodes)]
    current_in_stack = [False for _ in range(number_of_nodes)]

    for node in range(number_of_nodes):
        if visited[node]:
            continue
        contiain_cycle = is_node_in_cycle(node, edges, visited, current_in_stack)
        if contiain_cycle:
            return True

    return False


def is_node_in_cycle(node, edges, visited, current_in_stack):
    visited[node] = True
    current_in_stack[node] = True

    for neighbor in edges[node]:
        if not visited[neighbor]:
            contiain_cycle = is_node_in_cycle(
                neighbor, edges, visited, current_in_stack
            )
            if contiain_cycle:
                return True
        elif current_in_stack[neighbor]:
            return True

    current_in_stack[node] = False
    return False
