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

# put all school activities with dates into schedule first
for activity in activity_list:
    if activity.category == 'School' and activity.day:
        schedule[activity.day].append(activity)

# sort each day by start time (ASSUME NO CONFLICTS???)
for day in schedule:
    schedule[day].sort(key=lambda activity: activity.start)
    
