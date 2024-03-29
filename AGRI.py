# Welcome message and app information
print("Welcome to AgriMentor! This is a Soil Monitoring Application for Smallholder Farmers.")
print("We will collect and analyze data from IoT sensors to monitor soil conditions and provide personalized crop recommendations.")
print("Let's get started!")

# Prompt user to enter sensor data
acidity = float(input("Please enter the acidity level of the soil: "))
moisture = float(input("Please enter the moisture level of the soil: "))

# Prompt user for specific crops
specific_crops = input("Do you have any specific crop in mind? (Y/N): ")
7
if specific_crops.upper() == "Y":
    crops = input("Please enter the crops you want to plant, separated by commas: ")
    crop_list = crops.split(",")
else:
    crop_list = ['beans', 'wheat', 'corn', 'potato', 'tomato', 'carrot', 'lettuce', 'cabbage', 'onion', 'pepper',
             'strawberry', 'rice', 'barley', 'soybeans', 'peanut', 'oats', 'sunflower', 'sugarcane', 'coffee', 'cotton']
# Analyze data based on conditions and market trends
market_trends_good = True  # Placeholder value, you would need to implement the logic to determine market trends

if acidity < 6.5 and moisture > 0.3 and market_trends_good:
    # Display profitable crop recommendations
    print("Based on the soil conditions and market trends, the following crops are recommended:")
    for crop in crop_list:
        print("- " + crop)
else:
    # Conditions not favorable for planting
    print("Sorry, the current soil conditions and market trends are not favorable for planting.")

# Thank the user for using the platform
print("Thank you for using AgriMentor! We hope our recommendations were helpful.")