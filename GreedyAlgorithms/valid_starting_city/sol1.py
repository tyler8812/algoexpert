def validStartingCity(distances, fuel, mpg):
    for i in range(len(fuel)):
        fuel[i] *= mpg
    for start_idx in range(len(distances)):
        remain_gass = 0
        for current_idx in range(start_idx, start_idx + len(fuel)):
            if remain_gass < 0:
                break
            current_idx %= len(fuel)
            remain_gass += fuel[current_idx] - distances[current_idx]
        if remain_gass >= 0:
            return start_idx

    # never get here
    return -1


distances = [10, 20, 10, 15, 5, 15, 25]
fuel = [0, 2, 1, 0, 0, 1, 1]
mpg = 20

validStartingCity(distances, fuel, mpg)
