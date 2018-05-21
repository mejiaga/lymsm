import pandas
from scipy import stats

#DOCUMENTATION

#Start here
#http://www.scipy-lectures.org/packages/statistics/index.html

#Pandas DataFrame doc
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame

#Categorize list
#http://pandas.pydata.org/pandas-docs/stable/categorical.html

#Scipy docs

#t-test
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind

#Compute the Mann-Whitney rank test on samples x and y. -> use for non-normalized data
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html#scipy.stats.mannwhitneyu

#some funcion to compute some data

def time_interval(time_from, time_to, AgeType):
	


class DLBC_patient:
	def __init__(self, dataframe, index):
		self.age = dataframe.iloc[index]['AGE']
		self.perfomance_status =  dataframe.iloc[index]['PS']
		self.LDH =  dataframe.iloc[index]['LDH']
		self.AAstage =  self.ann_arbour_stage()
		self.extranodal_site =  dataframe.iloc[index]['EXTRANODAL']

	def ann_arbour_stage(self):
		#return array as ['I', 'A', 'X'] or ['III', 'B', '0']
		#'0' is a placeholder, meanig that this parameter is null

	def R_IPI_score(self):
		#return array as ['pt', 'prognosis'] -> ['0', 'VERYGOOD']



