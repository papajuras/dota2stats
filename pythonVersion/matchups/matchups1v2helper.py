def analyze1v2(team1, team2, team1wins, db):
    for i in range(0, 5):
        for j in range(i + 1, 5):
            foe_id = team2[i]
            foe2_id = team2[j]
            for hero_id in team1:
                hero_entry = db.matchups1v2.find_one({'h1': str(hero_id), 'h2': str(foe_id), 'h3': str(foe2_id)})
                if not hero_entry:
                    hero_entry = {'s': {}, 'h1': str(hero_id), 'h2': str(foe_id), 'h3': str(foe2_id)}

                for ally_id in team1:
                    if ally_id == hero_id:
                        continue

                    if team1wins:
                        if not str(ally_id) in hero_entry['s']:
                            hero_entry['s'][str(ally_id)] = {'t1w': 1, 't1l': 0, 't2w': 0, 't2l': 0}
                        else:
                            hero_entry['s'][str(ally_id)]['t1w'] += 1

                    else:
                        if not str(ally_id) in hero_entry['s']:
                            hero_entry['s'][str(ally_id)] = {'t1w': 0, 't1l': 1, 't2w': 0, 't2l': 0}
                        else:
                            hero_entry['s'][str(ally_id)]['t1l'] += 0

                for foe_ally_id in team2:
                    if foe_id == foe_ally_id or foe2_id == foe_ally_id:
                        continue
                    if team1wins:
                        if not str(foe_ally_id) in hero_entry['s']:
                            hero_entry['s'][str(foe_ally_id)] = {'t1w': 0, 't1l': 0, 't2w': 0, 't2l': 1}
                        else:
                            hero_entry['s'][str(foe_ally_id)]['t2l'] += 1

                    else:
                        if not str(foe_ally_id) in hero_entry['s']:
                            hero_entry['s'][str(foe_ally_id)] = {'t1w': 0, 't1l': 0, 't2w': 1, 't2l': 0}
                        else:
                            hero_entry['s'][str(foe_ally_id)]['t2w'] += 1

                db.matchups1v2.remove({'h1': str(hero_id), 'h2': str(foe_id), 'h3': str(foe2_id)})
                db.matchups1v2.insert_one(hero_entry)
