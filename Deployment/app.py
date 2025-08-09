import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="Agricultural Suitability Predictor")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("merged_data.csv")

df = load_data()

st.title("🌾 Agricultural Suitability Predictor")

# Input crop and county
crop_list = sorted(df["crop_name"].unique())
county_list = sorted(df["NAME2_"].unique())

col1, col2 = st.columns(2)
with col1:
    selected_crop = st.selectbox("Select Crop", crop_list)
with col2:
    selected_county = st.selectbox("Select County", county_list)

# Filter
result = df[(df["crop_name"] == selected_crop) & (df["NAME2_"] == selected_county)]

st.markdown("### 🌍 Results")

if not result.empty:
    row = result.iloc[0]
    st.write(f"**County:** {selected_county}")
    st.write(f"**Crop:** {selected_crop}")
    st.write(f"**Mean Rainfall:** {row['rainfall']:.2f} mm")
    st.write(f"**Mean pH:** {row['pH']:.2f}")

    if row['suitable'] == 1:
        st.success("✅ This crop is **suitable** for the selected county.")
    else:
        st.error("❌ This crop is **not suitable** for the selected county.")
else:
    st.warning("No data found for the selected crop and county.")

# Optional: Show raw data
with st.expander("🔍 View Raw Data"):
    st.dataframe(df[['crop_name', 'NAME2_', 'rainfall', 'pH', 'suitable']])
