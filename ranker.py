import pandas as pd

# Load dataset
df = pd.read_csv("Top_Indian_Places_to_Visit.csv")

def rank_weekend_places(source_city, top_n=5):

    # Remove the source city
    filtered_df = df[df["City"].str.lower() != source_city.lower()]

    # Aggregate city-wise data
    city_stats = filtered_df.groupby(["City", "State"]).agg(
        avg_rating=("Google review rating", "mean"),
        popularity=("Number of google review in lakhs", "sum"),
        avg_time=("time needed to visit in hrs", "mean")
    ).reset_index()

    # Compute ranking score
    city_stats["score"] = (
        city_stats["avg_rating"]
        + city_stats["popularity"]
        - city_stats["avg_time"]
    )

    return city_stats.sort_values("score", ascending=False).head(top_n)


if __name__ == "__main__":
    source_city = input("Enter source city: ")
    print(f"\nTop weekend destinations from {source_city}:")
    print(rank_weekend_places(source_city))
