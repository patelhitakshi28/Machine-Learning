import requests
import pandas as pd  

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZjlmM2U4YjkzY2ZkMGUyNTllMjUxYmEzMTYwMjcwZSIsIm5iZiI6MTczOTI3NDQzNy45MDQsInN1YiI6IjY3YWIzOGM1NDcwNTFjNTRiZWIwYWU4YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.paCsVNHGlow2P5T7J1fCW-mbVsPW096WWweSiQsh3e0"
}

empty_df = pd.DataFrame()  

for i in range(1, 502):  
    response = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={i}", headers=headers)
    
    if response.status_code == 200:  
        data = response.json()  
        results = data.get("results", [])  

        if results:  
            temp_df = pd.DataFrame(results)[["id", "title", "overview", "release_date", "popularity", "vote_average", "vote_count"]]
            empty_df = pd.concat([empty_df, temp_df], ignore_index=True)  
    else:
        print(f"Failed to fetch page {i}, Status Code: {response.status_code}")

print(empty_df)
print(empty_df.shape)

empty_df.to_csv('movies.csv')