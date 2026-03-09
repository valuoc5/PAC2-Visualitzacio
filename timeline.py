import requests
import pandas as pd
import plotly.express as px

# Get real dataset from SpaceX API
url = "https://api.spacexdata.com/v4/launches"
data = requests.get(url).json()

# Extract relevant fields
launches = []
for launch in data:
    launches.append({
        "Mission": launch["name"],
        "Date": launch["date_utc"],
        "Success": "Success" if launch["success"] else "Failure"
    })

df = pd.DataFrame(launches)

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Create timeline-like scatter
fig = px.scatter(
    df,
    x="Date",
    y="Mission",
    color="Success",
    title="Timeline of SpaceX Launches",
    hover_data=["Date"]
)

fig.update_layout(
    height=700,
    xaxis_title="Year",
    yaxis_title="Mission"
)

# Save interactive visualization
fig.write_html("timeline_spacex_real.html", include_plotlyjs="cdn")

print("Timeline generated: timeline_spacex_real.html")