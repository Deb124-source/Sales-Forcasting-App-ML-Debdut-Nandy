import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Sales Forecaster AI",
    page_icon="📈",
    layout="wide"
)


# -------------------------------
# Load Model
# -------------------------------

model = pickle.load(
    open(
        "models/sales_forecast_model.pkl",
        "rb"
    )
)


latest_sales = pickle.load(
    open(
        "models/latest_sales.pkl",
        "rb"
    )
)



# -------------------------------
# Custom CSS
# -------------------------------

st.markdown(
"""
<style>

body {
    color: #1f2937;
}


.main {
    background-color: #f7f9fc;
}


/* KPI Cards */

.card {

    background-color: white;

    padding: 20px;

    border-radius: 15px;

    box-shadow: 0 4px 12px rgba(0,0,0,0.08);

    text-align: center;

    color: #111827;

}



/* Card headings */

.card h3 {

    color: #2563eb;

    font-size: 18px;

}



/* Card values */

.card h2 {

    color: #111827;

    font-size: 30px;

}



/* Normal text */

.stMarkdown {

    color: #111827;

}



/* Success / info boxes */

.stAlert {

    color: #111827;

}



</style>

""",
unsafe_allow_html=True
)


# -------------------------------
# Header
# -------------------------------

st.title(
    "📈 AI Powered Sales Forecasting System"
)


st.markdown(
"""
Predict future sales using Machine Learning 
based on historical sales patterns.
"""
)



st.divider()



# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.header(
    "🔮 Forecast Parameters"
)



year = st.sidebar.number_input(
    "Forecast Year",
    min_value=2024,
    max_value=2035,
    value=2025
)



month = st.sidebar.selectbox(
    "Forecast Month",
    list(range(1,13))
)



previous_sales = st.sidebar.number_input(
    "Previous Month Sales",
    value=float(
        latest_sales["Sales"]
    )
)



predict_btn = st.sidebar.button(
    "🚀 Predict Sales"
)


# -------------------------------
# KPI Cards
# -------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="card">

        <h3 style="color:#2563eb;">
        Last Sales
        </h3>

        <h2 style="color:#111827;">
        ₹ {latest_sales['Sales']:,.0f}
        </h2>

        <p style="color:#6b7280;">
        Previous Month Sales
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )



with col2:

    st.markdown(
        """
        <div class="card">

        <h3 style="color:#2563eb;">
        Model
        </h3>

        <h2 style="color:#111827;">
        XGBoost
        </h2>

        <p style="color:#6b7280;">
        Machine Learning Model
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )



with col3:

    st.markdown(
        """
        <div class="card">

        <h3 style="color:#2563eb;">
        Accuracy
        </h3>

        <h2 style="color:#111827;">
        R² ~ 0.71
        </h2>

        <p style="color:#6b7280;">
        Model Performance
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()



# -------------------------------
# Prediction
# -------------------------------


if predict_btn:


    input_data = pd.DataFrame(
        {

        "Year":[year],

        "Month":[month],

        "Lag_1":[previous_sales],

        "Lag_2":[previous_sales],

        "Rolling_Mean":[previous_sales]

        }
    )



    prediction = model.predict(
        input_data
    )[0]



    st.success(
        "Forecast Generated Successfully"
    )



    col1,col2 = st.columns(2)



    with col1:

        st.metric(
            "Predicted Sales",
            f"₹ {prediction:,.0f}"
        )



    with col2:

        growth = (
            (prediction-previous_sales)
            /
            previous_sales
        )*100


        st.metric(
            "Expected Growth",
            f"{growth:.2f}%"
        )



    # ---------------------------
    # Chart
    # ---------------------------


    chart_data = pd.DataFrame(
        {

        "Type":
        [
        "Previous Sales",
        "Forecast Sales"
        ],


        "Sales":
        [
        previous_sales,
        prediction
        ]

        }
    )



    fig = go.Figure()



    fig.add_trace(
        go.Bar(
            x=chart_data["Type"],

            y=chart_data["Sales"],

            text=chart_data["Sales"],

            textposition="auto"

        )
    )



    fig.update_layout(

        title="Sales Forecast Comparison",

        xaxis_title="",

        yaxis_title="Revenue",

        height=400

    )



    st.plotly_chart(
        fig,
        use_container_width=True
    )



    # ---------------------------
    # Insight
    # ---------------------------


    if prediction > previous_sales:

        st.info(
        """
        📊 Expected growth detected.
        Future sales are predicted to increase
        compared to the previous period.
        """
        )

    else:

        st.warning(
        """
        ⚠️ Possible sales decline predicted.
        Consider reviewing pricing,
        demand and marketing strategies.
        """
        )



else:


    st.info(
    "Select forecast parameters and click Predict."
    )
