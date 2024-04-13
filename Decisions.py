import mysql.connector

#Establish Database Connection
def establish_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cavina@10",
            database="soil_monitoring"
        )
        return conn
    except mysql.connector.Error as err:
        print("Error:", err)
        return None

#Save Soil Data to Database
def save_soil_data(conn, soil_moisture, soil_acidity):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO soil_data (soil_moisture, soil_acidity) VALUES (%s, %s)", (soil_moisture, soil_acidity))
        conn.commit()
        print("Soil data saved successfully.")
    except mysql.connector.Error as err:
        print("Error saving soil data:", err)
    finally:
        cursor.close()

# Create Table to Store Crop Data and Insert Crop Prices
def create_crop_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crop_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                crop_name VARCHAR(255) NOT NULL,
                price INT NOT NULL
            )
        """)
        # Insert crop prices into the table
        crop_prices = MarketAPI.get_crop_prices()
        for crop, price in crop_prices.items():
            cursor.execute("INSERT INTO crop_data (crop_name, price) VALUES (%s, %s)", (crop, price))
        conn.commit()
        print("Crop table created and crop prices inserted successfully.")
    except mysql.connector.Error as err:
        print("Error creating crop table:", err)
    finally:
        cursor.close()

#Fetch Crop Data from Database
def fetch_crop_data(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM crop_data")
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print("Error fetching crop data:", err)
        return []

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
            "wheat": 12000,
            "tomatoes": 500,
            "cassava": 1500,
            "beans": 2000,
            "irish Potatoes": 3000,
            "sweet Potatoes": 800
        }

    @staticmethod
    def get_demand_trends():
        # Returns a dictionary of crop demand trends
        return {
            "maize": "high",
            "rice": "medium",
            "wheat": "low"
        }

# Retrieves the current soil moisture level from the user
def get_soil_moisture():
    return float(input("Enter current soil moisture level: "))

# Retrieves the current soil acidity level from the user
def get_soil_acidity():
    return float(input("Enter current soil acidity level: "))

# Collects soil data from the user
def collect_soil_data():
    soil_moisture = get_soil_moisture()
    soil_acidity = get_soil_acidity()
    return soil_moisture, soil_acidity

def fetch_weather_forecast():
    # Fetches the weather forecast using an external WeatherAPI
    forecast = WeatherAPI.get_forecast()
    return forecast  # Return the forecast dictionary

def analyze_market_trends():
    # Retrieves crop prices and demand trends from an external MarketAPI
    crop_prices = MarketAPI.get_crop_prices()
    demand_trends = MarketAPI.get_demand_trends()
    return crop_prices, demand_trends

def decision_support_system(conn):
    soil_moisture, soil_acidity = collect_soil_data()
    save_soil_data(conn, soil_moisture, soil_acidity)  # Insert soil data into database
    weather_forecast = fetch_weather_forecast()
    crop_prices, demand_trends = analyze_market_trends()

    crops_in_mind = input("Do you have specific crops in mind? (Yes/No): ").lower()
    recommended_crops = []

    if crops_in_mind == "yes":
        crops_list = input("Enter the crops you have in mind (comma-separated): ").lower().strip().split(",")
        for crop in crops_list:
            crop = crop.strip()  # Remove leading and trailing spaces
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
    conn = establish_connection()
    if conn:
        print("******************************************************************************************")
        print("* Welcome to AGRI-MENTOR! This is a Soil Monitoring Application for Smallholder Farmers. *")
        print("******************************************************************************************")
        print("Let's get started!")

        create_crop_table(conn)  # Create the crop_data table
        recommendation = decision_support_system(conn)
        print("Recommendation:", recommendation)
        print("Thank you for using AGRI-MENTOR! We hope our recommendations are helpful for your farming decisions!")

        conn.close()