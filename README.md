# Travel-Advisory

# Travel Advisory System

## Introduction
Welcome to the Travel Advisory System! This Python script offers travel recommendations, allows the addition of new destinations, and facilitates user feedback for existing destinations. The system considers various user preferences such as budget, weather, activities, rating, transportation, cellular connectivity, cuisine, and language.

## Knowledge Base
The system's knowledge base includes information about several destinations, each having attributes such as budget, weather, activities, rating, feedback, transportation, cellular connectivity, cuisine, and language.

## Usage

1. **Get Travel Recommendation**
   - Enter your preferences when prompted, including budget, weather, activities, rating, transportation, cellular connectivity, cuisine, and language.
   - The system will provide recommendations based on your preferences.

2. **Add New Destination**
   - Select this option to add a new destination to the knowledge base.
   - Enter details such as name, budget range, weather, activities, rating, feedback, transportation, cellular connectivity, cuisine, and language.

3. **Add Feedback for a Destination**
   - Provide feedback for an existing destination by entering the destination's name, rating, and comments.

4. **Check Feedback for a Destination**
   - Enter the destination's name to check existing feedback and ratings.

5. **Exit**
   - Choose this option to exit the Travel Advisory System.

## Functions

1. **`recommend_destination(user_preferences, destinations)`**
   - Recommends destinations based on user preferences.
   - Takes into account budget, weather, activities, rating, transportation, cellular connectivity, cuisine, and language.

2. **`add_new_destination(destinations)`**
   - Adds a new destination to the knowledge base.
   - Gathers information from the user about the new destination.

3. **`add_feedback(destination_list, destination_name)`**
   - Adds feedback for an existing destination.
   - Prompts the user to enter a rating and comments for the specified destination.

4. **`check_feedback(destination_name)`**
   - Checks existing feedback for a specified destination.
   - Displays feedback and ratings if available.

## Note
- The script uses a knowledge base of destinations stored in memory.
- Users can interact with the system by choosing options from the menu.
- Ensure valid inputs for numeric fields such as budget, rating, and feedback.
- The script will continue running until the user chooses to exit.

Feel free to explore, discover new destinations, provide feedback, and enjoy your virtual travel experience!
