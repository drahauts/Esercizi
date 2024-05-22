def seconds_since_noon (hours: int, minutes: int, seconds: int):
    secondi = (hours * 3600) + (minutes * 60) + seconds
    return secondi


def time_difference(hour_a: int, minutes_a: int, seconds_a: int, hour_b: int, minutes_b: int, seconds_b: int) -> int:
    if hour_a > hour_b:
        return seconds_since_noon(hour_a,minutes_a, seconds_a) - seconds_since_noon(hour_b,minutes_b,seconds_b)
    else:
        return seconds_since_noon(hour_b, minutes_b, seconds_b) - seconds_since_noon(hour_a, minutes_a, seconds_a)

print(time_difference(1, 0, 0, 3, 15, 30))