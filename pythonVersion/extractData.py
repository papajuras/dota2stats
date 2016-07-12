
import json

f = open("matches.txt", "r")
f2 = open("matchesData.txt", "w")
cnt = 0
for l in f.readlines():
    match = json.loads(l)
    limitedDataMatch = {}
    radiant = []
    dire = []
    for player in match["players"]:
        if player["player_slot"] < 5:
            radiant.append(player["hero_id"])
        else:
            dire.append(player["hero_id"])

    limitedDataMatch["r"] = sorted(radiant)
    limitedDataMatch["d"] = sorted(dire)
    limitedDataMatch["radiantWins"] = match["radiant_win"]
    f2.write(json.dumps(limitedDataMatch))
    f2.write('\n')

    cnt = cnt + 1
    if cnt % 1000 == 0:
        print cnt

f2.close()
