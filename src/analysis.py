import pandas as pd
from scipy.stats import pearsonr
from data_loader import df
import statsmodels
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

r_coef = pearsonr(df['life_expectancy'], df['GDP'])
# This statistic is 0.34320674844915594 meaning there is a moderate correlation between life expectancy and gdp.


