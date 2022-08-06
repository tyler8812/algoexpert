# O(c1 + c2) time | O(c1 + c2) space
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    update_calendar1 = update_calendar(calendar1, dailyBounds1)
    update_calendar2 = update_calendar(calendar2, dailyBounds2)
    print(update_calendar1, update_calendar2)
    # update_calendar: [[0, 540], [600, 700],...]
    merged_calendars = merge_calendars(update_calendar1, update_calendar2)
    flattened_calendars = flatten_calendars(merged_calendars)
    return get_matching_availabilities(flattened_calendars, meetingDuration)


def update_calendar(calendar, daily_bounds):
    updated_calendar = calendar[:]
    # add all unavailable time to list
    updated_calendar.insert(0, ["0:00", daily_bounds[0]])
    updated_calendar.append([daily_bounds[1], "23:59"])

    # '1:00' -> 60
    # '2:30' -> 2 * 60 + 30
    # transfer time string to minutes integer

    # m: ["0:00", "9:00"]
    return list(
        map(lambda m: [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calendar)
    )


def merge_calendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1

    return merged


def flatten_calendars(calendar):
    flattened = [calendar[0][:]]

    for i in range(1, len(calendar)):
        current_meeting = calendar[i]
        prev_meeting = flattened[-1]
        current_start, current_end = current_meeting
        prev_start, prev_end = prev_meeting
        # meeting is overlaped
        if prev_end >= current_start:
            new_prev_meeting = [prev_start, max(current_end, prev_end)]
            flattened[-1] = new_prev_meeting
        else:
            flattened.append(current_meeting[:])

    return flattened


def get_matching_availabilities(calendar, duration):
    print(calendar)
    matching_availabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        availability_duration = end - start
        if availability_duration >= duration:
            matching_availabilities.append([start, end])

    result = list(
        map(
            lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])],
            matching_availabilities,
        )
    )
    print(result)
    return result


def time_to_minutes(time):
    # input example: '2:30'
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    hours_string = str(hours)
    minutes_string = str(minutes) if minutes > 10 else "0" + str(minutes)
    return hours_string + ":" + minutes_string


calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
daily_bounds1 = ["0:00", "20:00"]
calendar2 = [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"],
]
daily_bounds2 = ["10:00", "18:30"]
meeting_duration = 30

calendarMatching(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration)
