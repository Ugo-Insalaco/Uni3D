import json

with open('train_dataids.json') as f:
    data = json.load(f)

print(len(data))
with open('train_dataids.txt','w') as out:
    out.writelines([','.join(line)+'\n' for line in data])