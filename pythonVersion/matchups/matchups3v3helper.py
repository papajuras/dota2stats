def analyze3v3(team1, team2, team1wins, db):
    for i in range(0, 5):
        for j in range(i + 1, 5):
            for k in range(0, 5):
                for l in range(k + 1, 5):
                    for m in range(j + 1, 5):
                        for n in range(l + 1, 5):
                            hero_id = team1[i]
                            hero2_id = team1[j]
                            hero3_id = team1[m]
                            foe_id = team2[k]
                            foe2_id = team2[l]
                            foe3_id = team2[n]
                            hero_entry = db.matchups3v3.find_one({'h1': str(hero_id), 'h2': str(hero2_id),
                                                                  'h3': str(hero3_id), 'h4': str(foe_id),
                                                                  'h5': str(foe2_id), 'h6': str(foe3_id)})
                            if not hero_entry:
                                hero_entry = {'s': {}, 'h1': str(hero_id), 'h2': str(hero2_id),
                                              'h3': str(hero3_id), 'h4': str(foe_id),
                                              'h5': str(foe2_id), 'h6': str(foe3_id)}

                            for ally_id in team1:
                                if ally_id == hero_id or ally_id == hero2_id or ally_id == hero3_id:
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
                                if foe_id == foe_ally_id or foe2_id == foe_ally_id or foe3_id == foe_ally_id:
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

                            db.matchups3v3.remove({'h1': str(hero_id), 'h2': str(hero2_id),
                                                   'h3': str(hero3_id), 'h4': str(foe_id),
                                                   'h5': str(foe2_id), 'h6': str(foe3_id)})
                            db.matchups3v3.insert_one(hero_entry)
