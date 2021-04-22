def task2():
    h = float(input("Input day time: "))

    d = {
        "morning" : range(6, 12),
        "day" : (12: 18),
        "evening" : {
            "start" : 18,
            "end" :24
        }
    }

    if h in d['morning']:
        ...
    elif d['day'][0] <= h < d['day'][1]:
        ...
    elif d['evening']["start"] <= h < d['evening']["end"]:
        ...
