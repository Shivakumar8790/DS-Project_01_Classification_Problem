# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:04:15 2023

@author: 91879
"""

import numpy as np
import pandas as pd



    # 1Q A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
    
df1 = pd.read_csv("D:/Shiva Data Science/ExcelR Assignments/Hypothesis Testing/Cutlets.csv")
df1

    ## Two sample test
#    H0 = There is no difference in the average dia of the cutlet between two units.
#    H1 = There is a difference in the average dia of the cutlet between two units.
from scipy import stats

Zcal, P_value = stats.ttest_ind(df1["Unit A"], df1["Unit B"],equal_var=True)

Zcal, P_value
print("Z statistic value:",Zcal)
print("P Value",P_value)

if P_value < 0.05:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 accepted")
    
    
        
#=================================================================================

import numpy as np
import pandas as pd


  # 2Q A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
   ## Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
    
df2 = pd.read_csv("D:/Shiva Data Science/ExcelR Assignments/Hypothesis Testing/LabTAT.csv")
df2

# Make it in single list with group

df2_single_data = pd.melt(df2, value_vars=["Laboratory 1","Laboratory 2","Laboratory 3","Laboratory 4"], var_name='Lab', value_name='TAT')
df2_single_data

    ## Annova test
#    H0 = there is no difference in the average Turn Around Time (TAT) of reports of the laboratories
#    H1 = there is any difference in the average Turn Around Time (TAT) of reports of the laboratories


from statsmodels.formula.api import ols
anova1 = ols('TAT ~ C(Lab)',data=df2_single_data).fit()
anova1

import statsmodels.api as sm
table = sm.stats.anova_lm(anova1, type=1) 
table

pvalue =table['PR(>F)'][0]
pvalue.round(9)
alpha = 0.05

if pvalue < alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")


#=================================================================================

import pandas as pd
## 3Q  Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.

df3 = pd.read_csv("D:/Shiva Data Science/ExcelR Assignments/Hypothesis Testing/BuyerRatio.csv")
df3

    # H0 = male-female buyer rations are similar across regions
    # H1 = male-female buyer rations are not similar across regions

## calculating the critical value
import researchpy as rp

table,results = rp.crosstab(df3['Observed Values'], df3[['East', 'West', 'North', 'South']], prop="col", test="chi-square")

# Remove the index numbers
table.reset_index(drop=True, inplace=True)

print(table)
print(results)

## Calculating the table value 
import scipy.stats as stats
crit = stats.chi2.ppf(q = 0.95, df = 3)
crit.round(4)

pvalue =table['PR(>F)'][0]
pvalue
alpha = 0.05

if pvalue < alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")



#=================================================================================


import pandas as pd
## 4Q  TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences  

df4 = pd.read_csv("D:/Shiva Data Science/ExcelR Assignments/Hypothesis Testing/Costomer+OrderForm.csv")
df4


    # H0 = male-female buyer rations are similar across regions
    # H1 = male-female buyer rations are not similar across regions

## calculating the critical value
import researchpy as rp

table = pd.crosstab(df4["Phillippines"],[df4["Indonesia"],df4["Malta"],df4["India"]])
table

from scipy.stats import chi2_contingency

chi2, P_Value, dof, expected = chi2_contingency(table)
P_Value


P_Value
alpha = 0.05

if P_Value < alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")






