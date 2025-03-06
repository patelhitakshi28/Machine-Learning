import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

base_url = 'https://www.yelp.de/search?find_desc=Restaurants&find_loc=Stuttgart%2C+Baden-W%C3%BCrttemberg'

name = []
rating = []
reviews = []
image = []

for page in range (0, 230, 10): 
    url = base_url if page == 0 else f"{base_url}&start={page}"
    response = requests.get(url, headers= headers).text
    soup = BeautifulSoup(response, 'lxml')
    hotels= soup.find_all('div', class_='y-css-pwt8yl')

    for i in hotels:
        # Extract hotel name and remove non-breaking spaces
        name.append(i.find('h3').text.strip().replace('\xa0', ' '))

        # Extract rating (first occurrence of <span> with class)
        rating.append(i.find('span', class_="y-css-1ugd8yy").text.strip() if i.find('span', class_="y-css-1ugd8yy") else None)
    
        # Extract number of reviews (first occurrence of <span> with class)
        reviews.append(i.find('span', class_="y-css-1d8mpv1").text.strip() if i.find('span', class_="y-css-1d8mpv1") else None)

        # Extract image URL
        image.append(i.find('img', class_="y-css-fex5b")['src'] if i.find('img', class_="y-css-fex5b") else None)


d= {'name': name, 'rating':rating, 'reviews':reviews, 'image': image}

df= pd.DataFrame(d)

df.to_csv('yelp_restaurants.csv', index=False, encoding='utf-8')
print("✅ Data saved to yelp_restaurants.csv successfully!")