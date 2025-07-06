import json
from activity import Activity

# Open function to open the file "MyFile1.txt"
# (same directory) in read mode ("r")
# if the file is in a different directory provide the relative path

file1 = open("sampleinput.txt","r")
#file_content = file1.read() # stores the entire file content of the file as a string into the file_content variable
 #remove brackets
file_lines = file1.readlines() # stores each line of the file as an element of a list

def split_time(times):
    '''
    returns time as an integer value of the nth minute of the day
    '''
    time = times.split(':') #splits time into where time[0] = hours and time[1] = minutes
    return (int(time[0])*60 + int(time[1]))

def assign_attributes(line, obj):
    '''
    assigns school_ac, oncampus and location attributes for socials/ECs
    '''
    obj.school_ac = 0
    obj.location = line[1]
    if(line[2]==" false"):
        obj.oncampus = False
    else:
        obj.oncampus = True
    times = line[3].split('-') #split start and end times
    obj.start = split_time(times[0]) #start time as an integer
    obj.end = split_time(times[1]) #end time as an integer
    



Activity_list = []#initial empty list of activities
num_school = None
num_EC = None
num_social = None

for i in range (len(file_lines)):
    file_line = file_lines[i].replace('(', '').replace(')', '').replace('\n','') # deletes brackets
    line = file_line.split(',') #split things by comma
    print (line)
    if "SCHOOL" in line:
        num_school = int(line[1]) #get number of school events
        school_start = i
    elif "ECs" in line:
        num_EC = int(line[1]) #get number of EC
        EC_start = i
    elif "SOCIAL" in line:
        num_social = int(line[1]) #get number of socials
        social_start = i
    else:
        if ('' not in line):
            event_obj = Activity()
            event_obj.name = line[0]

            if(num_school is not None):
                if(i>school_start and i<=school_start+num_school):
                    event_obj.category = "School"
                    event_obj.school_ac = line[1]
                    event_obj.location = line[2]
                    event_obj.oncampus = True
                    day_and_time = line[3].split(' ')
                    times = day_and_time[1].split('-')
                    event_obj.start = split_time(times[0])
                    event_obj.end = split_time(times[1])
                    event_obj.day = day_and_time[2]



                    
            
            if(num_EC is not None):
                if(i> EC_start and i<=EC_start+num_EC):
                    event_obj.category = "EC"
                    assign_attributes(line, event_obj)
            
            if(num_social is not None):
                if(i> social_start and i<=social_start+num_social):
                    event_obj.category = "Social"
                    assign_attributes(line, event_obj)
            Activity_list.append(event_obj)

            
        
     
for x in range (len(Activity_list)):
    print(Activity_list[x].name, '|', Activity_list[x].category, '|', Activity_list[x].school_ac, '|', Activity_list[x].location, '|', Activity_list[x].oncampus, '|', Activity_list[x].start, '|', Activity_list[x].end, '|', Activity_list[x].day)
    
file1.close() # make sure to close the file before opening in different mode
# RIPPED STRAIGHT FROM GFG

'''

dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}



# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
'''


