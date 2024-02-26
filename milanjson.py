import requests
from datetime import datetime, timedelta

headers = { 'X-Auth-Token': 'cc99d6b0d1024981b61b21fb606e4a48' }
url = "https://api.football-data.org/v4/competitions/SA/standings"
#print("getting standings")
resp = requests.get(url=url, headers=headers, verify=False)
data = resp.json()["standings"] # Check the JSON Response Content documentation below
#print(data)

# Define the class
class TableTeam:
    def __init__(self, pos, teamName, point, crestURI):
        self.pos = pos
        self.teamName = teamName
        self.point = point
        self.crestURI = crestURI

tableTeam = []
def GetTable():
        
    for item in data:
        # Get the table element
        table = item["table"]
        # Loop through the table
        for row in table:
            # Get the team element
            team = row["team"]
            # Get the position, crest, name and points of the team
            position = row["position"]
            name = team["tla"]
            points = row["points"]
            crest = team["crest"]
            teamId = team["id"]
            # Print the name and points of the team
            #print(position, name, points, crest)
            # Create an array of Person objects using a list comprehension
            newTeam = TableTeam(position, name, points, crest)
            tableTeam.append(newTeam)
            
    # Print the names of each team in the array
    #for single in tableTeam:
       # print(single.teamName)

    # Find Milan's position
    # Define a variable to store the result
    found = None

    # Loop over the array
    for single in tableTeam:
        # Check if the person's name matches the name you are looking for
        if single.teamName == "MIL":
            # If yes, assign the person to the result variable and break the loop
            found = single
            break



    #find Milan's position
    milanPos = 0
    startPos = 0 
    endPos = 0

    if found is not None:
        #print("Found:", found.teamName, found.pos)
        milanPos = found.pos
        #subtract 2 with a minimum of 1
        startPos = max(milanPos - 2, 1)
        if milanPos < 17:
            endPos = startPos + 4
        else:
            startPos = 16
            endPos = 20
        
        #print(startPos)
        #print(endPos)
        
        #grab all the teams around milan
        for single in tableTeam:
            if startPos <= single.pos <= endPos:
                print(single.pos, single.teamName, single.point, single.crestURI)

    else:
        print("Not found")
    

#Grab fixtures
def GetFixtures():
        
    current_date = datetime.now()
    end_date = current_date + timedelta(days=30)
    # Format the date
    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_end_date = end_date.strftime("%Y-%m-%d")

    matchesURI = 'https://api.football-data.org/v4/teams/98/matches?dateFrom=' + formatted_date + '&dateTo=' + formatted_end_date + '&limit=5'
    respMatches = requests.get(url=matchesURI, headers=headers, verify=False)
    dataMatches = respMatches.json()["matches"]

    match = dataMatches[0]
    #print(dataMatches)
    #for match in dataMatches:
    matchDate = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
    convertedMatchDate = matchDate.strftime("%m/%d")
    homeTeam = match["homeTeam"]["shortName"]
    awayTeam = match["awayTeam"]["shortName"]
        #print(convertedMatchDate)
        #if match["homeTeam"]["shortName"] == "Milan":
            #print('v ' + match["awayTeam"]["shortName"])
        #else:
            #print('@ ' + match["homeTeam"]["shortName"])
    return convertedMatchDate, homeTeam, awayTeam
