import pandas as pd

match_ids = []
champions_used = []
participants = []
counter = 0

for i in range(0, 4201, 50):
    data = pd.read_csv("dataset_champions" + str(i) + ".csv")
    match_ids.extend(data['match_id'])
    champions_used.extend(data['champions_used'])
    participants.extend(data['participants'])
    counter+=1


for i in range(4400, 9851, 50):
    data = pd.read_csv("dataset_champions" + str(i) + ".csv")
    match_ids.extend(data['match_id'])
    champions_used.extend(data['champions_used'])
    participants.extend(data['participants'])
    counter+=1


print(len(match_ids))
print(len(champions_used))
print(len(participants))
print(counter)

headers = ["match_id", "champions_used", "participants"]
data = {'match_id': match_ids, 'champions_used': champions_used, 'participants': participants}
df = pd.DataFrame(data)
df.to_csv("dataset_champions_total.csv", encoding='utf-8', index=False, columns=headers)