import pandas
from scipy import stats

#importa il DB da CSV sotto data
data = pandas.read_csv('CSV_linfomi_test.csv', sep=',', na_values="ND")

def mean_by_cat(category, val):
	groupby_STAGE = data.groupby(category)
	for stage, value in groupby_STAGE[val]:
		print((stage, value.mean()))

def ttest_by_cat(category, test_1, test_2, val):
	probe_1 = data[data[category] == test_1][val]
	probe_2 = data[data[category] == test_2][val]
	results = stats.ttest_ind(probe_1, probe_2, nan_policy='omit')
	print "T-TEST: ", category, " ", test_1, " vs ", test_2, ".\n",  "ttest force: ", results[0], "P: ", results[1]




#main

print "media PFS per STADIO"
mean_by_cat("STAGE", "PFS")

ttest_by_cat("STAGE", 1.0, 4.0, "PFS")
ttest_by_cat("STAGE", 2.0, 4.0, "PFS")

print "------------------------------------------------------------"

print "media OS per STADIO"
mean_by_cat("STAGE", "OS")

ttest_by_cat("STAGE", 1.0, 4.0, "OS")
ttest_by_cat("STAGE", 2.0, 4.0, "OS")


print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print "media PFS per risposta alla prima linea"
mean_by_cat("PL_RESP", "PFS")

ttest_by_cat("PL_RESP", "CR", "PD", "PFS")

print "------------------------------------------------------------"

print "media OS per risposta alla prima linea"
mean_by_cat("PL_RESP", "OS")

ttest_by_cat("PL_RESP", "CR", "PD", "OS")

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print "media PFS per prognosi alla diagnosi"
mean_by_cat("PROGNOSIS", "PFS")

ttest_by_cat("PROGNOSIS", "good", "poor", "PFS")

print "------------------------------------------------------------"

print "media OS per prognosi alla diagnosi"
mean_by_cat("PROGNOSIS", "OS")

ttest_by_cat("PROGNOSIS", "good", "poor", "OS")




