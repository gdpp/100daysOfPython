programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Empty dictionary
empty_dict = {}

# Edit item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)


# loop through a dictionary
for key in programming_dictionary:
    print(f'{key}')


# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3
    },
    "Mexico": {
        "cities_visited": ["Guadalajara", "Monterrey", "CDMX" ],
        "total_visits": 24
    } 
}

travel_log_v2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3
    },
    {
        "country": "Mexico",
        "cities_visited": ["Guadalajara", "Monterrey", "CDMX" ],
        "total_visits": 24
    } 
]
