import json
import pickle

with open("config.json", "r") as f:
    config = json.load(f)

config["logging"]["level"] = 'DEBUG'
with open ('config.pkl', 'wb') as f:
    pickle.dump(config, f)

with open ('config.pkl', 'rb') as f:
    show = pickle.load(f)
    print(show)