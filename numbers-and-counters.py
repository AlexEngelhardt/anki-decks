import pandas as pd
import numpy as np

np.random.seed(20250424)


cfg = [
    ("", {  # no suffix, i.e. create plain numbers to read
          "n_random_cards": 20,
          "min_value": 100,
          "max_value": 1_000
          }
    ),
    ("", {  # Create 10 more cards for large numbers
          "n_random_cards": 10,
          "min_value": 1_000,
          "max_value": 1_000_000
          }
    ),
    ("つ", {
          "must_include": [1, 10],
          "n_random_cards": 10,
          "min_value": 11,
          "max_value": 100,
          }
     ),
    ("個", {
          "must_include": [1, 10],
          "n_random_cards": 10,
          "min_value": 11,
          "max_value": 100,
          },
    ),
    ("円", {
          "n_random_cards": 30,
          "min_value": 100,
          "max_value": 10_000,
          }
    ),
    ("ページ", {
          "n_random_cards": 20,
          "min_value": 10,
          "max_value": 200,
          }
    ),
]

result = []

for counter, counter_cfg in cfg:
    if "must_include" in counter_cfg:
        result = result + [
            str(i) + counter 
            for i in range(
                counter_cfg["must_include"][0],
                counter_cfg["must_include"][1] + 1
            )
        ]
    if "n_random_cards" in counter_cfg:
        random_ints = sorted(np.random.randint(counter_cfg["min_value"], counter_cfg["max_value"], size=counter_cfg["n_random_cards"]))
        result = result + [
            str(i) + counter
            for i in random_ints
        ]
    

# print(result)

result_df = pd.DataFrame(result, columns=["number"])
result_df.to_csv("japanese-numbers.csv", index=None, header=False)

