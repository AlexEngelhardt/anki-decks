import pandas as pd
import random

random.seed(20250424)


cfg = {
    "": {  # no suffix, i.e. create plain numbers to read
        "n_cards": 10,
        "min_value": 100,
        "max_value": 1_000_000
    },
    "つ": {
        "must_include": [1, 10],
        "n_cards": 10,  # TODO make sure that cards don't repeat
        "min_value": 11,
        "max_value": 100,
    },
    "個": {
        "must_include": [1, 10],
        "n_random_cards": 10,
        "min_value": 11,
        "max_value": 100,
    }
}

result = []

for counter, counter_cfg in cfg.items():
    if "must_include" in counter_cfg:
        result = result + [str(i) + counter for i in range(counter_cfg["must_include"][0], counter_cfg["must_include"][1]+1)]

print(result)

