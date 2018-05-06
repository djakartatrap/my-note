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

