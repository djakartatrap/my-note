import pandas as pd

resume = pd.read_csv("officialSource/qss-master/CAUSALITY/resume.csv")
# 行数と列数を確認
resume.shape

resume.head(10)

resume.groupby("firstname", as_index=True).count()["sex"]

crossTable = pd.crosstab(index=resume["race"], columns=resume["call"], margins=True)

# 人種ごとの審査通過率
crossTable[1] / crossTable["All"]

# クロス集計表を作らずに、審査通過率を出す
resume.loc[resume["race"] == "black", "call"].mean()

# 黒人女性フラグカラムを作成
resume.loc[:, "blackFrmale"] = resume.apply(lambda x: x["race"] == "black" and x["sex"] == "female", axis=1)

pd.crosstab(index=resume["race"], columns=[resume["sex"], resume["blackFrmale"]]).to_csv("sample.csv")

# 性別 x 人種 のカラム、type を作成
def detectSexRace(x):
    """
    :param x: pandas.Series
    :return:
    """
    if x["sex"] == "male" and x["race"] == "black":
        return "BlackMale"
    elif x["sex"] == "male" and x["race"] == "white":
        return "WhiteMale"
    elif x["sex"] == "female" and x["race"] == "black":
        return "BlackFemale"
    elif x["sex"] == "female" and x["race"] == "white":
        return "WhiteFemale"

# type別の審査通過率
resume.loc[:, "type"] = resume.apply(detectSexRace, axis=1)
resume.groupby(by="type", as_index=False).mean()[["type", "call"]]

# firstnameの審査通過率
resume.groupby(by="firstname", as_index=False).mean()[["firstname", "call"]].sort_values(by="call")


###
# 2.4.2 社会的プレッシャーと投票率
###

social_df = pd.read_csv("officialSource/qss-master/CAUSALITY/social.csv")

social_df.describe()
social_df.sex.value_counts()
social_df.messages.value_counts()

means_col = social_df.groupby(['messages']).mean()['primary2006']
means_col[means_col.index != 'Control'] - means_col['Control']

# 2006のトリートメンによって、メッセージ別の投票率に変化が見られる。

# 同時に、RCTがうまくいっているかを確認
# → メッセージ別のその他の変数(年齢、2004年投票率、家族構成)に大きな差がないかを確認
# 年齢カラムを作成
social_df['age'] = 2018 - social_df.yearofbirth
social_df.groupby('messages').mean()[['age', 'primary2004', 'hhsize']]


###
# 2.5.1 最低賃金と失業率
###

minwage_df = pd.read_csv("officialSource/qss-master/CAUSALITY/minwage.csv")
minwage_df.describe()
minwage_df.chain.value_counts()
minwage_df.location.value_counts()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)

ax = sns.distplot(minwage_df["wageBefore"], label="wageBefore")
sns.distplot(minwage_df["wageAfter"], label="wageAfter")
plt.legend()
plt.show()

ax = sns.distplot(minwage_df["fullBefore"], label="fullBefore")
sns.distplot(minwage_df["fullAfter"], label="fullAfter")
plt.legend()
plt.show()

ax = sns.distplot(minwage_df["partBefore"], label="partBefore")
sns.distplot(minwage_df["partAfter"], label="partAfter")
plt.legend()
plt.show()

# 条例施行前後で、最低賃金以下の店舗の割合
minwage_df_PA = minwage_df[minwage_df["location"] == "PA"]

# 法施行前のNJの最低賃金以下の割合
(minwage_df[minwage_df["location"] != "PA"]["wageBefore"] < 5.05).mean()
# 法施行後のNJの最低賃金以下の割合
(minwage_df[minwage_df["location"] != "PA"]["wageAfter"] < 5.05).mean()

# 法施行前のPAの最低賃金以下の割合
(minwage_df[minwage_df["location"] == "PA"]["wageBefore"] < 5.05).mean()
# 法施行後のPAの最低賃金以下の割合
(minwage_df[minwage_df["location"] == "PA"]["wageAfter"] < 5.05).mean()

# 最低賃金が上がると、常勤労働者が減る(コスト削減のため)という予測の元、常勤労働者割合を算出
fullPropAfter_NJ = minwage_df[minwage_df["location"] != "PA"]["fullAfter"].sum() / (minwage_df[minwage_df["location"] != "PA"]["fullAfter"].sum() + minwage_df[minwage_df["location"] != "PA"]["partAfter"].sum())
fullPropAfter_PA = minwage_df[minwage_df["location"] == "PA"]["fullAfter"].sum() / (minwage_df[minwage_df["location"] == "PA"]["fullAfter"].sum() + minwage_df[minwage_df["location"] == "PA"]["partAfter"].sum())

fullPropAfter_NJ - fullPropAfter_PA

# 上の式が正しいと思うんだけど、本では以下のようにやってる
fullPropAfter_NJ = (minwage_df[minwage_df["location"] != "PA"]["fullAfter"] / (minwage_df[minwage_df["location"] != "PA"]["fullAfter"] + minwage_df[minwage_df["location"] != "PA"]["partAfter"])).mean()
fullPropAfter_PA = (minwage_df[minwage_df["location"] == "PA"]["fullAfter"] / (minwage_df[minwage_df["location"] == "PA"]["fullAfter"] + minwage_df[minwage_df["location"] == "PA"]["partAfter"])).mean()

fullPropAfter_NJ - fullPropAfter_PA


# 2.5.2 交絡バイアス
# NJとPAでは、バーガーキングの存在割合が大きく異なる。もしバーガーキングが雇用条件において
# 常勤雇用者を強く保護する方針だったりすると、バーガーキングが多くある州の方が、
# トリートメントなくても常勤雇用割合が増える可能性がある(＝バーガーキングが多い事が交絡因子

# 州別に、バーガーチェーン店の割合を見てみる
minwage_df_PA.groupby("chain").count()["location"] / minwage_df_PA.groupby("chain").count().sum()["location"]

minwage_df_NJ = minwage_df[minwage_df["location"] != "PA"]
minwage_df_NJ.groupby("chain").count()["location"] / minwage_df_NJ.groupby("chain").count().sum()["location"]

minwage_df_PA.loc[:, "fullPropAfter"] = minwage_df_PA.fullAfter / (minwage_df_PA.fullAfter + minwage_df_PA.partAfter)
minwage_df_NJ.loc[:, "fullPropAfter"] = minwage_df_NJ.fullAfter / (minwage_df_NJ.fullAfter + minwage_df_NJ.partAfter)

# 最低賃金が上がったNJでの常勤雇用割合は、バーガーキングのみのセグメントで比較しても、3.6ポイントくらい、
# 全体の差 4.8ポイント
# もし、チェーン店の違いが交絡因子だとして、チェーン店別の層別分析をしてみても、NJの方が常勤雇用割合が高い
# つまり、最低賃金を上げる事が、雇用になにか影響を与えているとはいえない
minwage_df_NJ[minwage_df_NJ["chain"] == "burgerking"]["fullPropAfter"].mean() - minwage_df_PA.loc[minwage_df_PA["chain"] == "burgerking"]["fullPropAfter"].mean()
minwage_df_NJ[minwage_df_NJ["chain"] == "roys"]["fullPropAfter"].mean() - minwage_df_PA.loc[minwage_df_PA["chain"] == "roys"]["fullPropAfter"].mean()
minwage_df_NJ[minwage_df_NJ["chain"] == "kfc"]["fullPropAfter"].mean() - minwage_df_PA.loc[minwage_df_PA["chain"] == "kfc"]["fullPropAfter"].mean()

# 他に交絡因子として考えられるのは、エリア。NJ州のなかでもPA州に近いところでは、
# PA州の特色を引き継いでいる可能性があり、その影響でNJ州での最低賃金が雇用率に与える影響がない、
# という事も考えられる(＝エリアが交絡因子)ので、エリアでの層別分析をする

# PA州から遠いエリアだけに限定したNJデータで、常勤割合の平均の差を比較。2つの交絡因子候補、チェーン✕エリア
minwage_df_NJ[(minwage_df_NJ["location"] != "shoreNJ") & (minwage_df_NJ["location"] != "centralNJ") & (minwage_df_NJ["chain"] == "burgerking")]["fullPropAfter"].mean() - minwage_df_PA[minwage_df_PA["chain"] == "burgerking"]["fullPropAfter"].mean()
minwage_df_NJ[(minwage_df_NJ["location"] != "shoreNJ") & (minwage_df_NJ["location"] != "centralNJ") & (minwage_df_NJ["chain"] == "roys")]["fullPropAfter"].mean() - minwage_df_PA[minwage_df_PA["chain"] == "roys"]["fullPropAfter"].mean()
minwage_df_NJ[(minwage_df_NJ["location"] != "shoreNJ") & (minwage_df_NJ["location"] != "centralNJ") & (minwage_df_NJ["chain"] == "kfc")]["fullPropAfter"].mean() - minwage_df_PA[minwage_df_PA["chain"] == "kfc"]["fullPropAfter"].mean()

# どのチェーンに対してエリアでさらに層別で見ても、最低賃金が常勤雇用割合に影響を与えている箇所は見られなかった

# 事前・事後分析
# NJでの法施行前の常勤雇用割合
minwageNJ_before = minwage_df_NJ.fullBefore / (minwage_df_NJ.fullBefore + minwage_df_NJ.partBefore)
minwageNJ_after = minwage_df_NJ.fullAfter / (minwage_df_NJ.fullAfter + minwage_df_NJ.partAfter)

NJ_diff = minwageNJ_after.mean() - minwageNJ_before.mean()

# DiD
# PAの事前の常勤労働者の割合

minwagePA_before = minwage_df_PA.fullBefore / (minwage_df_PA.fullBefore + minwage_df_PA.partBefore)
minwagePA_after = minwage_df_PA.fullAfter / (minwage_df_PA.fullAfter + minwage_df_PA.partAfter)

PA_diff = minwagePA_after.mean() - minwagePA_before.mean()

NJ_diff - PA_diff

# 2.6 記述統計量
# 中央値で横断比較とDiD

# 事後の常勤割合中央値の差(横断比較)
minwage_df_NJ.fullPropAfter.median() - minwage_df_PA.fullPropAfter.median()

# 事前事後比較(DiD)
minwage_df_NJ.loc[:, "fullPropBefore"] = minwage_df_NJ.fullBefore / (minwage_df_NJ.fullBefore + minwage_df_NJ.partBefore)
minwage_df_PA.loc[:, "fullPropBefore"] = minwage_df_PA.fullBefore / (minwage_df_PA.fullBefore + minwage_df_PA.partBefore)
NJdiff_med = minwage_df_NJ.fullPropAfter.median() - minwage_df_NJ.fullPropBefore.median()
PAdiff_med = minwage_df_PA.fullPropAfter.median() - minwage_df_PA.fullPropBefore.median()

NJdiff_med - PAdiff_med

# 四分位を見る
minwage_df_NJ.wageBefore.describe()
minwage_df_NJ.wageAfter.describe()

tempData = minwage_df_NJ[["wageBefore", "wageAfter"]].copy()
tempData = tempData.stack()
tempData = tempData.reset_index(level=[1])
tempData[[0]]
sns.boxplot(x="level_1", y=0, data=tempData)
plt.show()

# 10分位で見てみる
arr = []

for f in range(0, 101, 10) :
    arr.append(f / 100)

minwage_df_NJ.wageBefore.quantile(arr)
minwage_df_NJ.wageAfter.quantile(arr)

# RMS
import math
math.sqrt(((minwage_df_NJ.fullPropAfter - minwage_df_NJ.fullPropBefore)**2).mean())
(minwage_df_NJ.fullPropAfter - minwage_df_NJ.fullPropBefore).mean()

# 標準偏差
minwage_df_NJ.fullPropBefore.std()
minwage_df_NJ.fullPropAfter.std()

# 分散
minwage_df_NJ.fullPropBefore.var()
minwage_df_NJ.fullPropAfter.var()


