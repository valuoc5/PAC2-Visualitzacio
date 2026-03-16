import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("nobel_laureates_data.csv")

# Keep relevant columns
df = df[["year","category","fullName","motivation"]]

# Remove missing values
df = df.dropna()

# Sample to keep visualization readable
df = df.sample(150)

# Create timeline
fig = px.scatter(
    df,
    x="year",
    y="category",
    color="category",
    hover_name="fullName",
    hover_data=["motivation"],
    title="Nobel Prize Laureates Timeline"
)

fig.update_layout(
    height=600
)

# Save HTML for GitHub Pages
fig.write_html("timeline_nobel.html")

fig.show()