# O(n) time | O(1) space
def threeNumberSort(array, order):
    three_count = [0, 0, 0]
    for value in array:
        # order index
        order_idx = order.index(value)
        three_count[order_idx] += 1
        # use if statement
        # if value == order[0]:
        #     three_count[0] += 1
        # elif value == order[1]:
        #     three_count[1] += 1
        # else:
        #     three_count[2] += 1

    # 用count出來的array去更新舊的array
    for i in range(len(three_count)):
        start_idx = sum(three_count[:i])
        for j in range(three_count[i]):
            array[start_idx + j] = order[i]

    return array


input = {"array": [1, 0, 0, -1, -1, 0, 1, 1], "order": [0, 1, -1]}
print(threeNumberSort(input["array"], input["order"]))
