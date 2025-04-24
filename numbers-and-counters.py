import pandas as pd
import numpy as np

np.random.seed(20250424)

# For furigana and readings, pykakasi doesn't work well. I might have to implement something myself.

cfg = [
    (
        "",
        {  # no suffix, i.e. create plain numbers to read
            "n_random_cards": 20,
            "min_value": 100,
            "max_value": 1_000,
            "tags": "counters::plain",
        },
    ),
    (
        "",
        {  # Create 10 more cards for large numbers
            "n_random_cards": 10,
            "min_value": 1_000,
            "max_value": 1_000_000,
            "tags": "counters::plain",
        },
    ),
    (
        "つ",
        {
            "must_include": [1, 9],
            "tags": "counters::tsu",
        },
    ),
    (
        "個",
        {
            "must_include": [1, 10],
            "n_random_cards": 10,
            "min_value": 11,
            "max_value": 100,
            "tags": "counters::small-things",
        },
    ),
    (
        "円",
        {
            "n_random_cards": 30,
            "min_value": 100,
            "max_value": 10_000,
            "tags": "counters::yen",
        },
    ),
    (
        "ページ",
        {
            "n_random_cards": 20,
            "min_value": 10,
            "max_value": 200,
            "tags": "counters::pages",
        },
    ),
]

def add_one_line(number, suffix, cfg):
    line = [str(number) + suffix, cfg["tags"]]
    return line

result = []

for counter, counter_cfg in cfg:
    this_result = []

    # Create the numbers themselves
    if "must_include" in counter_cfg:
        this_result = this_result + [
            add_one_line(number=i, suffix=counter, cfg=counter_cfg)
            for i in range(
                counter_cfg["must_include"][0], counter_cfg["must_include"][1] + 1
            )
        ]
    if "n_random_cards" in counter_cfg:
        random_ints = sorted(
            np.random.randint(
                counter_cfg["min_value"],
                counter_cfg["max_value"],
                size=counter_cfg["n_random_cards"],
            )
        )
        this_result = this_result + [add_one_line(number=i, suffix=counter, cfg=counter_cfg) for i in random_ints]

    result = result + this_result


# print(result)

result_df = pd.DataFrame(result)
print(result_df)
result_df.to_csv("japanese-numbers.csv", index=None, header=False)

