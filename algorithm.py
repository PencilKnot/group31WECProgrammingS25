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
        case ' lecture': return 2
        case ' lab': return 1.5
        case ' tutorial': return 0.75

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
    score = 0
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

    # put all school activities with dates into schedule first
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    schedule = {day: [] for day in days}

    ordered_activities = []
    for a in activity_list:
        if(a.day == ""):
            ordered_activities.append((true_value(a), a))
    ordered_activities.sort(reverse=True)

    # list of all ordered activities without score value
    to_place = [a for _, a in ordered_activities]

    # put all school activities with dates into schedule first
    for day in days:
        current_day = []
        i = 1
        for a in activity_list:
            if a.category == 'School' and a.day == day and not during_sleep(a):
                current_day.append(a);
        current_day.sort(key=lambda a: a.start)

        while i < len(current_day):
            prev = current_day[i-1]
            curr = current_day[i]

            # idk how to do multiple conflicts
            if (has_conflict(prev, curr) or not enough_travel_time(prev, curr)) and not during_sleep(a):
                if(get_priority(prev) > get_priority(curr)):
                    current_day.pop(i)
                else:
                    current_day.pop(i-1)
                    i = max(1, i-1)
            else: i += 1
    
        schedule[day] = current_day;
    
    # greedy placing
    for day in days:
        current_day = schedule[day]
        changed = True;
    
        while changed:
            changed = False
            gap_list = find_gaps(current_day)

            # two variable for because tuples
            for gap_start, gap_end in gap_list:
                for i, activity in enumerate(to_place):
                    duration = activity.end - activity.start;

                    if activity.start >= gap_start and activity.end <= gap_end:
                        index = 0;
                        prev_time = True
                        next_time = True
                        prev_activity = None
                        next_activity = None
                        # find correct position to insert activity into current_day list
                        while index < len(current_day) and current_day[index].start < activity.start:
                            index += 1;
                        
                        # get previous and next activities already scheduled
                        if index > 0:
                            prev_activity = current_day[index - 1] 
                        if index < len(current_day):
                            next_activity = current_day[index]

                        if prev_activity:
                            prev_time = (activity.start - prev_activity.end) >= get_travel_time(prev_activity, activity)
                        if next_activity:
                            next_time = (next_activity.start - activity.end) >= get_travel_time(activity, next_activity)

                        if prev_time and next_time:
                            activity.day = day
                            current_day.insert(index, activity)
                            to_place.pop(i)
                            changed = True
                            break
                    
                    if changed:
                        break

        schedule[day] = current_day

    
    # SCHEDULE STUDY TIME MIN 5 HOURS

    # knapsack problem?
    ordered_activities = []
    for i in range(0, len(activity_list)):
        if((a.category == 'EC' or a.category == 'Social')):
            ordered_activities.append((true_value(a), a))
    ordered_activities.sort(reverse=True)

    school_score = 0
    EC_score = 0
    Social_score = 0


    for day in schedule:
        
        for activity in schedule[day]: #traverse every day's schedule in the week
            
            if (activity.category == "School"): #calculate and sums scores according to category and type of school activity

                if(activity.school_ac == " lecture"):
                    school_score = school_score + 2
                elif(activity.school_ac == " lab"):
                    school_score = school_score + 1.5
                elif(activity.school_ac == " tutorial"):
                    school_score = school_score + 0.75
                elif(activity.study == " study"):
                    school_score = school_score + ((activity.end - activity.start)/60)*0.5
            elif (activity.category == "EC"): 
                EC_score = EC_score + 1
            else:
                Social_score = Social_score + 1 
    
    for event in activity_list: #traverse the entire list of desired events
        if(event.category == "School"):#find the ones in school
            if activity not in schedule[event.day]: #check if they are scheduled on the day they should be scheduled
                if(activity.school_ac == " lecture"): #deduct school score accordingly if they are not scheduled
                    school_score = school_score - 2
                elif(activity.school_ac == " lab"):
                    school_score = school_score - 1.5
                elif(activity.school_ac == " tutorial"):
                    school_score = school_score - 0.75
    
        
    total_score = school_score + 0.75*EC_score + 0.5*Social_score #calculates composite score
    
    # need to add code to find best activity that fits in the current gap
    
    return schedule
