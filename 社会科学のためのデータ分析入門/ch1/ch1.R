resume  <- read.csv("officialSource/qss-master/CAUSALITY/resume.csv")
head(resume)
# レコード数と変数の数を確認できる
dim(resume)

# データの状況をざっくり確認
summary(resume)

# 人種x連絡フラグのクロス集計表をつくる
race.call.tab <- table(race = resume$race, call=resume$call)
race.call.tab
addmargins(race.call.tab)

# 審査通過率
race.call.tab[, 2]


