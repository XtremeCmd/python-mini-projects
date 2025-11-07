from functools import reduce

# Example dataset
songs = [
    {"title": "Afterglow", "artist": "Ed Sheeran", "duration_min": 3.5, "rating": 4.8},
    {"title": "Blinding Lights", "artist": "The Weeknd", "duration_min": 4.1, "rating": 4.7},
    {"title": "Dance Monkey", "artist": "Tones and I", "duration_min": 3.3, "rating": 3.9},
    {"title": "Peaches", "artist": "Justin Bieber", "duration_min": 3.0, "rating": 4.2},
    {"title": "Levitating", "artist": "Dua Lipa", "duration_min": 3.8, "rating": 4.6},
]

# Convert all durations from minutes → seconds
songs_in_seconds = list(map(
    lambda s: {**s, "duration_sec": round(s["duration_min"] * 60)},
    songs
))

# Filter songs by a minimum rating threshold
min_rating = float(input("Enter minimum rating (e.g. 4.5): ") or 4.5)
top_songs = list(filter(lambda s: s["rating"] >= min_rating, songs_in_seconds))

# Sort filtered songs by rating (descending)
sorted_playlist = sorted(top_songs, key=lambda s: s["rating"], reverse=True)

# Format the results neatly using list comprehension
formatted_playlist = [
    f"{i+1}. {s['title']} by {s['artist']} - {s['duration_sec']} sec rating: {s['rating']}"
    for i, s in enumerate(sorted_playlist)
]

# Compute total playlist duration using reduce()
total_duration = reduce(lambda acc, s: acc + s["duration_sec"], sorted_playlist, 0)

# Convert total seconds → minutes:seconds
minutes, seconds = divmod(total_duration, 60)

# Display results
print("\n Filtered Playlist (Top Rated) \n")
if formatted_playlist:
    print("\n".join(formatted_playlist))
    print(f"\nTotal Playlist Duration: {total_duration} seconds (~{minutes} min {seconds} sec)")
else:
    print("No songs matched your rating criteria.")
