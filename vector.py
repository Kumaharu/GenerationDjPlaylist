from sklearn import linear_model
clf = linear_model.LinearRegression()
import matplotlib.pyplot as plt

#評価式をまとめた。評価式で算出した値がベクトルの要素になる
class Vector:
    bpm_list = [120, 125, 128, 120, 125]
    bpm = {"bad": [124, "nomal"], "love me": [126, "sorry_next_skiped"], "sorry": [128, "nomal"],
           "alone": [110, "nomal"], "Faded": [100, "alone_next_skiped"], "shade": [96, "nomal"], "loop": [90, "nomal"]}



    # 再生番号を与える
    def give_number_of_play(self,bpm_list):
        i = 0
        play_number_dict = {}
        while (i < len(bpm_list) - 1):
            value = str(bpm_list[i]) + "→" + str(bpm_list[i + 1])
            i += 1
            play_number_dict.setdefault(i, value)
        return play_number_dict

    # 連続する２曲のbpmの遷移回数 例 b_i→b_i+1 120 → 123 #引数はlist型じゃないとダメ、dict型でも動くが結果が全て同じになってしまう
    def make_freq_list(self,bpm_list):
        i = 0
        bpm_transition = []
        freq_list_dict = {}

        while (i < len(bpm_list) - 1):
            key = str(bpm_list[i]) + "→" + str(bpm_list[i+1])
            if (key in freq_list_dict):
                freq_list_dict[key] = freq_list_dict[key] + 1
            else:
                freq_list_dict.setdefault(key, 1)
            #         print(key)
            #         print(dict)
            i += 1
        return (freq_list_dict)


    # rankb(r)はbpmの遷移回数が多いいものから抽出する. 戻り値は、遷移が多い曲番号リスト。曲番号play_numbers={1: '105→104', 2: '104→105', 3: '105→100'}
    def rankb(self,freq_list, play_numbers):
        rankb_i = []
        freq_list_sorted = sorted(freq_list.items(), reverse=True, key=lambda x: x[1])
        # print(freq_list_sorted)
        for r in freq_list_sorted:
            # print(r[0])
            for play_number in play_numbers:
                if (play_numbers[play_number] == r[0]):
                    rankb_i.append(play_number)
        return rankb_i

        # 評価関数f  freq(b_i,b_i+1)/sum_transition_num #𝑓(𝑖) が求められた。式（１０）　V_3r+6

    def f(self, bpm_list):
        freq_list = self.make_freq_list(bpm_list)
        freq_list_sorted = sorted(freq_list.items(), reverse=True, key=lambda x: x[1])
        sum_transition_num = len(bpm_list) - 1
        f_v = []
        i=0
        for freq in freq_list_sorted:
            if (i > 3):
                break
            i += 1
            f_v.append(freq[1] / sum_transition_num)

        return f_v

    # V_3r+7 rankb()で求めた遷移が多い曲番号を全体の遷移数で割る
    def calculate_element_v(self,bpm_list):
        freq_list = self.make_freq_list(bpm_list)
        play_number = self.give_number_of_play(bpm_list)
        rankb_list = self.rankb(freq_list, play_number)
        rankb_v = []
        i = 0
        for rankb_value in rankb_list:
            if (i > 3):
                break
            i += 1
            rankb_v.append(rankb_value / len(rankb_list))
        # print("ベクトル要素　V_3r+7: "+str(rankb_v))
        return rankb_v

    #####全体遷移のベクトル
    def make_all_transition_v4(self,func, indivisual_dict):
        result = 0
        # print("test"+str(func([[0]])))
        for key in indivisual_dict:
            result += (indivisual_dict[key] - float(func([[key]])[0])) ** 2
        return [result / 2]

    # 第一引数に単回帰式、第二引数に個体の長さ
    def make_all_transition_v1_v3(self,func, length):
        i = 0
        all_tansition_vector = []
        while (i < length):
            tmp = float(func([[i]])[0])
            all_tansition_vector.append(tmp)
            i += 3
        return all_tansition_vector

    # 全体分析のベクトルを返す
    def make_all_transition_vector(self,indivisual_dict):
        # list内list[[2],[3],[8]]を作成
        X = []
        Y = []
        all_tansition_vector = []
        for key in indivisual_dict:
            X.append([key])
            Y.append([indivisual_dict[key]])
        # 予測モデルを作成
        clf.fit(X, Y)
        v4 = self.make_all_transition_v4(clf.predict, indivisual_dict)
        v1_3 = self.make_all_transition_v1_v3(clf.predict, len(indivisual_dict))
        return v4 + v1_3
