import json
import algorithm

monday= {

}

tuesday= {

}

wednesday= {

}

thursday= {

}

friday= {

}

saturday= {

}

sunday= {

}

scheduledict = {
    monday,
    tuesday,
    wednesday,
    thursday,
    friday, 
    saturday, 
    sunday,
}

mondaylist = []
tuesdaylist = []
wednesdaylist = []
thursdaylist = []
fridaylist = []
saturdaylist = []
sundaylist = []
currentitem = []


schedule = algorithm.optimize_schedule()
listofdicts = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]
listoflists = [mondaylist,tuesdaylist,wednesdaylist,thursdaylist,fridaylist,saturdaylist,sundaylist]
listofacronyms = ["Mo","Tu","We","Th","Fr","Sa","Su"]


for activity in schedule:

    activity_day = activity.day

    for acronym_index in range(len(listofacronyms)-1):
        curr_acronym = listofacronyms[acronym_index]
        if activity_day == curr_acronym:
            currentitem.append(activity.name)
            currentitem.append(activity.start)
            currentitem.append(activity.end)
            listoflists[acronym_index].append(currentitem)
            currentitem.clear()
            
currentlistindict = []

#formats each dict
for dayindex in range(len(listoflists)-1):
    currentlist = listoflists[dayindex]
    currentdict = listofdicts[dayindex]
    for activity in currentlist:
        currentlistindict = activity[1:]
        currentdict.update({activity[0]: currentlistindict})
        currentlistindict.clear()

# Serializing json
json_object = json.dumps(scheduledict, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
