import json

label_map = json.load(open("./genre_label_map.json", "r"))
prompt_lib = {
    "templates":{
    "base": "a movie poster of {genre} file",
    "officical": "an official movie poster for a {genre_text} film",
    "official":"official movie poster for (genre_text) film",
    "cinematic":"cinematic movie poster, {genre_text}, high quality design"
    },
    "genre_combine_rules":{
        "1 genre":"{g1}",
        "2 genre":"{g2}",
        "3 genre":"{g3}",
        "4+ genre":"{g1},{g2},{g3} and other genres"
    },
    "genre_list":list(label_map["label2id"].keys()),
    "label_map":label_map
}
with open("./clip_prompt_base.json", "w", encoding="utf-8") as f:
    json.dump(prompt_lib, f, indent=2, ensure_ascii=False)