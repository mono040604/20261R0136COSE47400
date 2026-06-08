import os
from PIL import Image
from tqdm import tqdm
import pandas as pd

SRC_IMG_FOLDER = "./raw_data./MoviePosters/"
DST_IMG_FOLDER = "./processed_posters"

os.makedirs(DST_IMG_FOLDER, exist_ok=True)
df = pd.read_csv("./core_annotations.csv")
img_filename = df["img_filename"].tolist()

fail_list = []
for img_name in tqdm(img_filename, desc="standardizing poster images"):
    src_path = os.path.join(SRC_IMG_FOLDER, img_name)
    dst_path = os.path.join(DST_IMG_FOLDER, img_name)

    try:
        img = Image.open(src_path).convert("RGB")
        img = img.resize((224, 224), Image.Resampling.BILINEAR)
        img.save(dst_path, "JPEG", quality = 95)
    except Exception as e:
        fail_list.append(img_name)
        print(f"processing failed: {img_name}, Error reason:{e}")
with open("./process_failed_img.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(fail_list))

print(f"图片标准化完成！")
print(f"成功处理：{len(img_filename) - len(fail_list)} 张海报")
print(f"处理失败：{len(fail_list)} 张，已记录在 process_failed_imgs.txt")
print(f"处理后的海报保存在：{DST_IMG_FOLDER} 文件夹")