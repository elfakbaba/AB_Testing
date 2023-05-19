#####################################################
# Comparison of AB Test and Conversion of Bidding Methods
#####################################################

#####################################################
# Task 1: Preparing and Analyzing Data
#####################################################

# Facebook alternative to the recently available bidding type called "maximumbidding" As 
# it revives a new type of bidding, "average bidding". One of the protectors, bombambomba.com,
# decided to test this new feature and make averagebidding more performance than maximumbidding wants to run an A/B test to see if it returns 
# The A/B test continues to store 1 and
# bombabomba.com is now waiting for you to analyze the results of this A/B test.For Bombamboba.com
# The ultimate measure of success is Purchasing. Therefore, the focus should be on Purchasing metric for constraints.

#####################################################
# Dataset Story
#####################################################

# What users see and click in this dataset, which includes a company's website information
# There is information such as the number of advertisements, as well as the earnings information from here. Control and Test There are two separate data sets, the 
# group. These datasets are on separate sheets of the ab_testing.xlsx excel.
# takes. Maximum Bidding was applied to the control group and AverageBidding was applied to the test group.

# impression: Number of ad views
# Click: Number of clicks on the displayed ad
# Purchase: The number of products purchased after the ads clicked
# Earning: Earnings after purchased products

#####################################################
# TASKS
#####################################################

#####################################################
# Tasks 1:
#####################################################

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("/Users/dlaraalcan/Desktop/ab_testing.xlsx" , sheet_name="Control Group")
dataframe_test = pd.read_excel("/Users/dlaraalcan/Desktop/ab_testing.xlsx" , sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df_control)
check_df(df_test)

df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control,df_test], axis=0,ignore_index=False)
df.head()
df.shape

df.groupby("group").agg({"Purchase": "mean"})

#####################################################
# Task 2:  A/B Test Hypothesis
#####################################################

# H0 : M1 = M2 There is no difference between the purchasing averages of the two groups.
# H1 : M1!= M2 There is a difference between the purchase averages of the two groups.

df.groupby("group").agg({"Purchase": "mean"})

#####################################################
# TASK 3
#####################################################
##################################################
# AB Testing (Independent Two Sample T Test)
##################################################

# Step 1: Check the assumptions before testing the hypothesis. These are Assumption of Normality and Homogeneity of Variance.

# Test separately whether the control and test groups comply with the normality assumption via the Purchase variable.

# H0: Normal distribution assumption is provided.
# H1:..not provided

test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value=0.5891
# p-value>0.05 H0 cannot be rejected.

# When we applied the normality assumption test in both groups, the P value values showed that we provided the normality assumption.

#######################################
# Assumption of Variance Homogeneity
#######################################

# H0: Variances are Homogeneous
# H1: Variances Are Not Homogeneous
test_stat, pvalue = levene(test_group["Purchase"],
                           control_group["Purchase"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 2.6393, p-value = 0.1083
# p-value>0.05 H0 cannot be rejected. Variances are homogeneously distributed.

# Step 2: Select the appropriate test according to the Normality Assumption and Variance Homogeneity results
# We will apply parametric test as it provides the assumption of Normality and Homogeneity of Variance.

test_stat, pvalue = ttest_ind(test_group["Purchase"],
                              control_group["Purchase"],
                              equal_var=True)  # We would do the Welch test if variance homogeneities were not provided (it would be equal_var=False)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9416, p-value = 0.3493

# Step 3: Purchasing control and test groups, taking into account the p_value obtained as a result of the test
# Comment if there is a statistically significant difference between the # means.

# p-value>0.05 H0 cannot be rejected. It showed that there was no difference between the two groups.
# Observes that there is no statistically significant difference
