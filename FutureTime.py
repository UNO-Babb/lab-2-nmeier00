#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) %24
  currentMinute = (now.minute)
  

  #TODO:
  #Ask user for hours
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

now = datetime.datetime.now()
currentHour = (now.hour - 6) %24
currentMinute = (now.minute)
moreHours = input("enter in addtional hours: \n")
moreMins = input("enter in additional minutes:\n")
futureMins = (int(currentMinute) + int(moreMins)) %60
extraHour = (int(currentMinute) + int(moreMins)) //60
futureHour = (int(currentHour) + int(moreHours) + int(extraHour)) %24

print("Future time:")
print(str(futureHour) + ":" + str(futureMins) + " CST")
