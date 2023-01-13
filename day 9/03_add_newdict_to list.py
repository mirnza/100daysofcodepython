travel_log = [
    {
        "Country visited": "France",
        "cities visited": ["Paris", "Lens", "Lille"],
        "Total visits": "12 Days"
    },
    {
        "Country visited": "Germany",
        "cities visited": ["Stuttgart", "Munich", "Berlin"],
        "Total visits": "8 Days"
    }
]

def add_new_country(country, cities, days):
    new_country = {
        "Country visited": country,
        "Cities visited": cities,
        "Total visits": days
    }
    travel_log.append(new_country)

country_visited = input("Enter the country you visited: \n")
cities_visited = input("Enter the cities you visited using ',': \n")
l_cities_visited = cities_visited.split(',')
Total_visits = input("enter the days you visited the country for: \n")
add_new_country(country= country_visited,cities=l_cities_visited, days= Total_visits)
print(travel_log)
