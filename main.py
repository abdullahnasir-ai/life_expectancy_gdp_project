import matplotlib.pyplot as plt
from src.data_loader import df
import src.plotting as p

colors = plt.cm.tab10.colors

plt.figure(figsize = (10, 8))
for i in range(len(df['Country'].unique())):
    country = df['Country'].unique()[i]
    plt.subplot(2, 3, i + 1)
    p.timegdp(country, colors[i % len(colors)])
    plt.subplots_adjust(wspace = 0.4, hspace = 0.4)
plt.show()
plt.clf()

plt.figure(figsize = (10, 8))
for i in range(len(df['Country'].unique())):
    country = df['Country'].unique()[i]
    plt.subplot(2, 3, i + 1)
    p.timegdp(country)
    plt.subplots_adjust(wspace = 0.3, hspace = 0.3)
plt.show()
plt.clf()

