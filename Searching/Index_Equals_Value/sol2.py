# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    left_idx = 0
    right_idx = len(array) - 1
    target = (left_idx + right_idx) // 2
    while left_idx <= right_idx:
        # 目前idx太小了所以往右找
        if target < array[target]:
            right_idx = target - 1
        # 目前idx太大了所以往左找
        elif target > array[target]:
            left_idx = target + 1
        # 找到了判斷是不是為0
        elif target == array[target] and target == 0:
            return target
        # 找到了但左邊可能還有 判斷左邊的事是相同不是就return這個（因為這是distinct）
        elif target == array[target] and array[target - 1] != target - 1:
            return target
        # 有找到且左邊是相同的繼續往左邊走
        else:
            right_idx = target - 1
        target = (left_idx + right_idx) // 2

    return -1


test = [-12, 1, 2, 3, 12]

indexEqualsValue(test)
