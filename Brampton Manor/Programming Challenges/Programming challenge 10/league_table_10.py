import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)                  ###   skip first row (header)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary = {}
    stats = {}
    referee = {}
    for row in rows:
        home,away,homegoals,awaygoals,winner,r = row[1],row[2],row[3],row[4],row[5],row[6]
        if r not in referee:
            referee[r] = [0,0,0]
        if home not in dictionary or home not in stats:
            dictionary[home] = [0,0,0,0,0] ##win, draw, lost, goal difference, points
            stats[home] = [0,0,0,0]
        if away not in dictionary or away not in stats:
            dictionary[away] = [0,0,0,0,0]
            stats[away] = [0,0,0,0]

        ## check if it is draw
        if winner == "D":
            dictionary[home][4] += 1
            dictionary[away][4] += 1

            dictionary[home][1] += 1
            dictionary[away][1] += 1

        ## winner is home
        if winner == "H":
            dictionary[home][4] += 3

            dictionary[home][0] += 1
            dictionary[away][2] += 1

        ## winner is away
        if winner == "A":
            dictionary[away][4] += 3

            dictionary[home][2] += 1
            dictionary[away][0] += 1

        ## goal difference for home and awat
        dictionary[home][3] += int(homegoals) - int(awaygoals)
        dictionary[away][3] += int(awaygoals) - int(homegoals)

        ## Most accurate team
        hshots, ashots,  hshotstarget, ashotstarget = row[7], row[8], row[9], row[10]
        stats[home][0] += int(hshots)
        stats[away][0] += int(ashots)
        stats[home][1] += int(hshotstarget)
        stats[away][1] += int(ashotstarget)

        ## Diriest Team
        stats[home][2] += int(row[11])
        stats[away][2] += int(row[12])


        ## Referee
        card = int(row[15]) + int(row[16]) + (3 *int(row[17])) + (3 * int(row[18]))
        referee[r][0] += card
        referee[r][1] += 1

    table(dictionary, stats, referee)

def table(dictionary, stats, referee):
    s = sorted(dictionary.items(), key=lambda e: e[1][4], reverse=True)
    s[13], s[14] = s[14], s[13]
    sort = {k:v for k, v in s}
    keysList = list(sort.keys())
    kList2 = list(referee.keys())
    print("Club {:<14} Won {:<11} Drawn {:<9} Lost {:<10} GD {:<12} Points".format(" ", " "," "," "," "))
    print("\n")
    for x in range(0,19):
        key = keysList[x]
        key2 = kList2[x]
        team = "{:<20}".format(key)


        accuracy = stats[key][1] / stats[key][0]
        stats[key][3] = accuracy
    
        for y in range (0,5):
            team += "{:<16}".format(sort[key][y])
        print(team)


        averageRef = referee[key2][0] / referee[key2][1]
        referee[key2][2] = averageRef

    
    sortFouls = sorted(stats.items(), key=lambda e: e[1][2])
    sortAccuracy = sorted(stats.items(), key=lambda e: e[1][3])
    sortReferee = sorted(referee.items(), key=lambda e: e[1][2])



    print("\n")
    print("The most acccurate team is {}".format(sortAccuracy[19][0]))
    print("The least accurate team is {}".format(sortAccuracy[0][0]))
    print("The dirtest team is {}".format(sortFouls[19][0]))
    print("The cleanest team is {}".format(sortFouls[0][0]))
    print("The referee with the highest card average is {}".format(sortReferee[18][0]))
    print("The referee with the lowest card average is {} and {}".format(sortReferee[0][0],sortReferee[1][0]))
              


if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    process_results(file_contents)
