from datetime import datetime

def GetTime():
    now = datetime.now()
    return now
# datetime object containing current date and time

#currentTime = GetTime()
#print(currentTime.strftime('%I:%M %p'))
#print(currentTime.strftime('%A'))
#print(currentTime.strftime('%b %d, %Y'))
