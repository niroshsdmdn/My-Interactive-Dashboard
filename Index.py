import streamlit as st
import plotly.graph_objects as go


# ---------------------------------------------------
# Page configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Interactive Dashboard",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------
# Data
# ---------------------------------------------------
def get_data(dataset):
    if dataset == "Dataset 1":
        return {
            "x": ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
            "y": [12, 19, 3, 5, 2, 3]
        }

    elif dataset == "Dataset 2":
        return {
            "x": ["Apples", "Oranges", "Bananas", "Grapes", "Pineapples", "Mangoes"],
            "y": [15, 10, 13, 7, 8, 5]
        }


# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("Welcome to My Interactive Dashboard")

st.header("Dashboard")


# ---------------------------------------------------
# Dataset dropdown
# ---------------------------------------------------
dataset = st.selectbox(
    "Select Dataset:",
    ["Dataset 1", "Dataset 2"]
)


# ---------------------------------------------------
# Get selected dataset
# ---------------------------------------------------
data = get_data(dataset)


# ---------------------------------------------------
# Create Plotly chart
# ---------------------------------------------------
fig = go.Figure(
    data=[
        go.Bar(
            x=data["x"],
            y=data["y"]
        )
    ]
)

fig.update_layout(
    title="Interactive Bar Chart",
    xaxis_title="Categories",
    yaxis_title="Values",
    height=400
)


# ---------------------------------------------------
# Display chart
# ---------------------------------------------------
st.plotly_chart(
    fig,
    use_container_width=True
)


# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;'>"
    "&copy; 2024 My Interactive Dashboard. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)