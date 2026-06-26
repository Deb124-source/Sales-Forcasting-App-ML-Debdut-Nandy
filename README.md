# 📈 AI Powered Sales Forecasting System

An end-to-end **Machine Learning + Streamlit Sales Forecasting Application** that predicts future sales using historical sales patterns.

The project combines:
- Data Analytics
- Machine Learning Regression
- Time-series Feature Engineering
- Interactive Streamlit Deployment

---

## 🚀 Live Demo

🔗 Streamlit App:

https://sales-forcasting-app-debdut-nandy.streamlit.app/

---

## App Overview
<img src="" width="700">

---


## 📌 Project Overview

Sales forecasting helps businesses estimate future revenue and make better decisions related to:

- Inventory planning
- Marketing strategy
- Revenue prediction
- Business growth analysis

This application uses historical sales data and an **XGBoost regression model** to forecast future sales based on previous sales trends.

---

# 🛠️ Tech Stack

## Programming
- Python

## Data Processing
- Pandas
- NumPy

## Machine Learning
- XGBoost
- Scikit-learn

## Visualization
- Plotly

## Deployment
- Streamlit Cloud


---

# 📂 Project Structure


```

Sales-Forecasting-App

│
├── app.py
│
├── requirements.txt
│
├── models
│   ├── sales_forecast_model.pkl
│   └── latest_sales.pkl
│
└── README.md

````

---

# 📊 Dataset

The project uses historical sales transaction data containing:

- Order Date
- Sales
- Category
- Region
- Customer Information
- Product Details


The dataset was transformed into monthly sales trends for forecasting.

---

# 🔎 Data Preprocessing

Steps performed:

✔ Converted order dates into datetime format

✔ Extracted time-based features:

- Year
- Month
- Quarter


✔ Created forecasting features:

- Previous month sales
- Lag features
- Rolling average


✔ Prepared data for machine learning training

---

# 🤖 Machine Learning Model

## Model Used

### XGBoost Regressor


Why XGBoost?

- Handles nonlinear patterns
- Performs well on structured data
- Efficient for regression problems
- Provides strong forecasting performance


---

# 📈 Model Performance

Evaluation Metrics:


| Metric | Score |
|-|-|
| R² Score | ~0.71 |
| MAE | ~10K |
| RMSE | ~13K |


### Interpretation

The model explains around **71% of sales variation**, making it suitable for predicting future sales trends.

---

# 🖥️ Application Features

## 🔮 Sales Prediction

Users can input:

- Forecast Year
- Forecast Month
- Previous Month Sales


The application predicts expected future revenue.

---

## 📌 Dashboard Highlights
<img src="" width="700">


### KPI Cards

Displays:

- Latest Sales
- ML Model Used
- Model Performance


---

### Forecast Output

Shows:

- Predicted Sales
- Expected Growth Percentage


---

### Visualization

Interactive comparison between:

- Previous Sales
- Forecasted Sales


---

# ⚙️ Installation


Clone repository:

```bash
git clone https://github.com/yourusername/Sales-Forecasting-App.git
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 📦 Requirements

```
streamlit
pandas
numpy
plotly
scikit-learn
xgboost
```

---

# 🧠 Future Improvements

Possible enhancements:

* Add Prophet forecasting model
* Add confidence intervals
* Add category-wise forecasting
* Add automated retraining pipeline
* Add real-time sales database connection

---

# 👨‍💻 Author

**Debdut Nandy**

GitHub:
[https://github.com/Deb124-source](https://github.com/Deb124-source)

---

⭐ If you found this project useful, consider giving it a star!


