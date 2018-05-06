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

print(upper, lower)

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

print(lower, upper)


# 例題
# ある日，ある酪農家が，搾乳中のホルスタイン5頭の乳量を調べたら，
# 1頭あたりの平均乳量は22.1リットル，標本標準偏差は6.5リットルでした。
# この農家が飼養しているホルスタインの1頭あたりの乳量（／日）を，
# 信頼係数95％で推定してください。

sampleSize = 5
mean_sample = 22.1
sd_sample = 6.5

# 標本サイズが小さい、母数未知、母平均の推定＝ 統計量 T を使った推定をする。
# t分布表から、自由度(df)が4の時の、95%信頼係数の数値は、2.776であることが、ｔ分布表から分かる。
# 信頼限界の下限と上限を出す式も、Tから算出できるので、算出すると・・・

lower = mean_sample - 2.776 * (sd_sample / math.sqrt(sampleSize - 1))
upper = mean_sample + 2.776 * (sd_sample / math.sqrt(sampleSize - 1))

print(lower, upper)

# 例題
# ある市長選挙でA氏とB氏が立候補しました。50人に対する出口調査の結果，
# A氏の得票率は70％でした。この結果からA氏について当確を出してもよいでしょうか？
# 信頼係数95％で判断してください。

sampleSize = 50
sampleRate = 0.7

lower = sampleRate - 1.96 * math.sqrt(sampleRate*(1-sampleRate) / sampleSize)
print(lower)

# 下限値が57%を越えているので、当確をだしてもよい。


# 例題
# A君は卒論のためにアンケート調査を実施しなければなりませんが，お金も時間もないため，
# 母比率に対する信頼係数95％の信頼区間を推定する際，標本誤差が10％以内に
# 収まればよいと考えています。
# さて，A君は何人ぐらいから回答を得られればよいでしょうか？

sampleSize = 0

for samplesize in range(100):
    sampleSize += 1
    if 1.96 * (math.sqrt(0.5 * 0.5 / sampleSize)) < 0.1:
        print(sampleSize)
        break

# 章末問題
# 問1　ある島に調査に行って，そこに自生しているスギの中から無作為に100本を選び，
# 胸高周囲（成人の胸の高さでの幹周り）を観測したところ，標本平均が2.0m，
# 標本分散が1.0m2でした。
# この島のスギの平均胸高周囲の信頼区間を信頼係数95％で推定しなさい。

sampleSize = 100
sample_mean = 2.0
sample_var = 1.0
population_var = sample_var

# 標本サイズが充分に大きく、かつ母集団が正規分布していると考えられるので、
# 母分散が既知の区間推定をする

lower = sample_mean - 1.96 * math.sqrt(population_var) / math.sqrt(sampleSize)
upper = sample_mean + 1.96 * math.sqrt(population_var) / math.sqrt(sampleSize)

print(lower, upper)

# 同じことを、scipy でやってみる

import scipy.stats as stats

# 標準正規分布(stats.norm) で、標準偏差が 母標準偏差÷√n の間に母平均が収まっているとも捉える事ができるので、
# 以下の区間が95%信頼区間、としてさっと出せる。
stats.norm.interval(0.95, loc = sample_mean, scale = math.sqrt(population_var/sampleSize))

# 問2
# 第1章の章末問題で使用した農家データから，この地域の農家の平均販売金額の
# 信頼区間を信頼係数95％で推定しなさい。

# データ準備
import pandas as pd
data = pd.read_csv("ch4/Ch1_章末問題2.csv")
# データ状況把握
data
data["sellAmount"].describe()

# 一応、標本分布も見ておく
%matplotlib
data["sellAmount"].hist()

# 標本サイズ小さい、標本自体もわけわからん分布＝母集団が正規分布かどうかわからん、ので、
# 統計量Tを使った区間推定にする

import scipy.stats as stats
import math

sampleSize = len(data.sellAmount)
sample_mean = data.sellAmount.mean()
sample_sd = data.sellAmount.std(ddof=0)
sample_sd
lower = sample_mean - 2.093 * (sample_sd / math.sqrt(sampleSize-1))
upper = sample_mean + 2.093 * (sample_sd / math.sqrt(sampleSize-1))
lower, upper

stats.t.interval(0.95, sampleSize - 1, loc = sample_mean, scale=sample_sd / math.sqrt(sampleSize-1))
import statsmodels.stats.weightstats as weightstats
weightstats._tconfint_generic(sample_mean, sample_sd / math.sqrt(sampleSize-1), sampleSize-1, 1-0.95, "2s")

# 問3
# あるペットショップの猫の中から20匹を無作為抽出して血液型を調べたところ，
# A型の猫が16匹，B型が3匹，AB型が1匹でした（猫の血液型にO型はありません）。
# このペットショップの猫の中で，血液型がA型である比率を信頼係数95％で推定しなさい。
# ただし，標本サイズが小さいので，AgrestiとCoullの式を使うこと。

sampleSize = 20
targetCount = 16
p = targetCount / sampleSize
p_dash = (targetCount + 2) / (sampleSize + 4)
p, p_dash
lower = p_dash - 1.96 * math.sqrt( (p_dash * (1- p_dash) ) /(sampleSize + 4) )
upper = p_dash + 1.96 * math.sqrt( (p_dash * (1- p_dash) ) / (sampleSize + 4) )
lower, upper

# statsmodel package ver
import statsmodels.stats as sm_stats
sm_stats.proportion.proportion_confint(targetCount, sampleSize, 0.05, method='agresti_coull')

# 問4
# 郵送によるアンケート調査を実施することになりました。
# とても大事な調査で，かつ予算も十分にあるので，精度の高い調査を実施しようと思います。
# 標本誤差が1％となるような調査を目指す場合，何件に調査票を発送すべきかを求めなさい。
# ただし，返信率は20％とし，返信された回答はすべて分析に使えるとする。

# アンケート調査なので、母集団の比率を調査するものと捉える。
# 信頼係数95%で母比率を区間推定する前提で考え、標本誤差を考えると・・・

sampleSize = 1

for sampleSize in range(10000):
    sampleSize += 1
    if 1.96 * math.sqrt(0.5 * 0.5 / sampleSize) < 0.01:
        print('アンケートを発送する数は、' + str(sampleSize / 0.2))
        print('手元に欲しい回答数は、' + str(sampleSize))
        break
