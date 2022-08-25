import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

perfume = pd.read_csv('preprocessed_sample_data.csv')

perfume_name = "sample_taste1"
main_accord1 = "SPICES"
main_accord2 = "GREENSHERBSANDFOUGERES"
main_accord3 = "CITRUSSMELLS"
season = "spring"
longevity = "moderate"
sillage = "intimate"
rating = None
voters_num = None
main_accord1_ratio = 0.39
main_accord2_ratio = 0.33
main_accord3_ratio = 0.28

# 메인어코드 영향력 같은 자리 기준 0.6 <= 최대값 

#지속성
# 2.5 eternal
# 2 long_lasting
# 1.5 moderate
# 1 weak
# 0.5 very_weak

# 확산성 
# 1.98 enormous
# 1.485 strong
# 0.99 medium
# 0.495 intimate

# 시즌 
# 0.46

data_to_insert = {'perfume_name' : perfume_name, 'main_accord1': main_accord1, 'main_accord2' : main_accord2, 'main_accord3' : main_accord3, "season" : season,
"longevity" : longevity, "sillage" : sillage, "rating" : rating, "voters_num" : voters_num, "main_accord1_ratio" : main_accord1_ratio, 
"main_accord2_ratio" : main_accord2_ratio, "main_accord3_ratio" : main_accord3_ratio}

# print(type(perfume.iloc[0:1, :]))
# print(type(perfume))

perfume = perfume.append(data_to_insert, ignore_index=True)
perfume_features = perfume.iloc[:, 1:7]
print(perfume_features)

cnt = perfume['perfume_name'].count()
all = []

all.append("longevity")
all.append("sillage")
all.append("season")

print(perfume_features.values[0])

for i in range(0, cnt): 
    temp = " ".join(perfume_features.values[i])
    all.append(temp)

print(all[30], "+++++")

count_vector = CountVectorizer(min_df=1, ngram_range=(1,1))
perfume_mat = count_vector.fit_transform(all)
print(count_vector.vocabulary_)

# print(type(count_vector.vocabulary_))
# print(perfume_mat.shape)
# print(type(perfume_mat.toarray()))
# print(perfume_mat)

#csr_matrix(perfume_mat)
# 12 + 4 + 5 + 4 + 3 = 28개

# all에 append한 longevity, sillage, season 또한 매트릭스로 생성되기 때문에 해당 부분 제거
perfume_mat = np.delete(perfume_mat.toarray(), (0,1,2), axis = 0)
print(perfume_mat, "---")
perfume_mat = csr_matrix(perfume_mat)
print(perfume_mat, "=====")

reverse_vocabulary = dict(map(reversed, count_vector.vocabulary_.items()))

# print(reverse_vocabulary)
# print(reverse_vocabulary[22])
# print(perfumes.values[0][0])

perfume_mat = perfume_mat.toarray().astype(np.float64)
print(len(perfume_mat))
print(perfume_mat[0].size)
for i in range(0, len(perfume_mat)):
    for j in range(0, perfume_mat[0].size):
        if perfume_mat[i][j] == 1:
            if j == 0: #beverage
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
            
            elif j == 1: #citrus smells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue

            elif j == 2: #enormous
                perfume_mat[i][j] = 0
                perfume_mat[i][17] = 2 #17 = 시아주
                continue
                   
            elif j == 3: #eternal
                perfume_mat[i][j] = 0
                perfume_mat[i][10] = 2.5 #10 = longevity
                continue
                   
            elif j == 4: #fall
                perfume_mat[i][j] = 0
                if season == 'fall':
                    perfume_mat[i][16] = 0.05 # 16 = season
                continue
                  
            elif j == 5: #flowers
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue

            elif j == 6: #fruitsvegetablesandnuts
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue

            elif j == 7: #greensherbsandfougeres
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                    
            elif j == 8:  #intimate
                perfume_mat[i][j] = 0
                perfume_mat[i][17] = 0.5 #17 = 시아주
                continue
                  
            elif j == 9: #long_lasting
                perfume_mat[i][j] = 0
                perfume_mat[i][10] = 2 #10 = longevity
                continue
                
            elif j == 11: #medium
                perfume_mat[i][j] = 0
                perfume_mat[i][17] = 1 #17 = 시아주
                continue
                    
            elif j == 12: #moderate
                perfume_mat[i][j] = 0
                perfume_mat[i][10] = 1.5 #10 = longevity
                continue
                  
            elif j == 13: #muskamberanimalicsmells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                   
            elif j == 14: #naturalandsyntheticpopularandweird
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                  
            elif j == 15: #resinsandbalsams
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                   
            elif j == 18: #spices
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                   
            elif j == 19: #spring
                perfume_mat[i][j] = 0
                if season == 'spring':
                    perfume_mat[i][16] = 0.05 # 16 = season
                continue
                 
            elif j == 20: #strong
                perfume_mat[i][j] = 0
                perfume_mat[i][17] = 1.5 #17 = 시아주
                continue
                   
            elif j == 21: #summer
                perfume_mat[i][j] = 0
                if season == 'summer':
                    perfume_mat[i][16] = 0.05 # 16 = season
                continue
               
            elif j == 22: #sweetsandgourmandsmells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                   
            elif j == 23: #very_weak
                perfume_mat[i][j] = 0
                perfume_mat[i][10] = 0.5 #10 = longevity
                continue
                  
            elif j == 24: #weak
                perfume_mat[i][j] = 0
                perfume_mat[i][10] = 1 #10 = longevity
                continue
                  
            elif j == 25: #whiteflowers
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                     
            elif j == 26: #winter
                perfume_mat[i][j] = 0
                if season == 'winter':
                    perfume_mat[i][16] = 0.05 # 16 = season
                continue
                  
            elif j == 27: #woodsandmosses
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                elif perfume.values[i][2].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][10]
                elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][11]
                continue
                  
        elif perfume_mat[i][j] == 2: # 메인 어코드가 2개 겹칠 경우
            if j == 0: #beverage
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    temp[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                    
            elif j == 1: #citrus smells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue

            # elif j == 2: #enormous
            #     temp[i][j] = 1 
                   
            # elif j == 3: #eternal
            #     temp[i][j] = 1 
                  
            # elif j == 4: #fall
            #     temp[i][j] = 0.25 
                     
            elif j == 5: #flowers
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                    
            elif j == 6: #fruitsvegetablesandnuts
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue

            elif j == 7: #greensherbsandfougeres
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                    
            # elif j == 8:  #intimate
            #     temp[i][j] = 0.25
                  
            # elif j == 9: #long_lasting
            #     temp[i][j] = 0.8 
                
            # elif j == 11: #medium
            #     temp[i][j] = 0.5 
                    
            # elif j == 12: #moderate
            #     temp[i][j] = 0.6 
                  
            elif j == 13: #muskamberanimalicsmells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            elif j == 14: #naturalandsyntheticpopularandweird
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                  
            elif j == 15: #resinsandbalsams
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            elif j == 18: #spices
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            # elif j == 19: #spring
            #     temp[i][j] = 0.25 
                 
            # elif j == 20: #strong
            #     temp[i][j] = 0.75 
                   
            # elif j == 21: #summer
            #     temp[i][j] = 0.25 
               
            elif j == 22: #sweetsandgourmandsmells
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            # elif j == 23: #very_weak
            #     temp[i][j] = 0.2 
                  
            # elif j == 24: #weak
            #     temp[i][j] = 0.4 
                  
            elif j == 25: #whiteflowers
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
                     
            # elif j == 26: #winter
            #     temp[i][j] = 0.25 
                  
            elif j == 27: #woodsandmosses
                if perfume.values[i][1].lower() == reverse_vocabulary[j]:
                    perfume_mat[i][j] = perfume.values[i][9]
                    if perfume.values[i][2].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][10]
                    elif perfume.values[i][3].lower() == reverse_vocabulary[j]:
                        perfume_mat[i][j] += perfume.values[i][11]
                else:
                    perfume_mat[i][j] = perfume.values[i][10] + perfume.values[i][11]
                continue
 
        elif perfume_mat[i][j] == 3: #메인 어코드 카테고리가 3개 다 같을 경우
            if j == 0: #beverage
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                
            elif j == 1: #citrus smells
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                
            # elif j == 2: #enormous
            #     temp[i][j] = 1 
                   
            # elif j == 3: #eternal
            #     temp[i][j] = 1 
                  
            # elif j == 4: #fall
            #     temp[i][j] = 0.25 
                    
            elif j == 5: #flowers
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue  

            elif j == 6: #fruitsvegetablesandnuts
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            elif j == 7: #greensherbsandfougeres
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
             
            # elif j == 8: #intimate
            #     temp[i][j] = 0.25 
                  
            # elif j == 9: #long_lasting
            #     temp[i][j] = 0.8 
                
            # elif j == 11: #medium
            #     temp[i][j] = 0.5 
                    
            # elif j == 12: #moderate
            #     temp[i][j] = 0.6 
                  
            elif j == 13: #muskamberanimalicsmells
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue

            elif j == 14: #naturalandsyntheticpopularandweird
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            elif j == 15: #resinsandbalsams
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
               
            elif j == 18: #spices
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                   
            # elif j == 19: #spring
            #     temp[i][j] = 0.25 
                 
            # elif j == 20: #strong
            #     temp[i][j] = 0.75 
                   
            # elif j == 21: #summer
            #     temp[i][j] = 0.25 
               
            elif j == 22: #sweetsandgourmandsmells
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                    
            # elif j == 23: #very_weak
            #     temp[i][j] = 0.2 
                  
            # elif j == 24: #weak
            #     temp[i][j] = 0.4 
                  
            elif j == 25: #whiteflowers
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue
                    
            # elif j == 26: #winter
            #     temp[i][j] = 0.25 
                  
            elif j == 27: #woodsandmosses
                perfume_mat[i][j] = perfume.values[i][9] + perfume.values[i][10] + perfume.values[i][11]
                continue

print(perfume_mat[0])
print(perfume_mat[1])

# perfume_mat를 데이터베이스 저장하기 위한 코드 ndarray => dataframe
perfume_mat_DataFrame = pd.DataFrame(perfume_mat, columns=['beverages', 'citrussmells', 'enormous', 'eternal', 'fall', 'flowers', 'fruitsvegetablesandnuts', 'greensherbsandfougeres',
'intimate', 'long_lasting', 'longevity', 'medium', 'moderate', 'muskamberanimalicsmells', 'naturalandsyntheticpopularandweird', 'resinsandbalsams', 'season', 'sillage', 'spices', 'spring', 
'strong', 'summer', 'sweetsandgourmandsmells', 'very_weak', 'weak', 'whiteflowers', 'winter', 'woodsandmosses'])
perfume_mat_DataFrame.to_csv("perfume_mat.csv")

# perfume_sim = cosine_similarity(perfume_mat, perfume_mat)
perfume_sim = cosine_similarity(perfume_mat, perfume_mat)
print(type(perfume_sim))
print(perfume_sim[0])

perfume_sim_sorted_idx = perfume_sim.argsort()[: , ::-1]
print(perfume_sim_sorted_idx[0])

# 가상의 input 데이터를 빼주는 과정
perfume = perfume[:-1]
print(perfume)

# 가중 평점(Weighted Rating) = (v/(v+m)) * R + (m/(v+m)) * C
C = perfume['rating'].mean()
m = perfume['voters_num'].quantile(0.6)
print(round(C, 3), round(m, 3))

def set_weighted_rating(row):
    v = row['voters_num']
    R = row['rating']

    return ((v/(v+m)) * R + (m/(v+m)) * C)

perfume['weighted_rating'] = perfume.apply(set_weighted_rating, axis=1)
# input data를 perfumes에 다시 넣기
perfume = perfume.append(data_to_insert, ignore_index=True)

def find_sim_perfume(df, sorted_idx, target_perfume, limit):
    target = df[df['perfume_name'] == target_perfume]
    target_idx = target.index.values

    similar_idxs = sorted_idx[target_idx, :(limit)]
    similar_idxs = similar_idxs.reshape(-1)
    similar_idxs = similar_idxs[similar_idxs != target_idx]
    print(similar_idxs)
    print(type(similar_idxs))

    print(similar_idxs[0], "+++++++++++++++++")
    idx_top = similar_idxs[0:33]
    idx_middle = similar_idxs[33:66]
    idx_bottom = similar_idxs[66:99]

    print(idx_top.size)
    print(idx_middle.size)
    print(idx_bottom.size)

    print(random.choice(idx_top))
    print(random.choice(idx_middle))
    print(random.choice(idx_bottom))

    # return df.iloc[similar_idxs].sort_values("weighted_rating", ascending = False)[:limit] #유사도 순 정렬 후, 가중 평점 적용하여 재정렬
    return df.iloc[similar_idxs][:limit] #유사도 순 정렬
    
similar_perfumes = find_sim_perfume(perfume, perfume_sim_sorted_idx, 'sample_taste1', 100)
print(similar_perfumes)
print(type(similar_perfumes))
similar_perfumes.to_csv("temp.csv")