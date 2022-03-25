# O(nlog(n))
def laptopRentals(times):
    start_time = [time[0] for time in times]
    end_time = [time[1] for time in times]
    start_time.sort()
    end_time.sort()

    start_iterator = 0
    end_iterator = 0
    laptop = 0
    while start_iterator < len(start_time):
        if start_time[start_iterator] >= end_time[end_iterator]:
            laptop -= 1
            end_iterator += 1
        laptop += 1
        start_iterator += 1

    return laptop


times = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]

print(laptopRentals(times))
