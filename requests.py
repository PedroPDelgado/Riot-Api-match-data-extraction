from socket import timeout

import requests
import json
import pandas as pd
import time
import champion_info

api_key = "RGAPI-5bc81289-aca1-45e7-b81a-c7f8e5779e7e"
match_v4_url = "https://euw1.api.riotgames.com/lol/match/v4/matches/"
ci = champion_info.ChampionInfo()


in_match_ids = pd.read_csv("match_ids.csv")
out_match_ids = []
out_champions_used = []
out_participants = []


for i in range(0, len(in_match_ids['id'])):
    match_id = in_match_ids['id'][i]
    champions_used = []
    participants = []
    response = requests.get(match_v4_url + str(match_id) + "?api_key=" + api_key, timeout=1000).json()
    time.sleep(1.5)
    print("request número: ", i)
    print(response)
    for j in range(len(response['participants'])):
        champions_used.append(ci.get_champion_name(response['participants'][j]['championId']))
        participants.append(response['participantIdentities'][j]['player']['summonerId'])

    out_match_ids.append(match_id)
    out_champions_used.append(champions_used)
    out_participants.append(participants)

headers = ["match_id", "champions_used", "participants"]
data = {'match_id': out_match_ids, 'champions_used': out_champions_used, 'participants': out_participants}
df = pd.DataFrame(data)
df.to_csv("dataset_champions" + str(i) + ".csv", encoding='utf-8', index=False, columns=headers)