import json
from activity import Activity

# Open function to open the file "MyFile1.txt"
# (same directory) in read mode ("r")
# if the file is in a different directory provide the relative path

file1 = open("MyFile1.txt","r")
file_content = file1.read() # stores the entire file content of the file as a string into the file_content variable
file_content = file_content.replace('(', '').replace(')', '') #remove brackets
file_lines = file1.readlines() # stores each line of the file as an element of a list

def split_time(times):
    '''
    returns time as an integer value of the nth minute of the day
    '''
    time = times.split(':') #splits time into where time[0] = hours and time[1] = minutes
    return (time[0]*60 + time[1])

Activity_list = []
num_school = None
num_EC = None
num_social = None

for i in range (len(file_lines)):
    line = file_lines[i].split(',') #split things by comma 
    if "SCHOOL" in line:
        num_school = line[1] #get number of school events
        school_start = i
    elif "ECs" in line:
        num_EC = line[1] #get number of EC
        EC_start = i
    elif "SOCIAL" in line:
        num_social = line[1] #get number of socials
        social_start = i
    else:
        event_obj = Activity()
        event_obj.name = line[0]
        if(num_school is not None):
            if(i>school_start and i<=school_start+num_school):
                event_obj.category = "School"
                
        if(num_EC is not None):
            if(i> EC_start and i<=EC_start+num_EC):
                event_obj.category = "EC"
        if(num_EC is not None):
            if(i> EC_start and i<=EC_start+num_EC):
                event_obj.category = "Social"
        for j in range (len(line)):
            if ':' in line[j]: #finds the times
                times = line[j].split('-') #split start and end times
                event_obj.start = split_time(times[0]) #start time as an integer
                event_obj.end = split_time(times[1]) #end time as an integer

        





    
        



file1.close() # make sure to close the file before opening in different mode

file1_w = open("MyFile1.txt", "w") # deletes all contents of the file and opens it for write mode ("w")

L = ["Hello\n", "World\n"]

file1_w.write("Hello") # writes hello to the file without adding a new line
file1_w.write("Hello\n") # same as above but starts a new line
file1_w.writelines(L) # pass in a list of strings and python writes each element of the list as a new line

file1_w.close()

# RIPPED STRAIGHT FROM GFG

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



