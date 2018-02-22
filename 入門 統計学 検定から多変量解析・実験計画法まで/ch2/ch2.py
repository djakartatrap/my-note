import pandas as pd
data = pd.read_csv("入門 統計学 検定から多変量解析・実験計画法まで/ch2/キュウリ.csv")

# 標準化カラムを個別に作る
data["normalizedA"] = (data.cultivationA - data.cultivationA.mean()) / data.cultivationA.std(ddof=False)
data["normalizedB"] = (data.cultivationB - data.cultivationB.mean()) / data.cultivationB.std(ddof=False)

# 標準化された値の平均値と標準偏差を確認
data.normalizedA.mean()
data.normalizedA.std()

data.normalizedB.mean()
data.normalizedB.std()

"""
例題2
"""
# 日本では過去 5 年間（ 2006 年 4 月 ～ 2011 年 3 月） に マグニチュード 7 以上 の 大きな 地震（余震は除く）は 7 回 起こっていました（1. 4回／年）。
# これから 3日の間にマグニチュード 7 以上の地震が 1回起きる確率はいくつになるでしょうか。

# λ値を算出
# 試行回数3日で、M7以上の地震が起きる確率(1日あたり)、というのを使って算出
my_lambda = 3 * (1.4 / 365)

import math

x = 1
# 確率質量関数に代入する
myValue = math.pow(math.e, (-my_lambda)) * math.pow(my_lambda, x) / math.factorial(x)

"""
章末問題
"""

# 問1
data = pd.read_csv("./ch1/Ch1_章末問題2.csv")
data["norm_sellAmount"] = (data.sellAmount - data.sellAmount.mean()) / data.sellAmount.std(ddof=False)
data["norm_dimension"] = (data.dimension - data.dimension.mean()) / data.dimension.std(ddof=False)

# 一応確認
data.norm_sellAmount.mean()
data.norm_sellAmount.std()
data.norm_dimension.mean()
data.norm_dimension.std()

# 問2
# 歪度
data.skew()
# 尖度
data.kurtosis()

# 問3
# 標準化
myPoint = 80
all_mean = 60
std = 10
z_score = (myPoint - all_mean) / std
# 偏差値
hensa = 10*(myPoint - all_mean) / std + 50

# 問4
# zスコアが2.0の時の確率密度を、分布表で探すと、上側確率＝0.0228なので、上位2.3％くらいに居る。

# 問5
# 1人以上の食中毒者が発生する確率 / 日 を出したい。

all_population = 127370000
matsudo_population = 484600
foodPoisoning_perDay_perPerson = 20204 / 365 / all_population

# 松戸市民一人一人にたいして、1日あたりの食中毒になる確率を当てはめていけばいいので、試行回数は松戸市民分になる。
n = matsudo_population
# 1人も起きない場合(1回も起きない場合)を考えるので、x＝0となる
x = 0
p = foodPoisoning_perDay_perPerson
my_lambda = n * p

# ポアソン分布の確率質量関数に入れる
myValue = math.pow(math.e, (-my_lambda)) * math.pow(my_lambda, x) / math.factorial(x)