import pandas
from scipy import stats



#importa il DB da CSV sotto data
data = pandas.read_csv('CSV_linfomi_test.csv', sep=',', na_values="ND")

# colonne = data.columns
# print colonne

#categorizzare una serie di dati: array

cat_data = pandas.Series(data['PL_RESP'], dtype="category")


def media_per_categorie(data_frame, col_cat, col_val):
	cat_data = pandas.Series(data_frame[col_cat], dtype="category")
	for category in cat_data.cat.categories:
		print "la media di ", col_val, "tra i ", category, ": ", data_frame[data_frame[col_cat] == category][col_val].mean()

#media_per_categorie(data, 'PL_RESP', 'PFS')
#media_per_categorie(data, 'PL_RESP', 'OS')

#yet exist:

def overall_mean():
	for x in data.columns[1:]:
		groupby_category = data.groupby(x)
		print "mean value for value categorized by:", x
		print groupby_category.mean()
	
#confrontiamo due medie


#ttest per uso di rituximab e PFS e OS

rituximab_0_OS = data[data['PL_RITUXIMAB'] == 'n']['OS']
rituximab_1_OS = data[data['PL_RITUXIMAB'] == 'y']['OS']

rituximab_0_PFS = data[data['PL_RITUXIMAB'] == 'n']['PFS']
rituximab_1_PFS = data[data['PL_RITUXIMAB'] == 'y']['PFS']

print "ttest RITUXIMAB vs NON: OS", stats.ttest_ind(rituximab_1_OS, rituximab_0_OS, nan_policy='omit') 
print "ttest RITUXIMAB vs NON: PFS", stats.ttest_ind(rituximab_1_PFS, rituximab_0_PFS, nan_policy='omit')

#ttest VEMP vs CHOP in PFS
VEMP_PFS = data[data['P_LINEA'] == 'VEMP']['PFS']
CHOP_PFS = data[data['P_LINEA'] == 'CHOP']['PFS']

print "ttest VEMP vs CHOP: PFS", stats.ttest_ind(CHOP_PFS, VEMP_PFS, nan_policy='omit')

#stats.wilcoxon(data['FSIQ'], data['PIQ'])
