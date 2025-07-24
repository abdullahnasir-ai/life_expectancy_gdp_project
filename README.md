# 🌍 Life Expectancy vs GDP: A Data Analysis Project

This project explores the relationship between GDP and life expectancy across six countries using real-world data. The goal was to analyse whether economic growth correlates with improvements in population health, and to visualise trends using Python.

---

## 📌 Project Objectives

- Investigate whether GDP is correlated with life expectancy  
- Plot GDP over time for six selected countries  
- Analyse and visualise the relationship between GDP and life expectancy using scatter plots, line plots, and linear regression

---

## 📊 Data Source

The dataset used is `all_data.csv`, which combines GDP and life expectancy data for six countries between 2000–2015. The original data was sourced from:

- World Bank (GDP)  
- World Health Organization (Life Expectancy)

---

## 🛠️ How to Run This Project

To run this project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/abdullahnasir-ai/life_expectancy_gdp_project.git
cd life_expectancy_gdp_project
```

### 2. Install dependencies

Ensure you have Python 3 installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the project

Once everything is set up, execute the following command:

```bash
python main.py
```

This script will:
- Load and clean the dataset  
- Convert GDP values to trillions  
- Generate and GDP-over-time plots for each country  
- Create scatter plots of GDP vs life expectancy  
- Perform linear regression and correlation analysis

---

## 🗂️ Project Structure

```
life_expectancy_gdp_project/
├── data/
│   └── all_data.csv
├── src/
│   ├── data_loader.py      # Loads and cleans data     
│   ├── analysis.py         # Runs regression and stats
│   └── plotting.py         # Generates plots
├── main.py                 # Orchestrates the analysis pipeline
├── README.md               # You're reading it
└── requirements.txt        # Python dependencies
```

---

## 📈 Outputs

- **📉 Time Series Plots**  
  Line plots showing GDP growth over time for each of the six countries (2000–2015).

- **📊 Scatter Plot: Life Expectancy vs GDP**  
  A scatter plot visualising the relationship between GDP (in trillions) and life expectancy across countries.

- **📈 Linear Regression Analysis**  
  Statistical model summary showing the strength and nature of the relationship between GDP and life expectancy.

- **📉 Residual Plots**  
  Diagnostic plots assessing regression assumptions like normality.

- **📝 Blog Summary**  
  Final written analysis and reflection on [Blog Post](https://medium.com/@abdullah.nasir1905/does-wealth-equal-health-e33ffb4806af), including what was learned, key findings, and whether the results matched expectations.

---

## 📚 Key Libraries Used

- `pandas` – for data manipulation  
- `matplotlib` – for visualisations  
- `seaborn` – for enhanced plots  
- `statsmodels` – for linear regression and statistical analysis  
- `scipy` - for correlation analysis

---

## ✍️ Author

Abdullah Nasir  
BSc Mathematics @ Queen Mary University of London  
GitHub: [@abdullahnasir-ai](https://github.com/abdullahnasir-ai)

