count = int(input())

# g - games, w - won, d - draw, l - lost, p - points
table = {}


def updateTable(table, matchStr):
    match = matchStr.split(";")
    team1, goals1, team2, goals2 = match[0], int(match[1]), match[2], int(match[3])

    # init
    if team1 not in table.keys():
        table[team1] = {"g": 0, "w": 0, "d": 0, "l": 0, "p: 0}
    if team2 not in table.keys():
        table[team2] = {'g': 0, 'w': 0, 'd': 0, 'l': 0, 'p': 0}

    table[team1]['g'] += 1
    table[team2]['g'] += 1

    if goals1 > goals2:
        table[team1]['w'] += 1
        table[team2]['l'] += 1
        table[team1]['p'] += 3
    elif goals1 < goals2:
        table[team1]['l'] += 1
        table[team2]['w'] += 1
        table[team2]['p'] += 3
    else:
        table[team1]['d'] += 1
        table[team2]['d'] += 1
        table[team1]['p'] += 1
        table[team2]['p'] += 1

def printTable(table):
    for team, row in  table.items():
        print(team + ':' + str(row['g']) + ' '
            + str(row['w']) + ' ' + str(row['d']) + ' '
            + str(row['l']) + ' ' + str(row['p']))

for i in range(count):
    matchStr = input()
    updateTable(table, matchStr)

printTable(table)
