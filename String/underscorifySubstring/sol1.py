def underscorifySubstring(string, substring):
    locations = collapse(get_locations(string=string, substring=substring))
    return under_scorify(string, locations)


def get_locations(string, substring):
    locations = []
    start_idx = 0
    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)
        if next_idx != -1:
            locations.append([next_idx, next_idx + len(substring)])
            start_idx = next_idx + 1
        else:
            break
    print(locations)
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    new_locations = [locations[0]]
    prev_location = locations[0]
    for i in range(1, len(locations)):
        current_location = locations[i]
        if current_location[0] <= prev_location[1]:
            prev_location[1] = current_location[1]
        else:
            new_locations.append(current_location)
            prev_location = current_location

    print(new_locations)
    return new_locations


def under_scorify(string, locations):
    string_idx = 0
    locations_idx = 0
    is_left_under_score = True
    final_chars = []
    while string_idx < len(string) and locations_idx < len(locations):
        if is_left_under_score:
            if string_idx == locations[locations_idx][0]:
                final_chars.append("_")
                is_left_under_score = False
        else:
            if string_idx == locations[locations_idx][1]:
                final_chars.append("_")
                is_left_under_score = True
                locations_idx += 1
        final_chars.append(string[string_idx])
        string_idx += 1

    if locations_idx < len(locations):
        final_chars.append("_")
    elif string_idx < len(string):
        final_chars.append(string[string_idx:])
    return "".join(final_chars)


string = "testest is a testtest to see if testestest it works"
substring = "test"
print(underscorifySubstring(string, substring))
