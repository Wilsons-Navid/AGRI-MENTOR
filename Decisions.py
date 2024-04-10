print("Welcome to AgriMentor! This is a Soil Monitoring Application for Smallholder Farmers.")
print("We will collect and analyze data from IoT sensors to monitor soil conditions and provide personalized crop recommendations.")
print("Let's get started!")

class WeatherAPI:
    @staticmethod
    def get_forecast():
        precipitation = float(input("Enter current precipitation level: "))
        temperature = float(input("Enter current temperature: "))
        humidity = float(input("Enter current humidity: "))
        return {"precipitation": precipitation, "temperature": temperature, "humidity": humidity}

class MarketAPI:
    @staticmethod
    def get_crop_prices():
        # Returns a dictionary of crop prices
        return {
            "maize": 10000,
            "rice": 8000,
            "wheat": 12000
        }

    @staticmethod
    def get_demand_trends():
        # Returns a dictionary of crop demand trends
        return {
            "maize": "high",
            "rice": "medium",
            "wheat": "low"
        }

def get_soil_moisture():
    # Retrieves the current soil moisture level from the user
    return float(input("Enter current soil moisture level: "))

def get_soil_acidity():
    # Retrieves the current soil acidity level from the user
    return float(input("Enter current soil acidity level: "))

def collect_soil_data():
    # Collects soil data from the user
    soil_moisture = get_soil_moisture()
    soil_acidity = get_soil_acidity()
    return soil_moisture, soil_acidity

def fetch_weather_forecast():
    # Fetches the weather forecast using an external WeatherAPI
    forecast = WeatherAPI.get_forecast()
    return forecast

def analyze_market_trends():
    # Retrieves crop prices and demand trends from an external MarketAPI
    crop_prices = MarketAPI.get_crop_prices()
    demand_trends = MarketAPI.get_demand_trends()
    return crop_prices, demand_trends

def decision_support_system():
    soil_moisture, soil_acidity = collect_soil_data()
    weather_forecast = fetch_weather_forecast()
    crop_prices, demand_trends = analyze_market_trends()

    crops_in_mind = input("Do you have specific crops in mind? (Yes/No): ").lower()
    recommended_crops = []

    if crops_in_mind == "yes":
        crops_list = input("Enter the crops you have in mind (comma-separated): ").lower().split(",")
        for crop in crops_list:
            if crop in crop_prices:
                if soil_moisture < soil_acidity and weather_forecast["precipitation"] > soil_acidity:
                    recommended_crops.append("Drought-resistant " + crop)
                if crop_prices[crop] > crop_prices["rice"]:
                    recommended_crops.append(crop)
            else:
                print(f"{crop} is not in the available crop data.")
    else:
        for crop in crop_prices:
            if soil_moisture < soil_acidity and weather_forecast["precipitation"] > soil_acidity:
                recommended_crops.append("Drought-resistant " + crop)
            if crop_prices[crop] > crop_prices["rice"]:
                recommended_crops.append(crop)

    if len(recommended_crops) > 0:
        recommendation = f"Consider planting {', '.join(recommended_crops)} based on the available data."
    else:
        recommendation = "Monitor soil conditions and market trends for optimal decision-making."

    return recommendation

if __name__ == "__main__":
    # Entry point of the script
    recommendation = decision_support_system()
    print("Recommendation:", recommendation)
    print("Thank you for using AGRI-MENTOR! We hope our recommendations are helpful for your farming decisions.")





