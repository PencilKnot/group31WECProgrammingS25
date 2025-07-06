days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
schedule = {day: [] for day in days}

def has_conflict(a1, a2):
    return not(a1.end >= a2.start or a2.end <= a1.start)

def get_travel_time(a1, a2):
    return 25 if (a1.oncampus == a2.oncampus and a1.oncampus) else 15

def enough_travel_time(a1, a2):
    return (a2.start - a1.end) >= get_travel_time(a1, a2)

def during_sleep(a):
    return True if (a.start < 1380 and a.end < 1380 and a.start > 420 and a.end > 420) else False

def get_priority(a):
    match a.type:
        case 'Lecture': return 2
        case 'Lab': return 1.5
        case 'Tutorial': return 0.75

def optimize_schedule(activity_list):
    # put all school activities with dates into schedule first
    for day in days:
        current_day = []
        i = 1
        for a in activity_list:
            if(a.category == 'School' and a.day == day and not(during_sleep(a))):
                current_day.append(a);
        current_day.sort(key=lambda a: a.start)

        while i < len(current_day):
            prev = current_day[i-1]
            curr = current_day[i]

            if has_conflict(prev, curr) or not enough_travel_time(prev, curr):
                if(get_priority(prev) > get_priority(curr)):
                    current_day.pop(i)
                else:
                    current_day.pop(i-1)
                    i = max(1, i-1)
            else: i += 1

        schedule[day] = current_day;
