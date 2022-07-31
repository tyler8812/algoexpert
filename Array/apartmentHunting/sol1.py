# O(b^2*r) time | O(b) space
# b: length of blocks
# r: length of reqs
def apartmentHunting(blocks, reqs):
    nearest_pos = [0] * len(blocks)
    for i in range(len(blocks)):
        for req in reqs:
            current_req_shortest = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    current_req_shortest = min(current_req_shortest, abs(i - j))
            nearest_pos[i] = max(current_req_shortest, nearest_pos[i])

    min_blocks = float("inf")
    min_idx = 0
    for i in range(len(nearest_pos)):
        if nearest_pos[i] < min_blocks:
            min_blocks = nearest_pos[i]
            min_idx = i

    return min_idx


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

print(apartmentHunting(blocks, reqs))
