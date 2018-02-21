import math
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats.mstats import gmean

data = pd.read_csv("Ch1_例題.csv")

corr = data.corr()
print(corr.parents_mean.child)

del data["num"]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(data["parents_mean"], data["child"], "o")
plt.show()

# 問題2
data = pd.read_csv("Ch1_章末問題2.csv")

# 階級 の 数 の 目安 として，「 データ 数 の 平方根 に プラス 1」 程度
num_degree = round(math.sqrt(data.shape[0]) + 1)

# 実際にビニングする
data.loc[:, "dimension_bin"] = pd.cut(data["dimension"], num_degree)

# グラフ化
dimension_bin = data.groupby(by="dimension_bin", as_index=False).count()[["dimension_bin", "dimension"]]
fig = plt.figure()
# ヒストグラムを作る時は、単純にデータシーケンスと、分けたいBIN数を渡せばイケる
ax.hist(data['dimension'], num_degree)
fig.show()

# 算術平均、分散、標準偏差、変動係数を求める
data.describe()

data["sellAmount"].mean()
data["sellAmount"].var()
data["sellAmount"].std()
coefficient_of_variation = data["sellAmount"].std() / data["sellAmount"].mean()

data["dimension"].mean()
data["dimension"].var()
data["dimension"].std()
coefficient_of_variation = data["dimension"].std() / data["dimension"].mean()

# 相関係数を求める
data.corr()

# 問3
arr1 = pd.DataFrame([2, 4, 5, 7])
arr2 = pd.DataFrame([2, 4, 5, 70])

arr1.mean()
arr2.mean()
gmean(arr1)
gmean(arr2)
# 幾何平均だと、70 という突出した値が混じっていても、大きくハズレる事がないのがみてとれるよね。