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
    assigns school_ac, oncampus, start, end and location attributes for socials/ECs
    '''
    obj.school_ac = 0 #attribute doesn't exist for ECs/socials 
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
        school_start = i #track where the school events start
    elif "ECs" in line:
        num_EC = int(line[1]) #get number of EC
        EC_start = i #track where the ECs start
    elif "SOCIAL" in line:
        num_social = int(line[1]) #get number of socials
        social_start = i #track where the socials start
    elif ('' not in line): #check if line is empty
        event_obj = Activity()
        event_obj.name = line[0] 

        if(num_school is not None): #check if we already have the number 
            if(i>school_start and i<=school_start+num_school): #if this is a school event
                event_obj.category = "School" #assign category
                event_obj.school_ac = line[1] #assign the type of school activity (labs/lec/tut)
                event_obj.location = line[2] #assign location
                event_obj.oncampus = True #assign oncampus flag to be true to indicate it is on campus
                day_and_time = line[3].split(' ') #split day and time with spacing 
                times = day_and_time[1].split('-') #split start and end times
                event_obj.start = split_time(times[0]) # call function to convert the time to an int and assign them to start and end times
                event_obj.end = split_time(times[1])
                event_obj.day = day_and_time[2] #assign day of the week to day attribute

        if(num_EC is not None): #check if we already have the number 
            if(i> EC_start and i<=EC_start+num_EC):#if this is an EC
                event_obj.category = "EC" 
                assign_attributes(line, event_obj) #call function to assign attribute
            
        if(num_social is not None):
            if(i> social_start and i<=social_start+num_social): #if this is a social
                event_obj.category = "Social"
                assign_attributes(line, event_obj) #call function to assign attribute

        Activity_list.append(event_obj)



