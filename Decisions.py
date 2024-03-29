#Creating class Weather API with a function getforest();
class WeatherAPI:
    @staticmethod
    def get_forecast():
        precipitation = float(input("Enter current precipitation level: "))  
        temperature = float(input("Enter current temperature: "))  
        humidity = float(input("Enter current humidity: ")) 
        return {"precipitation": precipitation, "temperature": temperature, "humidity": humidity}
#Market API  class to get market trends
class MarketAPI:
    @staticmethod
    def get_crop_prices():
        return {"maize": 10000, "rice": 8000, "wheat": 12000}  

    @staticmethod
    def get_demand_trends():
        return {"maize": "high", "rice": "medium", "wheat": "low"}  
#
def get_soil_moisture():
    return float(input("Enter current soil moisture level: "))  

def get_soil_acidity():
    return float(input("Enter current soil acidity level: "))  
#collecting the soil and acidity from the function
def collect_soil_data():
    soil_moisture = get_soil_moisture() 
    soil_acidity = get_soil_acidity()    
    return soil_moisture, soil_acidity

def fetch_weather_forecast():
    forecast = WeatherAPI.get_forecast()
    return forecast

def analyze_market_trends():
    crop_prices = MarketAPI.get_crop_prices()
    demand_trends = MarketAPI.get_demand_trends()
    return crop_prices, demand_trends

def decision_support_system():
    soil_moisture, soil_acidity = collect_soil_data()
    weather_forecast = fetch_weather_forecast()
    crop_prices, demand_trends = analyze_market_trends()
# providing recommendation base on data collected
    if soil_moisture < soil_acidity and weather_forecast["precipitation"] > soil_acidity:
        recommendation = "Consider planting drought-resistant crops."
    elif crop_prices["maize"] > crop_prices["rice"]:
        recommendation = "Consider planting maize due to higher market prices."
    else:
        recommendation = "Monitor soil conditions and market trends for optimal decision-making."

    return recommendation
# return the recommendation
if __name__ == "__main__":
    recommendation = decision_support_system()
    print("Recommendation:", recommendation)
