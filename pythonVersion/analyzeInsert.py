import pymongo
import json

from matchups import matchups1v1helper
from matchups import matchups2v1helper
from matchups import matchups1v2helper
from matchups import matchups2v2helper
from matchups import matchups3v2helper
from matchups import matchups2v3helper
from matchups import matchups3v3helper

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['dota2stats']
db.matchups1v0.create_index([('h1', pymongo.ASCENDING)])
db.matchups1v1.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING)
])
db.matchups2v1.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING)
])
db.matchups1v2.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING)
])
db.matchups2v2.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING),
    ("h4", pymongo.ASCENDING)
])
db.matchups3v2.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING),
    ("h4", pymongo.ASCENDING),
    ("h5", pymongo.ASCENDING)
])
db.matchups2v3.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING),
    ("h4", pymongo.ASCENDING),
    ("h5", pymongo.ASCENDING)
])
db.matchups3v3.create_index([
    ("h1", pymongo.ASCENDING),
    ("h2", pymongo.ASCENDING),
    ("h3", pymongo.ASCENDING),
    ("h4", pymongo.ASCENDING),
    ("h5", pymongo.ASCENDING),
    ("h6", pymongo.ASCENDING)
])


def analyze1v0stats(match):
    global db
    for heroId in match['r']:
        heroEntry = db.matchups1v0.find_one({'h1': str(heroId)})
        if not heroEntry:
            heroEntry = {}
            heroEntry['s'] = {}
            heroEntry["h1"] = str(heroId)

        for ally in match['r']:
            if ally == heroId:
                continue

            if match['radiantWins']:
                if not str(ally) in heroEntry['s']:
                    heroEntry['s'][str(ally)] = {'t1w': 1, 't1l': 0, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(ally)]['t1w'] += 1
            else:
                if not str(ally) in heroEntry['s']:
                    heroEntry['s'][str(ally)] = {'t1w': 0, 't1l': 1, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(ally)]['t1l'] += 1

        for foe in match['d']:
            if not match['radiantWins']:
                if not str(foe) in heroEntry['s']:
                    heroEntry['s'][str(foe)] = {'t1w': 1, 't1l': 0, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(foe)]['t1w'] += 1
            else:
                if not str(foe) in heroEntry['s']:
                    heroEntry['s'][str(foe)] = {'t1w': 0, 't1l': 1, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(foe)]['t1l'] += 1
        db.matchups1v0.remove({"h1": heroEntry["h1"]})
        db.matchups1v0.insert_one(heroEntry)

    for heroId in match['d']:
        heroEntry = db.matchups1v0.find_one({'h1': str(heroId)})
        if not heroEntry:
            heroEntry = {}
            heroEntry['s'] = {}
            heroEntry["h1"] = str(heroId)
        for ally in match['d']:
            if ally == heroId:
                continue

            if not match['radiantWins']:
                if not str(ally) in heroEntry['s']:
                    heroEntry['s'][str(ally)] = {'t1w': 1, 't1l': 0, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(ally)]['t1w'] += 1
            else:
                if not str(ally) in heroEntry['s']:
                    heroEntry['s'][str(ally)] = {'t1w': 0, 't1l': 1, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(ally)]['t1l'] += 1

        for foe in match['r']:
            if not match['radiantWins']:
                if not str(foe) in heroEntry['s']:
                    heroEntry['s'][str(foe)] = {'t1w': 1, 't1l': 0, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(foe)]['t1w'] += 1
            else:
                if not str(foe) in heroEntry['s']:
                    heroEntry['s'][str(foe)] = {'t1w': 0, 't1l': 1, 't2w': 0, 't2l': 0}
                else:
                    heroEntry['s'][str(foe)]['t1l'] += 1

        db.matchups1v0.remove({"h1": heroEntry["h1"]})
        db.matchups1v0.insert_one(heroEntry)


def analyzeAndInsertMatch(match):
    global db
    matchups1v1helper.analyze1v1(match['r'], match['d'], match['radiantWins'], db)
    matchups2v1helper.analyze2v1(match['r'], match['d'], match['radiantWins'], db)
    matchups1v2helper.analyze1v2(match['r'], match['d'], match['radiantWins'], db)
    matchups2v2helper.analyze2v2(match['r'], match['d'], match['radiantWins'], db)
    matchups3v2helper.analyze3v2(match['r'], match['d'], match['radiantWins'], db)
    matchups2v3helper.analyze2v3(match['r'], match['d'], match['radiantWins'], db)
    matchups3v3helper.analyze3v3(match['r'], match['d'], match['radiantWins'], db)


f = open('dataSet1000.txt', 'r')
cnt = 0
for l in f.readlines():
    match = json.loads(l)
    analyzeAndInsertMatch(match)
    print cnt
    cnt += 1
    break