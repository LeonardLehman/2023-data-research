import folium
from geopy.geocoders import Nominatim



# List of city names
cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Rome', 'Cairo', 'Moscow', 'Beijing', 'Rio de Janeiro']

# Initialize the geocoder
geolocator = Nominatim(user_agent='city_plotter')

# Create an empty map centered on the world
map_plot = folium.Map(location=[0, 0], zoom_start=2)

# Plot the cities on the map
for city in cities:
    # Geocode the city coordinates
    location = geolocator.geocode(city)
    if location:
        # Add a marker for the city
        folium.Marker(location=[location.latitude, location.longitude], popup=city).add_to(map_plot)

# Display the map
map_plot.save('2023-data-research\Assignments\Proposal\city_map.html')  # Save the map as an HTML file
map_plot


"""import snscrape.modules.twitter as  sntwitter
import pandas as pd

query = "protest"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    if len(tweet) == limit:
        break
    else:
        tweets.append(tweet.date, tweet.user.username, tweet.content)

df = pd.DataFrame(tweets, columns=["Date", 'User', "Content"])
"""

