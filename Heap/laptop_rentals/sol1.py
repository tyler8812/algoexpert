# bruteforce
# t: max time in time interval
# O(t*n) time |
def laptopRentals(times):
    max_laptop = float("-inf")
    max_time = float("-inf")
    for time in times:
        max_time = max(time[1], max_time)
    if max_time == float("-inf"):
        return 0
    for current_time in range(max_time):
        use_laptop = 0
        for time in times:
            if time[0] <= current_time and current_time < time[1]:
                use_laptop += 1
                max_laptop = max(max_laptop, use_laptop)
            print(time[0], time[1], current_time, use_laptop)
    return max_laptop


def is_overlap_in_two_interval(time1, time2):
    if time1[0] > time2[0] and time1[0] < time2[1]:
        return True
    elif time1[1] > time2[0] and time1[1] < time2[1]:
        return True
    elif time2[0] > time1[0] and time2[0] < time1[1]:
        return True
    elif time2[1] > time1[0] and time2[1] < time1[1]:
        return True
    return False


times = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]

print(laptopRentals(times))

# time1 = [0, 10]
# time2 = [8, 10]
# print(is_overlap_in_two_interval(time1, time2))
