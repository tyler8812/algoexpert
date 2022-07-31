# O(b*r) time | O(b*r) space
# b: length of blocks
# r: length of reqs
def apartmentHunting(blocks, reqs):
    nearest_pos = [0] * len(blocks)

    for req in reqs:
        current_req_shortest = find_req_shortest(blocks, req)
        for i in range(len(blocks)):
            nearest_pos[i] = max(current_req_shortest[i], nearest_pos[i])

    min_blocks = float("inf")
    min_idx = 0
    for i in range(len(nearest_pos)):
        if nearest_pos[i] < min_blocks:
            min_blocks = nearest_pos[i]
            min_idx = i

    return min_idx


def find_req_shortest(blocks, req):
    from_left = [0] * len(blocks)
    closest_idx = float("inf")
    # from left
    for i in range(len(blocks)):
        if blocks[i][req]:
            closest_idx = i
        from_left[i] = abs(i - closest_idx)

    from_right = [0] * len(blocks)
    closest_idx = float("inf")
    # from right
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest_idx = i
        from_right[i] = abs(i - closest_idx)

    min_distance = [0] * len(blocks)
    for i in range(len(from_right)):
        min_distance[i] = min(from_left[i], from_right[i])

    return min_distance


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))
