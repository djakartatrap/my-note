import pandas as pd
import math

data = pd.read_csv("入門 統計学 検定から多変量解析・実験計画法まで/ch3/キュウリ.csv")

"""
例題
キュウリの収量を不偏標準誤差を、栽培法ごとに計算
"""

# 不偏標準誤差＝標本標準偏差 / √(n-1) なので・・・

data.std() / math.sqrt(data.shape[0])


"""
章末問題
"""
"""
問題1

ある大学で，統計学の授業内容の検討資料とするため，新入生の学力を測ることにしました。しかし新入生だけでも1万人もいるマンモス大学のため，無作為に500人だけ
抽出して試験を行うことにしました。この調査（試験）における母集団，標本，ユニバースが何にあたるか，また標本数がいくつかを答えなさい。

母集団＝大学の全新入生の1万人分の学力(試験の点数)
標本＝無作為に選ばれた500人の新入生の学力(試験の点数)
ユニバース＝大学の全新入生1万人分の様々な属性データ
標本数＝1 ← 500人の抽出を1回だけ行うので。標本サイズとの違いをしっかり把握すること！
"""

"""
問題2

母分散（有限母集団から計算した分散）と標本分散（標本から計算した分散）とでは どちら が 大きく なる か 答え なさい。

母分散の方が大きくなる
"""

"""
問題3

標準偏差と標準誤差の違いを述べよ。

標準偏差は、標本内の各要素のバラツキを表す指標。
標準誤差は、母集団から得られる標本の平均(標本平均)のバラツキを表す指標。
特に標準誤差は、「標準偏差 / 標本サイズの平方根」なので、標本サイズが大きくなるほど、標準誤差は小さくなる。
なので、標準誤差は、様々な不偏統計量の精度を示す指標として使われる。
"""

"""
問題4

母集団の相関係数を標本から推測する際、その統計量の自由度はいくつになるか？

相関係数＝2つの集合の平均を用いて計算する値 なので、

自由度は n-2

"""