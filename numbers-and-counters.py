import pandas as pd
import numpy as np

np.random.seed(20250424)

# For furigana and readings, pykakasi doesn't work well. I might have to implement something myself.
# 'kanjize' might work for the >10 part of the numbers

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

# Add some dates and times
# TODO: Randomize this
dates = [
    "7月1日", 
    "8月2日", 
    "9月3日", 
    "10月4日", 
    "11月5日", 
    "12月6日", 
    "1月7日", 
    "2月8日", 
    "3月9日", 
    "4月10日", 
    "5月11日", 
    "6月12日", 
    "7月13日", 
    "8月14日", 
    "9月15日", 
    "10月16日", 
    "11月17日", 
    "12月18日", 
    "1月19日", 
    "2月20日", 
    "3月21日", 
    "4月22日", 
    "5月23日", 
    "6月24日", 
    "7月25日", 
    "8月26日", 
    "9月27日", 
    "10月28日", 
    "11月29日", 
    "12月30日", 
    "1月31日", 
]
dates = [[x, "numbers::month_days"] for x in dates]
result = result + dates

times = [
    "午前1時5分",
    "午後2時10分",
    "午前3時15分",
    "午後4時20分",
    "午前5時25分",
    "午後6時30分",
    "午前7時35分",
    "午後8時40分",
    "午前9時45分",
    "午後10時50分",
    "午前11時55分",
    "午後12時半",

    "午後4時51分",
    "午前5時42分",
    "午後6時33分",
    "午前7時24分",
    "午後8時16分",
    "午前9時57分",
    "午後10時48分",
    "午前11時39分",
]
times = [[x, "numbers::times"] for x in times]
result = result + times


# print(result)

result_df = pd.DataFrame(result)
print(result_df)
result_df.to_csv("japanese-numbers.csv", index=None, header=False)

