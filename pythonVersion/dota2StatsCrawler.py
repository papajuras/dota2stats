import dota2api
import json
import time
start_seq_num = 1792780777
api = dota2api.Initialise('36A7239946D3AA33C7C678D78403E346')

res = api.get_match_history_by_seq_num(start_at_match_seq_num=1792780777, matches_requested=100)

f = open('matches.txt', 'w')
counter = 0
while True:
    matches = res["matches"]

    last_match_id = int(matches[-1]['match_seq_num']) + 1
    start_time = int(matches[-1]['start_time'])
    ranked_matches = [x for x in matches if x["lobby_type"] == 7]
    print last_match_id
    for match in ranked_matches:
        f.write(json.dumps(match))
        f.write('\n')
    counter = counter + len(ranked_matches)
    print "counter: " + str(counter) + " timestamp: " + str(start_time)
    while True:
        try:
            res = api.get_match_history_by_seq_num(start_at_match_seq_num=last_match_id, matches_requested=100)
            break
        except ValueError:
            print "Error, sleeping 1 sec"
            time.sleep(1)

    time.sleep(1.5)
    if counter > 100000:
        break
print last_match_id

f.close()

print "Done."
