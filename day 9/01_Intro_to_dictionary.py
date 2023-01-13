programing_dictionary = {
    "Bug": "A error in program that prevents the program from running", 
    "Function": "A piece of code that you can easily call over and over again",
}
#To call an item from a dictionary
print(programing_dictionary["Bug"])

#To add another item to the dictionary
programing_dictionary["Loop"] = "To do a task over and over again"

#To create an empty dictionary
empty_dictionary = {}

#To wipe a entire dictionary
programing_dictionary = {}

#To edit an item in the dictionary
programing_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

#nesting a list in dict
travel_log = {
    "france": ["paris", "lille", "lyon"],
    "germany": ["stuttgart", "berlin", "munich"]
}
#nesting a dict in dict
cities_visited = {
    "france": {
        "Paris": "4 days",
        "lille": "3 days",
        "lyon": "2 days",
    }
}

travel_log = {
    "france": {"cities visited": ["paris", "lens", "lille"]}, "Total visits": "12 Days",
    "Germany": {"cities visited":["munich", "dortmund", "berlin"]},"Total visits": "8 Days"
}

#nesting a dict in list
travel_log = [
    {
        "Country visited": "France",
        "cities visited": ["Paris", "Lens", "Lille"],
        "Total visits": "12 Days"
    }
]