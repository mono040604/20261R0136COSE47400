import pandas as pd
import json
import random

TRAIN_CSV = "./train_annotations2.csv"
LABEL_MAP = "./genre_label_map.json"
TEST_CSV = "./test_annotations.csv"
SEED = 42

with open(LABEL_MAP, 'r', encoding='utf-8') as f:
    label_map = json.load(f)
all_genres = list(label_map['label2id'].keys())
print(f'total genres:{len(all_genres)}')

random.seed(SEED)
random.shuffle(all_genres)
split_index = int(len(all_genres) * 0.7)

train_genres = all_genres[:split_index]
retained_genres = all_genres[split_index:]
print(f'train genrens({len(train_genres)}):{train_genres}')
print(f'retained genres({len(retained_genres)}):{retained_genres}')

split_result = {
    'train_genres':train_genres,
    'retained_genres':retained_genres,
    'total_genres':len(all_genres),
    'split_ratio':'7:3'
}
with open('genre_split.json', 'w', encoding='utf-8') as f:
    json.dump(split_result, f, indent=2, ensure_ascii=False)

train_df = pd.read_csv(TRAIN_CSV)
memory_train_df = train_df.copy()

for genre in retained_genres:
    memory_train_df[genre] = 0
memory_train_df.to_csv('train_annotations_memory.csv', index=False)
print('set memory_set as train_annotations_memory.csv')