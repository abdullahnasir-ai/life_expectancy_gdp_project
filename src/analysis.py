import pandas as pd
from scipy.stats import pearsonr
from data_loader import df
import statsmodels

r_coef = pearsonr(df['Life expectancy at birth (years)'], df['GDP'])
# This statistic is 0.34320674844915594 meaning there is a moderate correlation between life expectancy and gdp.


