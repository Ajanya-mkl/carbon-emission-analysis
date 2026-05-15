import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Carbon Emission Dashboard",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/final_dataset.csv")
    return df

df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Filters")

metric = st.sidebar.selectbox(
    "Select Metric",
    [
        'co2_per_capita',
        'renewable_energy',
        'gdp',
        'energy_consumption'
    ]
)

countries = sorted(df['country'].unique())

select_all = st.sidebar.checkbox(
    "Select All Countries",
    value=True
)

if select_all:
    selected_countries = countries
else:
    selected_countries = st.sidebar.multiselect(
        "Select Country",
        countries,
        default=countries[:10]
    )

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df['year'].min()),
    int(df['year'].max()),
    (
        int(df['year'].min()),
        int(df['year'].max())
    )
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df['country'].isin(selected_countries)) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1])
]

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    "Download Filtered Data",
    csv,
    "filtered_data.csv",
    "text/csv"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🌍 Carbon Emission Impact Analysis Dashboard")
st.caption("Industry-Level ESG & Sustainability Analytics Dashboard")

# -----------------------------
# KPI SECTION
# -----------------------------
avg_co2 = filtered_df['co2_per_capita'].mean()
avg_renewable = filtered_df['renewable_energy'].mean()
avg_gdp = filtered_df['gdp'].mean()
avg_energy = filtered_df['energy_consumption'].mean()
total_countries = filtered_df['country'].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Avg CO₂", f"{avg_co2:.2f}")
col2.metric("Avg Renewable %", f"{avg_renewable:.2f}")
col3.metric("Avg GDP", f"{avg_gdp:,.0f}")
col4.metric("Avg Energy", f"{avg_energy:.2f}")
col5.metric("Countries", total_countries)

st.markdown("---")

# -----------------------------
# DYNAMIC METRIC CHARTS
# -----------------------------
trend_data = (
    filtered_df.groupby('year')[metric]
    .mean()
    .reset_index()
)

top_countries = (
    filtered_df.groupby('country')[metric]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.line(
    trend_data,
    x='year',
    y=metric,
    title=f"{metric.replace('_', ' ').title()} Trend Over Time"
)

fig2 = px.bar(
    top_countries,
    x='country',
    y=metric,
    title=f"Top 10 Countries by {metric.replace('_', ' ').title()}"
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# SCATTER PLOTS
# -----------------------------
fig3 = px.scatter(
    filtered_df,
    x='renewable_energy',
    y='co2_per_capita',
    hover_name='country',
    title="Renewable Energy vs CO₂"
)

fig4 = px.scatter(
    filtered_df,
    x='gdp',
    y='co2_per_capita',
    hover_name='country',
    title="GDP vs CO₂ Emissions"
)

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# ENERGY TREND + MAP
# -----------------------------
energy_trend = (
    filtered_df.groupby('year')['energy_consumption']
    .mean()
    .reset_index()
)

fig5 = px.line(
    energy_trend,
    x='year',
    y='energy_consumption',
    title="Global Energy Consumption Trend"
)

latest_year = filtered_df['year'].max()

map_df = filtered_df[
    filtered_df['year'] == latest_year
]

fig6 = px.choropleth(
    map_df,
    locations='country_code',
    color='co2_per_capita',
    hover_name='country',
    color_continuous_scale='Reds',
    title=f"Global CO₂ Emissions Map ({latest_year})"
)

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# SUSTAINABILITY TABLE
# -----------------------------
st.subheader("Top Sustainable Countries")

sustainable = (
    filtered_df.groupby('country')
    .agg({
        'renewable_energy': 'mean',
        'co2_per_capita': 'mean',
        'energy_consumption': 'mean'
    })
    .reset_index()
)

sustainable = sustainable[
    sustainable['renewable_energy'] > 50
]

sustainable = sustainable.sort_values(
    by='co2_per_capita',
    ascending=True
).head(10)

st.dataframe(
    sustainable,
    use_container_width=True
)

# -----------------------------
# BUSINESS RECOMMENDATIONS
# -----------------------------
with st.expander("Business Recommendations"):
    st.markdown("""
    - Increase renewable energy investment
    - Reduce fossil fuel dependency
    - Improve industrial energy efficiency
    - Use forecasting for sustainability planning
    - Benchmark sustainability leaders
    - Support ESG reporting initiatives
    """)