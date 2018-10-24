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