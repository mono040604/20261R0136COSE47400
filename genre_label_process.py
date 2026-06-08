import json
import pandas as pd

df = pd.read_csv("./valid_annotations.csv")
df["genre_list"] = df["Genre"].apply(lambda x: x.strip().split("|"))

all_genres = []
for genres in df["genre_list"]:
    all_genres.extend(genres)
genres_count = pd.Series(all_genres).value_counts()
 
print(f'print the top 20 labels:{genres_count.head(20)}')

TARGET_GENRES = ["Drama","Comedy", "Romance", "Crime", "Short", "Adventure", "Mystery", "Horror", "Fantasy", "Action", "Western", "History", "War", "Thriller", "Animation","Biography","Sport",'Music', 'Family', 'Sci-Fi', 'Film-Noir','Musical','Documentary']

for genres in TARGET_GENRES:
    df[genres] = df["genre_list"].apply(lambda x:1 if genres in x else 0)
df = df[df[TARGET_GENRES].sum(axis=1) > 0].reset_index(drop=True)

labels_map = {"label2id":{genres: idx for idx, genres in enumerate(TARGET_GENRES)},
              "id2label":{idx: genres for genres, idx in enumerate(TARGET_GENRES)},
              "total_gernes": len(TARGET_GENRES)}

df.to_csv("./core_annotations.csv", index=False, encoding="utf-8")
with open("./genre_label_map.json", "w", encoding="utf-8") as f:
    json.dump(labels_map, f, indent=2, ensure_ascii=False)

print(f'useful numbers of datasets:{len(df)}') 