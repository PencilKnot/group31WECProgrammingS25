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

def find_gaps(activities):
    gaps = []
    # if whole day is empty
    if len(activities) == 0: gaps.append((420, 1380))
    else:
        # morning gap (7:00 - )
        if activities[0].start > 420:
            gaps.append((420, activities[0].start))
        # gaps between daily activities
        for i in range(1, len(activities)):
            if activities[i-1].end < activities[i].start:
                gaps.append((activities[i-1].end, activities[i].start))
        # evening gap
        if activities[-1].end < 1380:
            gaps.append((activities[-1].end, 1380))

    return gaps

# since all school activities are scheduled, assumes only ECs/social
def true_value(a, travel):
    score = 0;
    match a.category:
        case 'EC':
            score = 0.75
        case 'Social':
            score = 0.5
    
    return score/(a.end - a.start + travel)

# check if activity fits in gap given
def fits_gap(a1, a2, duration):
    # if not morning gap (somewhere to go from)
    if(a1 != 0):
        return False if ((a2.end - a2.start + get_travel_time(a1, a2) > duration)) else True
    else:
        return False if (a2.end - a2.start > duration) else True

def optimize_schedule(activity_list):
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    schedule = {day: [] for day in days}
    activity_list[:] = [a for a in activity_list if not during_sleep(a)]

    # put all school activities with dates into schedule first
    for day in days:
        current_day = []
        i = 1
        for a in activity_list:
            if(a.category == 'School' and a.day == current_day):
                current_day.append(a);
        current_day.sort(key=lambda a: a.start)

        while i < len(current_day):
            prev = current_day[i-1]
            curr = current_day[i]

            # idk how to do multiple conflicts
            if has_conflict(prev, curr) or not enough_travel_time(prev, curr):
                if(get_priority(prev) > get_priority(curr)):
                    current_day.pop(i)
                else:
                    current_day.pop(i-1)
                    i = max(1, i-1)
            else: i += 1

        schedule[day] = current_day;
    
    # SCHEDULE STUDY TIME MIN 5 HOURS

    # knapsack problem?
    ordered_activities = []
    for i in range(0, len(activity_list)):
        if((a.category == 'EC' or a.category == 'Social')):
            ordered_activities.append((true_value(a), a))
    ordered_activities.sort(reverse=True)

    # need to add code to find best activity that fits in the current gap
    

    return schedule
