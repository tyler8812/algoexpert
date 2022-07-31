# complexity same as sol2.py but more advanced
def apartmentHunting(blocks, reqs):
    min_distances_from_blocks = list(
        map(lambda req: get_min_distances(blocks, req), reqs)
    )
    max_distances_at_blocks = get_max_distances_at_blocks(
        blocks, min_distances_from_blocks
    )
    return get_idx_at_min_value(max_distances_at_blocks)


def get_min_distances(blocks, req):
    min_distances = [0 for _ in blocks]
    closest_idx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closest_idx = i
        min_distances[i] = distance_between(i, closest_idx)
    for j in reversed(range(len(blocks))):
        if blocks[j][req]:
            closest_idx = j
        min_distances[j] = min(distance_between(closest_idx, j), min_distances[j])
    return min_distances


def get_max_distances_at_blocks(blocks, min_distances_from_blocks):

    max_distances = [0 for _ in blocks]
    for i in range(len(blocks)):
        min_distance_at_blocks = list(
            map(lambda distances: distances[i], min_distances_from_blocks)
        )
        max_distances[i] = max(min_distance_at_blocks)
    return max_distances


def get_idx_at_min_value(array):
    idx_at_min_value = 0
    min_value = float("inf")
    for i in range(len(array)):
        current_value = array[i]
        if current_value < min_value:
            min_value = current_value
            idx_at_min_value = i
    return idx_at_min_value


def distance_between(a, b):
    return abs(a - b)
