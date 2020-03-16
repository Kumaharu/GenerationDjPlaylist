import vector
import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime


ref_playlist = {0: 'SKY (Edited)', 1: 'Ignite', 2: 'All Falls Down', 3: 'Stargazing(Acapella) vs All Aboard', 4: 'TJR & Reece Low - Check This', 5: 'TWIIG - Tarantella', 6: 'MARNIK & Danko - Hymn (Till My Kingdom Comes)', 7: 'Alone vs Get down (Alan Walker Mashup)', 8: 'Faded', 9: 'Faded (Tiësto Northern Lights Remix)', 10: 'Ariana Grande ft. Zedd - Break Free', 11: 'Daft Punk - Da Funk', 12: 'Popeska - Diamonds', 13: 'Zedd ft. Selena Gomez - I Want You To Know', 14: 'John Dish - Karmma', 15: 'Curbi - Shinai ', 16: 'Ariana Grande - Into You (Acappella)  ', 17: 'Zedd ft. Hayley Williams - Stay The Night (Zedd & KDrew aka Kevin Drew Extended Remix) ', 18: 'Zedd ft. Foxes - Clarity'}



#参考プレイリストのbpm遷移リスト
bpm_list = [120, 125, 128, 120, 125,127,126,120,125]


#3 辞書型オブジェクトをシャッフルできるメソッド
def shuffleDict(d):
  keys = list(d.keys())
  random.shuffle(keys)
  [(key, d[key]) for key in keys]
  random.shuffle(keys)
  [(key, d[key]) for key in keys]
  random.shuffle(keys)
  keys = [(key, d[key]) for key in keys]
  #keys = d(keys)
  return dict(keys)


#一つの個体、プレイリストを生成 （辞書型を返す）
def make_individual_playlist():
    sum_of_playlist_song = 10
    individual_playlist = {}
    i = 0
    while i < sum_of_playlist_song:
        individual_playlist.setdefault(i, random.randint(95, 100))
        i += 1
    return  individual_playlist

def extract_bpm(individual_playlist):
    for key in individual_playlist:
        bpm_list.append(individual_playlist[key])
    return bpm_list


#個体（曲数Mの楽曲集合）とりあえず50作る
def collection_of_individual_playlists():
    individual_playlist = make_individual_playlist()
    # individual_playlist = {0: 104, 1: 104, 2: 107, 3: 107, 4: 109, 5: 104, 6: 106, 7: 107, 8: 107, 9: 102, 10: 109, 11: 110, 12: 110, 13: 107, 14: 107, 15: 109, 16: 107, 17: 106, 18: 105, 19: 105, 20: 105, 21: 108, 22: 102, 23: 103, 24: 107, 25: 106, 26: 110, 27: 101, 28: 101, 29: 100, 30: 103, 31: 104, 32: 110, 33: 102, 34: 104, 35: 110, 36: 109, 37: 101, 38: 101, 39: 102, 40: 108, 41: 110, 42: 104, 43: 101, 44: 109, 45: 107, 46: 107, 47: 100, 48: 108, 49: 101, 50: 109, 51: 102, 52: 106, 53: 106, 54: 110, 55: 105, 56: 105, 57: 101, 58: 109, 59: 109, 60: 102, 61: 102, 62: 100, 63: 103, 64: 103, 65: 103, 66: 101, 67: 110, 68: 102, 69: 110, 70: 110, 71: 100, 72: 110, 73: 110, 74: 104, 75: 102, 76: 102, 77: 108, 78: 107, 79: 104, 80: 105, 81: 108, 82: 109, 83: 102, 84: 110, 85: 107, 86: 105, 87: 108, 88: 105, 89: 102, 90: 101, 91: 107, 92: 104, 93: 101, 94: 105, 95: 104, 96: 103, 97: 104, 98: 104, 99: 109}
    # individual_playlist = {0: 105, 1: 103, 2: 105, 3: 105, 4: 104, 5: 104, 6: 104, 7: 104, 8: 105, 9: 101}
    # individual_playlist = {0: 104, 1: 104, 2: 107, 3: 107, 4: 109, 5: 104, 6: 106, 7: 107, 8: 107, 9: 102, 10: 109, 11: 110, 12: 110, 13: 107, 14: 107, 15: 109, 16: 107, 17: 106, 18: 105, 19: 105, 20: 105, 21: 108, 22: 102, 23: 103, 24: 107, 25: 106, 26: 110, 27: 101, 28: 101, 29: 100, 30: 103, 31: 104, 32: 110, 33: 102, 34: 104, 35: 110, 36: 109, 37: 101, 38: 101, 39: 102, 40: 108, 41: 110, 42: 104, 43: 101, 44: 109, 45: 107, 46: 107, 47: 100, 48: 108, 49: 101, 50: 109}
    # individual_playlist = {0: 130, 1: 90, 2: 110, 3: 100, 4: 128, 5: 138, 6: 138, 7: 100, 8: 90, 9: 125, 10: 130, 11: 111, 12: 111, 13: 130, 14: 128, 15: 128, 16: 108, 17: 128, 18: 128}


    i = 0
    individual_playlists = []
    while i < 100:
        individual_playlists.append(shuffleDict(individual_playlist))
        i += 1
    return individual_playlists

collection_of_individual_playlists()

extract_bpm(make_individual_playlist())
#インスタン作成
vector_instance = vector.Vector()



#f(i)を実行　2つの曲のbpm遷移回数を全曲遷移割った値をリストとして返す
# vector_list_f = vector_instance.f(bpm_list)

#V_3+7 ranckb/N
# vector_list_ranckb = vector_instance.calculate_element_v(bpm_list)

# reference_playlist_vector = vector_list_f+vector_list_ranckb
# print("reference_playlist_vector: "+str(reference_playlist_vector))
# print("reference_playlist_vector: "+str(vector_list_f))



#--------------遺伝的アルゴリズムを作成------------------

#プレイリストからBPMを取り出す関数
def extract_bpm(play_list):
    bpm_list = []
    for song_number in play_list:
        bpm_list.append(play_list[song_number])
    return bpm_list

#プレイリストから曲番号を取り出す関数
def extract_number_song(play_list):
    song_number_list = []
    for song_number in play_list:
        song_number_list.append(song_number)
    return song_number_list

def fitness(reference_playlist,individual_playlist_bpm):
    i = 0
    eval_sum = 0
    while(i<len(reference_playlist)):
        eval_sum += (reference_playlist[i]-individual_playlist_bpm[i])**2
        i += 1
    return eval_sum
#評価式
# def fitness(reference_playlist,individual_playlist_bpm):
#     individual_playlist_bpm_vector = []
#     reference_playlist_bpm_vector = []
#     # for song_number in individual_playlist:
#     #     individual_playlist_bpm_vector.append(individual_playlist[song_number])
#     for bpm in individual_playlist_bpm:
#         individual_playlist_bpm_vector.append(bpm)
#     # for song_number2 in reference_playlist:
#     #     reference_playlist_bpm_vector.append(reference_playlist[song_number2])
#     for bpm2 in reference_playlist:
#         reference_playlist_bpm_vector.append(bpm2)
#     a = np.array(reference_playlist_bpm_vector)
#     b = np.array(individual_playlist_bpm_vector)
#
#     a_b_inner_product = np.dot(a, b) #内積
#     size_a = np.linalg.norm(a) #ベクトルのサイズ
#     size_b = np.linalg.norm(b)
#
#     fitness_value = a_b_inner_product/(size_a*size_b) #適応度
#     return fitness_value

def evaluate(fitness_value_list):
    fitness_value_list.sort()
    # print("evaluateのリターン"+str(fitness_value_list))
    return fitness_value_list

#交叉
def two_point_crossover(parent1, parent2):
    cross_point = int(len(parent1)/2)
    child = {}
    parent1_song_number = extract_number_song(parent1)
    parent2_song_number = extract_number_song(parent2)
    parent2_gene = []
    parent1_gene = parent1_song_number[0:cross_point]
    for tmp in parent2_song_number:
        if(tmp in parent1_gene):
            parent2_gene.append(tmp)
    parent1_song_number[0:cross_point] =  parent2_gene
    #プレイリスト復元
    for song_number in parent1_song_number:
        child[song_number] = parent1[song_number]
    # print("交叉 child:  "+str(child))
    return child


#突然変異 引数：dict return dict
def mutate(parent):
    mutate_child = shuffleDict(parent)
    # print("突然変異 "+str(mutate_child))
    return mutate_child

def main():
    # REFERENCE_PLAYLIST = make_individual_playlist()
    # population = [(fitness(vector_instance.f(extract_bpm(REFERENCE_PLAYLIST)),vector_instance.f(extract_bpm(individual_playlist))), individual_playlist) for individual_playlist in collection_of_individual_playlists()]
    population = []
    reference_playlist_vector = vector_instance.f( extract_bpm(REFERENCE_PLAYLIST)) + vector_instance.calculate_element_v(extract_bpm(REFERENCE_PLAYLIST)) + vector_instance.make_all_transition_vector(REFERENCE_PLAYLIST)
    print("参考プレイリストのベクトル " +str(reference_playlist_vector))
    for individual_playlist in collection_of_individual_playlists():
        # reference_playlist_vector = vector_instance.f(extract_bpm(REFERENCE_PLAYLIST)) + vector_instance.calculate_element_v(extract_bpm(REFERENCE_PLAYLIST))
        # individual_playlist_vector = vector_instance.f(extract_bpm(individual_playlist)) + vector_instance.calculate_element_v(extract_bpm(individual_playlist))
        # reference_playlist_vector = vector_instance.f(extract_bpm(REFERENCE_PLAYLIST))+vector_instance.calculate_element_v(extract_bpm(REFERENCE_PLAYLIST))+vector_instance.make_all_transition_vector(REFERENCE_PLAYLIST)
        individual_playlist_vector = vector_instance.f(extract_bpm(individual_playlist))+vector_instance.calculate_element_v(extract_bpm(individual_playlist))+vector_instance.make_all_transition_vector(individual_playlist)
        # reference_playlist_vector=vector_instance.make_all_transition_vector(REFERENCE_PLAYLIST)
        # individual_playlist_vector=vector_instance.make_all_transition_vector(individual_playlist)
        print("個体プレイリストのベクトル " + str(individual_playlist_vector))
        population.append((fitness(extract_bpm(REFERENCE_PLAYLIST),extract_bpm(individual_playlist)),individual_playlist))



    evaluate_population = evaluate(population)
    print('--------------------------')
    print("参考プレイリスト" + str(REFERENCE_PLAYLIST))

    print('Generation: 0')
    print('Min : {}'.format(evaluate_population[-1][0]))
    print('Max : {}'.format(evaluate_population[0][0]))
    print('--------------------------')

    for g in range(generation):
        print('Generation: ' + str(g + 1))
        # エリートを選択
        eva = evaluate(population)
        elites = eva[:int(len(population) * elite_rate)] #sliceしている　上位何割をエリートとして取得

        # 突然変異、交叉
        population = elites
        while len(population) < sum_individual_length:
            # m1 = random.randint(0, len(elites) - 1)  # リストのインデックスを作っているのでlength-1の値
            # m2 = random.randint(0, len(elites) - 1)
            # child = two_point_crossover(elites[m1][1], elites[m2][1])
            if random.random() < mutate_rate:
                m = random.randint(0, len(elites) - 1)
                child = mutate(elites[m][1])
            else:
                m1 = random.randint(0, len(elites) - 1) #リストのインデックスを作っているのでlength-1の値
                m2 = random.randint(0, len(elites) - 1)
                child = two_point_crossover(elites[m1][1], elites[m2][1])
            population.append((fitness(extract_bpm(REFERENCE_PLAYLIST),extract_bpm(child)), child))

        # 評価
        eva = evaluate(population)
        population = eva

        print('Min : {}'.format(population[-1][0]))
        print('Max : {}'.format(population[0][0]))
        # print('--------------------------')
    print('Result : {}'.format(population[0]))
    print(population)

    keys = list(population[0][1].keys())
    key1 = []
    # for key in keys:
    #     if(key%5 == 0):
    #         key1.append(key)
    values = [population[0][1][key] for key in keys]
    print(keys)
    #参考プレリストのデータ

    key2 = []
    keys2 = list(REFERENCE_PLAYLIST.keys())
    # for key in keys2:
    #     if(key%5 == 0):
    #         key2.append(key)
    values_ref = [REFERENCE_PLAYLIST[key] for key in keys2]
    plt.xlabel("song_number")
    plt.ylabel("BPM")
    plt.scatter(keys2, values, label="Generated playlist")
    plt.scatter(keys2, values_ref, label="Reference playlist created by dj")
    plt.plot(keys2, values)
    plt.plot(keys2, values_ref, linewidth=4, color="orange", linestyle="dotted")
    plt.legend()
    plt.savefig(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
+'.png')
    plt.show()


    # #評価値の分布を可視化する
    # evaluate_histgram_data = []
    # for person in population:
    #     evaluate_histgram_data.append(person[0])
    # plt.hist(evaluate_histgram_data,bins=100)
    # plt.savefig(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+'.png')
    # plt.show()
    # print(population)
if __name__ == '__main__':
    # 定数定義
    #個体長100
    # REFERENCE_PLAYLIST = {0: 104, 1: 104, 2: 107, 3: 107, 4: 109, 5: 104, 6: 106, 7: 107, 8: 107, 9: 102, 10: 109, 11: 110, 12: 110, 13: 107, 14: 107, 15: 109, 16: 107, 17: 106, 18: 105, 19: 105, 20: 105, 21: 108, 22: 102, 23: 103, 24: 107, 25: 106, 26: 110, 27: 101, 28: 101, 29: 100, 30: 103, 31: 104, 32: 110, 33: 102, 34: 104, 35: 110, 36: 109, 37: 101, 38: 101, 39: 102, 40: 108, 41: 110, 42: 104, 43: 101, 44: 109, 45: 107, 46: 107, 47: 100, 48: 108, 49: 101, 50: 109, 51: 102, 52: 106, 53: 106, 54: 110, 55: 105, 56: 105, 57: 101, 58: 109, 59: 109, 60: 102, 61: 102, 62: 100, 63: 103, 64: 103, 65: 103, 66: 101, 67: 110, 68: 102, 69: 110, 70: 110, 71: 100, 72: 110, 73: 110, 74: 104, 75: 102, 76: 102, 77: 108, 78: 107, 79: 104, 80: 105, 81: 108, 82: 109, 83: 102, 84: 110, 85: 107, 86: 105, 87: 108, 88: 105, 89: 102, 90: 101, 91: 107, 92: 104, 93: 101, 94: 105, 95: 104, 96: 103, 97: 104, 98: 104, 99: 109}
    #個体長50
    # REFERENCE_PLAYLIST = {0: 104, 1: 104, 2: 107, 3: 107, 4: 109, 5: 104, 6: 106, 7: 107, 8: 107, 9: 102, 10: 109,11: 110, 12: 110, 13: 107, 14: 107, 15: 109, 16: 107, 17: 106, 18: 105, 19: 105, 20: 105,21: 108, 22: 102, 23: 103, 24: 107, 25: 106, 26: 110, 27: 101, 28: 101, 29: 100, 30: 103,31: 104, 32: 110, 33: 102, 34: 104, 35: 110, 36: 109, 37: 101, 38: 101, 39: 102, 40: 108,41: 110, 42: 104, 43: 101, 44: 109, 45: 107, 46: 107, 47: 100, 48: 108, 49: 101, 50: 109}
    #個体長12
    REFERENCE_PLAYLIST = {0: 105, 1: 103, 2: 105, 3: 105, 4: 104, 5: 104, 6: 104, 7: 104, 8: 105, 9: 101}
    # REFERENCE_PLAYLIST = {0: 103, 1: 102, 2: 103, 3: 104, 4: 100, 5: 103, 6: 100, 7: 102, 8: 103, 9: 100, 10: 105, 11: 105, 12: 100, 13: 100, 14: 103, 15: 105, 16: 103, 17: 104, 18: 102, 19: 105, 20: 103, 21: 101, 22: 104, 23: 105, 24: 100, 25: 102, 26: 100, 27: 102, 28: 101, 29: 105, 30: 103, 31: 102, 32: 105, 33: 102, 34: 100, 35: 103, 36: 100, 37: 100, 38: 102, 39: 101, 40: 104, 41: 104, 42: 103, 43: 101, 44: 102, 45: 105, 46: 104, 47: 100, 48: 100, 49: 103}
    # REFERENCE_PLAYLIST = {0: 130, 1: 90, 2: 110, 3: 100, 4: 128, 5: 138, 6: 138, 7: 100, 8: 90, 9: 125, 10: 130, 11: 111, 12: 111, 13: 130, 14: 128, 15: 128, 16: 108, 17: 128, 18: 128}
    # gene_length = 10  # 遺伝子長
    # sum_individual_length = len(REFERENCE_PLAYLIST) # 個体数
    sum_individual_length = 100
    generation = 2000  # 世代数
    mutate_rate = 0.3  # 突然変異の確率
    elite_rate = 0.4  # エリート選択の割合

    main()