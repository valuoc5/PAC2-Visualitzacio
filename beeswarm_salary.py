import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spoty_dataset.csv")

# Select columns
df = df[["track_name","popularity","track_genre"]]

# Remove NA
df = df.dropna()

# Reduce size
df = df.sample(600)

# Keep top genres
top_genres = df["track_genre"].value_counts().head(8).index
df = df[df["track_genre"].isin(top_genres)]

# Plot
plt.figure(figsize=(12,7))

sns.swarmplot(
    data=df,
    x="popularity",
    y="track_genre",
    size=4
)

plt.title("Spotify Song Popularity by Genre (Beeswarm Plot)")
plt.xlabel("Popularity")
plt.ylabel("Genre")

plt.tight_layout()

plt.savefig("beeswarm_spotify.png", dpi=300)
plt.show()