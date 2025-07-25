from scipy.stats import pearsonr
from data_loader import df
import statsmodels.api as sm
import matplotlib.pyplot as plt


r_coef = pearsonr(df['life_expectancy'], df['GDP'])
# This statistic is 0.34320674844915594 meaning there is a moderate correlation between life expectancy and gdp.

model = sm.OLS.from_formula("life_expectancy ~ GDP", data = df).fit()
# This model tells us that for a GDP of 0 life expectancy is 7.005478e+01 which is hypothetical as there is no country with a GDP of 0, It also tells us that for every $1 in GDP Life expectancy increases by 7.047546e-13.

fitted_values = model.predict(df)
residuals = df.life_expectancy - fitted_values

plt.hist(residuals)
plt.show()
plt.clf()
# This histogram of the residuals comes out left-skewed which indicates that it is not distributed normally and therefore linear regression is not a good way to model life expectancy.

print(df.describe())
# Life expectancy has an average of 72.79 across all years and countries with a minimum life expectancy of 44.4 and a maximum of 81.
# GDP has a mean of 3.8 trillion USD with a minimum of 44 billion USD and a maximum of 18.1 trillion USD across all countries and years.