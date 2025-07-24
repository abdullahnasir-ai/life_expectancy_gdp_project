import matplotlib.pyplot as plt
from src.data_loader import df
import src.plotting as p

plt.figure(figsize = (12, 10))
for i in range(len(df['Country'].unique())):
    country = df['Country'].unique()[i]
    plt.subplot(2, 3, i + 1)
    p.timegdp(country)
    plt.subplots_adjust(wspace = 0.3, hspace = 0.3)
plt.show()
plt.clf()

