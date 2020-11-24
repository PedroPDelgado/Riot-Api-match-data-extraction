import pandas as pd
import collections
from ast import literal_eval


champions_win = []
champions_defeat = []
unique_champions_won = set()

data = pd.read_csv("dataset_champions_total.csv", converters={"champions_used": literal_eval})
data_winners = pd.read_csv("winnner.csv")

for i in range(len(data['match_id'])):
    champions_win.extend(data['champions_used'][i][0:5]) if data_winners['blueWins'][i] == 1 else champions_win.extend(data['champions_used'][i][5:10])
    champions_defeat.extend(data['champions_used'][i][5:10]) if data_winners['blueWins'][i] == 1 else champions_defeat.extend(data['champions_used'][i][0:5])
    unique_champions_won.update(data['champions_used'][i][0:5]) if data_winners['blueWins'][i] == 1 else unique_champions_won.update(data['champions_used'][i][5:10])


counter_wins = collections.Counter(champions_win)
counter_defeats = collections.Counter(champions_defeat)

print(len(unique_champions_won))

win_rates = {}
for champion in unique_champions_won:
    win_rates[champion] = counter_wins[champion] / (counter_wins[champion] + counter_defeats[champion])

print(counter_wins)
print(counter_defeats)
print(win_rates)

blueSideChampionWrChance = []

for i in range(len(data['match_id'])):
    wr = 0
    for j in range(10):
        if j < 5:
            wr += win_rates[data['champions_used'][i][j]]
            #print("somando win rate de", data['champions_used'][i][j], " que é: ", win_rates[data['champions_used'][i][j]])
        else:
            wr -= win_rates[data['champions_used'][i][j]]
            #print("subtraindo win rate de", data['champions_used'][i][j], " que é: ", win_rates[data['champions_used'][i][j]])
    blueSideChampionWrChance.append(wr)

print(blueSideChampionWrChance)

headers = ["matchId", "blueSideChampionWrChance"]
out_data = {'matchId': data['match_id'], 'blueSideChampionWrChance': blueSideChampionWrChance}
df = pd.DataFrame(out_data)
df.to_csv("dataset_final.csv", encoding='utf-8', index=False, columns=headers)