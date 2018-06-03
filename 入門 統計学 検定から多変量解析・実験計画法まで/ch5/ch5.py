import scipy.stats as stats
import math

alpha = 0.95
df = 5-1
mean = (5+8+10+11+15) / 5
loc = mean
sample_sd = math.sqrt( ( (5-mean) ** 2 + (8-mean) ** 2 + (10-mean) ** 2 + (11-mean) ** 2 + (15-mean) ** 2 ) / (5-1) )
scale = 1
lower, upper = stats.chi2.interval(alpha, df, loc=0, scale=1)
df * sample_sd ** 2 / lower
df * sample_sd ** 2 / upper

# 章末問題の3
# 10年間の農業所得率の不偏標準偏差
sample_sd = 0.05
# 標本サイズn
n = 10
# 農家の経営上のリスク＝農業所得率の簿標準偏差が入ると考えられる信頼区間を、信頼係数90％で推定しなさい
alpha = 0.9
df = n - 1
# 標準化されたカイ二乗分布表から、上限値と下限値を持ってくる
lower, upper = stats.chi2.interval(alpha, df, loc=0, scale=1)
# 上限値、下限値に基づいた、実際の標準偏差の区間を求める
math.sqrt(df * sample_sd ** 2 / lower)
math.sqrt(df * sample_sd ** 2 / upper)