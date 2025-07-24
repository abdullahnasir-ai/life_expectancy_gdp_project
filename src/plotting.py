import matplotlib.pyplot as plt
from src.data_loader import df

def timegdp(country, color):
    df_country = df[df['Country'] == country]
    plt.plot(df_country['Year'], df_country['GDP'],color = color, marker = 'o')
    plt.title(f"Country - {country}")
    plt.xlabel('Year')
    plt.ylabel('GDP in Trillions')

def lifegdp(country, color):
    df_country = df[df['Country'] == country]
    plt.scatter(df_country['life_expectancy'], df_country['GDP'],color = color, marker = 'o')
    plt.title(f"Country - {country}")
    plt.xlabel('Life Expectancy')
    plt.ylabel('GDP in Trillions')

