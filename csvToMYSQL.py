import pandas as pd
import numpy as np
import pymysql

data = pd.read_csv("perfume_mat_winter.csv")

data = data.replace({np.nan: None})
print(data)

db = pymysql.connect(host='localhost', port = 3306, user = 'root', password='epqpvmqlqjs',
                    db='perfume', charset='utf8')

cursor = db.cursor() 

# sql = 'INSERT INTO perfume(id, perfume_name, brand, brand_value, gender, launch_year, main_accord1, main_accord2, main_accord3, top_note, middle_note, base_note, season, day_or_night, longevity, sillage, rating, voters_num, main_accord1_ratio, main_accord2_ratio, main_accord3_ratio) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
# sql = 'INSERT INTO preprocessed_perfume(id, perfume_name, brand_value, main_accord1, main_accord2, main_accord3, season, longevity, rating, voters_num, main_accord1_ratio, main_accord2_ratio, main_accord3_ratio) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
sql = 'INSERT INTO perfume_mat_winter(id, beverages, brand_value, citrussmells, eternal, fall, flowers, fruitsvegetablesandnuts, greensherbsandfougeres,long_lasting, longevity, luxury, moderate, muskamberanimalicsmells, naturalandsyntheticpopularandweird, normal, popular, resinsandbalsams, season, spices, spring, summer, sweetsandgourmandsmells, very_weak, weak, whiteflowers, winter, woodsandmosses) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

for idx in range(len(data)):
    cursor.execute(sql, tuple(data.values[idx]))

db.commit()
db.close() 