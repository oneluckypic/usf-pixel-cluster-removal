
import json
import pandas as pd
import yaml


def dfread(json_file):
    with open(json_file, 'r') as file:
        return pd.DataFrame.from_dict(yaml.safe_load(file))


def dfwrite(df, json_file):
    with open(json_file, 'w') as file:
        json.dump(df.to_dict(), file, indent=4, sort_keys=True)
