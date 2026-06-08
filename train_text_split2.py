from iterstrat.ml_stratifiers import MultilabelStratifiedShuffleSplit
import pandas as pd
import json

INPUT_CSV = "./core_annotations.csv"
LABEL_MAP = "./genre_label_map.json"
TEST_SIZE = 0.2
RANDOM_STATE = 42

df = pd.read_csv(INPUT_CSV)
label_map = json.load(open(LABEL_MAP, "r", encoding="utf-8"))
TARGET_GERNES = list(label_map["label2id"].keys())

y = df[TARGET_GERNES].values
x = df.index.values

msss = MultilabelStratifiedShuffleSplit(
    n_splits=1,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE
)
train_idx, test_idx = next(msss.split(x, y))
train_df = df.iloc[train_idx].reset_index(drop=True)
test_df = df.iloc[test_idx].reset_index(drop=True)

keep_cols = ["img_filename", "imdbId", "Title", "Genre"] + TARGET_GERNES
train_df[keep_cols].to_csv("./train_annotations2.csv", index=False, encoding="utf-8")
test_df[keep_cols].to_csv("./test_annotations2.csv", index=False, encoding="utf-8")

print(f'total sample = {len(df)}')
print(f'training_set = {len(train_df)}')
print(f'testing_set = {len(test_df)}')

stats = []
for genre in TARGET_GERNES:
    total_pos = df[genre].sum()
    train_pos = train_df[genre].sum()
    test_pos = test_df[genre].sum()
    stats.append({
        "genre":genre,
        "total_pos":total_pos,
        "train_pos":train_pos,
        "test_pos":test_pos
    })
stats_df = pd.DataFrame(stats).sort_values("total_pos", ascending=False)
print(stats_df.to_string(index=False))