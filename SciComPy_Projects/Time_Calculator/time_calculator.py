
# Project available in https://repl.it/@lastlost/boilerplate-time-calculator#time_calculator.py

def find_day(given_day, add_days) :
    given_day = given_day.upper()
    day = ""

    if given_day == "SUNDAY" :
        day = "0"
    elif given_day == "MONDAY" :
        day = "1"
    elif given_day == "TUESDAY" :
        day = "2"
    elif given_day == "WEDNESDAY" :
        day = "3"
    elif given_day == "THURSDAY" :
        day = "4"
    elif given_day == "FRIDAY" :
        day = "5"
    elif given_day == "SATURDAY" :
        day = "6"

    day = str((int(day) + int(int(add_days))) % 7)

    if int(day) == 0 :
        day = "SUNDAY"
    elif int(day) == 1 :
        day = "MONDAY"
    elif int(day) == 2 :
        day = "TUESDAY"
    elif int(day) == 3 :
        day = "WEDNESDAY"
    elif int(day) == 4 :
        day = "THURSDAY"
    elif int(day) == 5 :
        day = "FRIDAY"
    elif int(day) == 6 :
        day = "SATURDAY"

    return day.capitalize()

def add_time(start, duration, daygiven = False):
    result_day = "0"
    result_hr = "0"
    result_min = "0"
    temp = start.split()
    amorpm = temp[1]
    temp = temp[0].split(":")
    hr = temp[0]
    min = temp[1]
    add_duration = duration.split(":")

    if int(min) + int(add_duration[1]) < 60 :
        result_min =  str(int(min) + int(add_duration[1]))
    elif int(min) + int(add_duration[1]) >= 60 :
        result_min = str((int(min) + int(add_duration[1])) % 60)
        result_hr = str(1)

    if int(result_min) < 10 :
        result_min = "0" + result_min

    if int(result_hr) + int(hr) + int(add_duration[0]) < 12 :
        result_hr = str(int(result_hr) + int(hr) + int(add_duration[0]))
    elif (int(result_hr) + int(hr) + int(add_duration[0])) % 12 == 0 :
        if (int(result_hr) + int(hr) + int(add_duration[0])) % 24 == 12 :
            result_hr = str(12)
            if amorpm == "AM" :
                amorpm = "PM"
                result_day = str(int((int(hr) + int(add_duration[0]))/24))
            elif amorpm == "PM" :
                amorpm = "AM"
                result_day = str(int((int(hr) + int(add_duration[0]))/24) + 1)
        elif (result_hr + int(hr) + int(add_duration[0])) % 24 == 0 :
            result_hr = str(12)
            result_day = str(int((int(hr) + int(add_duration[0]))/24))
    elif int(result_hr) + int(hr) + int(add_duration[0]) % 12 != 0 :
        if (int(result_hr) + int(hr) + int(add_duration[0])) % 24 < 12 :
            result_hr = str((int(result_hr) + int(hr) + int(add_duration[0])) % 12)
            result_day = str(int((int(hr) + int(add_duration[0]))/24))
        elif (int(result_hr) + int(hr) + int(add_duration[0])) % 24 > 12 :
            result_hr = str((int(result_hr) + int(hr) + int(add_duration[0])) % 12)
            if amorpm == "AM" :
                amorpm = "PM"
                result_day = str(int((int(hr) + int(add_duration[0]))/24))
            elif amorpm == "PM" :
                amorpm = "AM"
                result_day = str(int((int(hr) + int(add_duration[0]))/24) + 1)

    new_time = result_hr + ":" + result_min + " " + amorpm

    if daygiven != False :
        new_time = new_time.rstrip() + ", " + find_day(daygiven, result_day)

    if result_day == "0" :
        new_time = new_time.rstrip()
    elif result_day == "1" :
        new_time = new_time + " (next day)"
    else :
        new_time = new_time + " (" + str(result_day) + " days later)"

    return new_time
