import sys

max_integer = sys.maxsize

# Knowledge Base
destinations = [
    {
        "name": "Manali",
        "budget": [8000, 12000],
        "weather": "Mild",
        "activities": ["valley", "Pass", "Mountains", "Old Manali"],
        "rating": 8.8,
        "feedback": ["Beautiful place!", "Great for adventure seekers."],
        "transportation": ["Airport", "Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Hindi", "Himachali"]
    },
    {
        "name": "Rann of Kutch",
        "budget": [15000, 20000],
        "weather": "Varied",
        "activities": ["Desert", "Kala Dungar", "Villages"],
        "rating": 8.5,
        "feedback": ["Unique landscape!", "Good cultural experience."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Limited Cellular Network"],
        "cuisine": "Mostly Veg",
        "language": ["Gujarati", "Hindi"]
    },
    {
        "name": "Ooty",
        "budget": [9000, 14000],
        "weather": "Mild",
        "activities": ["Gardens", "Mountain Railway", "Lake", "Mountains"],
        "rating": 8.6,
        "feedback": ["Scenic beauty!", "Relaxing atmosphere."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Tamil", "English"]
    },
    {
        "name": "Ladakh",
        "budget": [14000, 18000],
        "weather": "Cold",
        "activities": ["Lake", "Valley", "Monasteries", "Mountains"],
        "rating": 9.0,
        "feedback": ["Breathtaking landscapes!", "Spiritual experience."],
        "transportation": ["Airport"],
        "cellular_connectivity": ["Limited Cellular Network"],
        "cuisine": "Mostly Non-Veg",
        "language": ["Ladakhi", "Tibetan", "Hindi"]
    },
    {
        "name": "Auroville",
        "budget": [4000, 7000],
        "weather": "Tropical",
        "activities": ["Matrimandir", "Beach", "Sri Aurobindo Ashram"],
        "rating": 8.7,
        "feedback": ["Spiritual haven!", "Relaxing beach."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["English", "Tamil", "French"]
    },
    {
        "name": "Hampi",
        "budget": [18000, 22000],
        "weather": "Hot",
        "activities": ["Temple", "Hill", "Bazaar", "Mountains"],
        "rating": 8.5,
        "feedback": ["Historical marvel!", "Unique landscape."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Limited Cellular Network"],
        "cuisine": "Both",
        "language": ["Kannada", "English"]
    },
    {
        "name": "Haridwar",
        "budget": [5000, 10000],
        "weather": "Varied",
        "activities": ["Ghat", "Temple", "Mountains"],
        "rating": 8.0,
        "feedback": ["Spiritual experience!", "Holy city."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Limited Cellular Network"],
        "cuisine": "Mostly Veg",
        "language": ["Hindi"]
    },
    {
        "name": "Khajuraho",
        "budget": [20000, 25000],
        "weather": "Varied",
        "activities": ["Temples", "Light and Sound Show", "National Park"],
        "rating": 8.8,
        "feedback": ["Architectural marvel!", "Historical significance."],
        "transportation": ["Airport"],
        "cellular_connectivity": ["Wi-Fi", "Limited Cellular Network"],
        "cuisine": "Both",
        "language": ["Hindi", "English"]
    },
    {
        "name": "Munnar",
        "budget": [24000, 30000],
        "weather": "Mild",
        "activities": ["Tea Gardens", "National Park", "Peak"],
        "rating": 8.9,
        "feedback": ["Picturesque landscapes!", "Serene atmosphere."],
        "transportation": ["Airport"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Malayalam", "English"]
    },
    {
        "name": "Pondicherry",
        "budget": [10000, 15000],
        "weather": "Tropical",
        "activities": ["French Quarter", "Beach", "Sri Aurobindo Ashram"],
        "rating": 8.6,
        "feedback": ["French vibes!", "Relaxing beach."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Tamil", "English", "French"]
    },
    {
        "name": "Coorg",
        "budget": [7000, 10000],
        "weather": "Mild",
        "activities": ["Plantations", "Falls", "Talakaveri"],
        "rating": 8.7,
        "feedback": ["Coffee paradise!", "Waterfalls are stunning."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Limited Cellular Network"],
        "cuisine": "Both",
        "language": ["Kannada", "English"]
    },
    {
        "name": "Jaisalmer",
        "budget": [10000, 14000],
        "weather": "Hot",
        "activities": ["Fort", "Sand Dunes", "Haveli"],
        "rating": 8.4,
        "feedback": ["Golden city!", "Camel safari is a must."],
        "transportation": ["Airport"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Hindi", "English"]
    },
    {
        "name": "Andaman and Nicobar Islands",
        "budget": [45000, 55000],
        "weather": "Tropical",
        "activities": ["Beach", "Diving", "Jail", "Historical Importance"],
        "rating": 9.1,
        "feedback": ["Paradise on earth!", "Crystal clear waters."],
        "transportation": ["Airport"],
        "cellular_connectivity": ["Limited Cellular Network"],
        "cuisine": "Both",
        "language": ["Hindi", "English"]
    },
    {
        "name": "Pushkar",
        "budget": [6000, 9000],
        "weather": "Varied",
        "activities": ["Lake", "Temple", "Fair"],
        "rating": 8.6,
        "feedback": ["Spiritual vibe!", "Camel fair is unique."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Limited Cellular Network"],
        "cuisine": "Both",
        "language": ["Hindi", "English"]
    },
    {
        "name": "Mahabalipuram",
        "budget": [12000, 18000],
        "weather": "Tropical",
        "activities": ["Temple", "Rathas", "Beach"],
        "rating": 8.5,
        "feedback": ["Architectural marvel!", "Beach vibes."],
        "transportation": ["Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Tamil", "English"]
    },
    {
        "name": "Kodaikanal",
        "budget": [8000, 12000],
        "weather": "Mild",
        "activities": ["Lake", "Walk", "Park"],
        "rating": 8.7,
        "feedback": ["Stunning landscapes!", "Pleasant climate."],
        "transportation": ["Airport", "Railway"],
        "cellular_connectivity": ["Wi-Fi", "Cellular Network"],
        "cuisine": "Both",
        "language": ["Tamil", "English"]
    }
]



def recommend_destination(user_preferences, destinations):

    filtered_destinations = []
  
    user_budget = user_preferences.get("budget", [max_integer])
    # print(user_budget[0])
    
   
    for d in destinations:
        # Check if the user's budget falls within the budget range of each destination
        if (d["budget"][0]) <= user_budget[0] <= (d["budget"][1]):
            filtered_destinations.append(d)
        elif(d["budget"][1] <= user_budget[0]):
            filtered_destinations.append(d)
    

    # Remove duplicates from filtered_destinations based on 'name' key
    unique_destinations = []
    seen_names = set()

    for destination in filtered_destinations:
        name = destination['name']
        if name not in seen_names:
            unique_destinations.append(destination)
            seen_names.add(name)
    # filtered_destinations now contains unique destinations based on 'name'
    filtered_destinations = unique_destinations
    
    # print("Budget:")
    # for destination in filtered_destinations:
    #     print(destination["name"])

    # Check user's weather preference
    weather_preference = user_preferences.get("weather", "n/a")
    if weather_preference != "n/a":
        filtered_destinations = [d for d in filtered_destinations if d["weather"].lower() == weather_preference.lower()]

    # Remove duplicates from filtered_destinations based on 'name' key
    unique_destinations = []
    seen_names = set()

    for destination in filtered_destinations:
        name = destination['name']
        if name not in seen_names:
            unique_destinations.append(destination)
            seen_names.add(name)
    # filtered_destinations now contains unique destinations based on 'name'
    filtered_destinations = unique_destinations
    # print("Weather:")
    # for destination in filtered_destinations:
    #     print(destination["name"])

    # Check user's activity preference
    activity_preference = user_preferences.get("activities", "n/a")
    # print(activity_preference)
    updated_destinations = []

    if activity_preference != "n/a":
        for destination in filtered_destinations:
            destination_activities = destination.get("activities", [])
            # print(destination_activities)
            if any(activity.lower() in [a.lower() for a in destination_activities] for activity in activity_preference):
                updated_destinations.append(destination)
        print(updated_destinations)
        filtered_destinations = updated_destinations


        
    # print("Activities:")
    # for destination in filtered_destinations:
    #     print(destination["name"])

    # Check user's ratings preference
    min_rating = user_preferences.get("min_rating", 0)
    max_rating = user_preferences.get("max_rating", 10)
    if min_rating != "n/a" and max_rating != "n/a":
        filtered_destinations = [d for d in filtered_destinations if min_rating <= d["rating"] <= max_rating]
    elif min_rating == "n/a" and max_rating == "n/a":
        pass  # do nothing
    elif min_rating == "n/a":
        filtered_destinations = [d for d in filtered_destinations if d["rating"] <= max_rating]
    elif max_rating == "n/a":
        filtered_destinations = [d for d in filtered_destinations if min_rating <= d["rating"] <= 10]

    # print("ratings")
    # for destination in filtered_destinations:
    #    print(destination["name"])
    
    # Check user's transportation preference
    transportation_preference = user_preferences.get("transportation", "n/a")
    if transportation_preference != "n/a":
        filtered_destinations = [d for d in filtered_destinations if transportation_preference.lower() in [l.lower() for l in d["transportation"]]]
    # print("trans")
    # for destination in filtered_destinations:
    #     print(destination["name"])


    # Check user's cellular connectivity preference
    cellular_connectivity_preference = user_preferences.get("cellular_connectivity", "n/a")
    if cellular_connectivity_preference != "n/a":
        filtered_destinations = [d for d in filtered_destinations if cellular_connectivity_preference.lower() in [l.lower() for l in d["cellular_connectivity"]]]
    # print("cellular connectivity")
    # for destination in filtered_destinations:
    #    print(destination["name"])

    # Check user's cuisine preference
    cuisine_preference = user_preferences.get("cuisine", "n/a")
    if cuisine_preference != "n/a":
        filtered_destinations = [d for d in filtered_destinations if cuisine_preference.lower() == d["cuisine"].lower()]
    
    # print("cuisine")
    # for destination in filtered_destinations:
    #    print(destination["name"])

    # Check users' language preference
    language_preference = user_preferences.get("language", "n/a")
    if language_preference != "n/a":
        for language in language_preference:
            filtered_destinations = ([d for d in filtered_destinations if language.lower() in [l.lower() for l in d["language"]]])
    # print("language")
    # for destination in filtered_destinations:
    #    print(destination["name"])


    

    # Remove duplicates from filtered_destinations based on 'name' key
    unique_destinations = []
    seen_names = set()

    for destination in filtered_destinations:
        name = destination['name']
        if name not in seen_names:
            unique_destinations.append(destination)
            seen_names.add(name)

    # filtered_destinations now contains unique destinations based on 'name'
    filtered_destinations = unique_destinations

    return filtered_destinations

# Function to add a new destination
def add_new_destination(destinations):
    # Gather information from the user about the new destination
    print("Add a New Destination:")
    name = input("Enter the name of the destination: ")
    budget_min = float(input("Enter the minimum budget: ") or 0)
    budget_max = float(input("Enter the maximum budget (press Enter to skip): ") or float("inf"))
    weather = input("Enter the preferred weather condition (press Enter to skip): ") or "n/a"
    activities = input("Enter activities you can enjoy (comma-separated, press Enter to skip): ").split(",") or []
    rating = float(input("Enter the rating for this destination (press Enter to skip): ") or 0)
    feedback = []  # You can add feedback functionality if needed in the future
    connectivity = input("Enter connectivity options (comma-separated, press Enter to skip): ").split(",") or []
    transportation = input("Enter transportation options (press Enter to skip): ") or "n/a"
    cellular_connectivity = input("Enter cellular connectivity options (press Enter to skip): ") or "n/a"
    cuisine = input("Enter cuisine options (press Enter to skip): ") or "n/a"
    language = input("Enter languages spoken (comma-separated, press Enter to skip): ").split(",") or []

    # Create a new destination dictionary
    new_destination = {
        "name": name,
        "budget": [budget_min, budget_max],
        "weather": weather,
        "activities": activities,
        "rating": rating,
        "feedback": feedback,
        "connectivity": connectivity,
        "transportation": transportation,
        "cellular_connectivity": cellular_connectivity,
        "cuisine": cuisine,
        "language": language
    }

    # Add the new destination to the list
    destinations.append(new_destination)

    print(f"Destination '{name}' has been added!")



# Function to add feedback to a destination
def add_feedback(destination_list, destination_name):
    for destination in destination_list:
        if destination["name"].lower() == destination_name:
            print(f"Adding Feedback for Destination: {destination_name}")
            rating = float(input("Enter the rating (0-10): "))
            comment = input("Enter your feedback comment: ")

            feedback = {
                "rating": rating,
                "feedback": comment
            }

            destination["feedback"].append(feedback)
            return

    print(f"Destination '{destination_name}' not found in the database.")

# Function to check feedback for a destination
def check_feedback(destination_name):
    for destination in destinations:
        if destination["name"].lower() == destination_name:
            return destination["feedback"]

# Main program
while True:
    print("Welcome to the Travel Advisory System!")
    print("1. Get Travel Recommendation")
    print("2. Add New Destination")
    print("3. Add Feedback for a Destination")
    print("4. Check Feedback for a Destination")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            user_preferences = {}
            
            budget_input = input("Enter your budget (Only Amount (please don't write units), press Enter to skip): ")
            user_preferences["budget"] = [float(budget_input)] if budget_input.strip() else [max_integer]
            
            weather_input = input("Enter your preferred weather (Like Mild/Varied/Cold/Tropical/Hot)(press Enter to skip): ")
            user_preferences["weather"] = weather_input.strip() or "n/a"
            
            activities_input = input("Enter activities you enjoy (Like Mountains, Falls, Valley) (comma-separated, press Enter to skip): ")
            user_preferences["activities"] = [activity.strip() for activity in activities_input.split(",")] if activities_input.strip() else "n/a"

            
            min_rating_input = input("Enter your minimum preferred rating (press Enter to skip): ")
            user_preferences["min_rating"] = float(min_rating_input) if min_rating_input.strip() else 0
            
            max_rating_input = input("Enter your maximum preferred rating (press Enter to skip): ")
            user_preferences["max_rating"] = float(max_rating_input) if max_rating_input.strip() else 10
            
            transportation_input = input("Enter your preferred transportation (Airport/Railway, press Enter to skip): ")
            user_preferences["transportation"] = transportation_input.strip() or "n/a"
            
            cellular_input = input("Enter your preferred cellular connectivity (Wi-Fi/Limited Cellular Network/Cellular Network, press Enter to skip): ")
            user_preferences["cellular_connectivity"] = cellular_input.strip() or "n/a"
            
            cuisine_input = input("Enter your preferred cuisine (Mostly Veg/Mostly Non-Veg/Both, press Enter to skip): ")
            user_preferences["cuisine"] = cuisine_input.strip() or "n/a"
            
            languages_input = input("Enter languages you prefer (comma-separated, press Enter to skip): ")
            user_preferences["language"] = languages_input.split(",") if languages_input.strip() else []

            recommended_destinations = recommend_destination(user_preferences, destinations)

            if not recommended_destinations:
                print("Sorry, no matches found based on your preferences.")
            else:
                print("Recommended Destinations based on your preferences:")
                for destination in recommended_destinations:
                    print(destination["name"])
        except ValueError:
            print("Error: Invalid data type entered. Please enter numeric values for budget and ratings.")




    
    elif choice == "2":
        add_new_destination(destinations)
    
    elif choice == "3":
        destination_name = input("Enter the destination you want to provide feedback for: ")
        add_feedback(destinations, destination_name.lower())
        print("Feedback added successfully!")
    
    elif choice == "4":
        destination_name = input("Enter the destination you want to check feedback for: ")
        feedback = check_feedback(destination_name.lower())
        if feedback:
            print("Feedback for", destination_name, ":")
            for idx, fb in enumerate(feedback, start=1):
                print(f"{idx}. {fb}")
        else:
            print("No feedback available for", destination_name)
    
    elif choice == "5":
        print("Thank you for using the Travel Advisory System!")
        break

    else:
        print("Invalid choice. Please try again.")