# 例題
# ある園芸農家が，母の日に向けて出荷を控えたカーネーション16本の蕾の直径を調べたところ，平均で10.0mmでした。
# この園芸農家の栽培しているカーネーションの蕾の平均直径を信頼係数95％で推定してください。
# ただし，母分散は36.0mm2であることがわかっているとします。

import math

var_population = 36
mean_sample = 10
n_sample = 16

# 95%信頼限界の上限
upper = mean_sample + 1.96*(math.sqrt(var_population / n_sample))

# 95%信頼限界の下限
lower = mean_sample - 1.96*(math.sqrt(var_population / n_sample))

# 例題
# 中国産キャベツの輸入量と，中国産野菜に関する新聞記事の掲載回数との関係について調べたところ（2000年1月～2006年6月），
# 1回の掲載につき輸入量が月平均で165.0トン減少していたことがわかりました。
# この減少量について，信頼係数90％の信頼区間を推定してください。
# なお，標本サイズは66（月），標本標準偏差は680.6（トン）です。

var_population = None
mean_sample = 165
n_sample = 66
std_sample = 680.6

# 母分散が未知だが、標本サイズ(66)が大きいので、この標本≒母集団と見て良い
# なので、標本平均＝母平均、標本標準偏差＝母標準偏差と見て良いので・・・

upper = mean_sample + 1.65 * std_sample / math.sqrt(n_sample)

lower = mean_sample - 1.65 * std_sample / math.sqrt(n_sample)