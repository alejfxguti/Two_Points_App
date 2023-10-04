from flask import Flask, render_template, request, jsonify, current_app
import arcgis
from arcgis.gis import GIS

app = Flask(__name__)

# Get credentials from config 
arcgis_username = config.arcgis_username
arcgis_password = config.arcgis_password
arcgis_url = 'https://www.arcgis.com/sharing/rest/oauth2/authorize?client_id=arcgisdevelopers&response_type=code&expiration=20160&redirect_uri=https%3A%2F%2Fdevelopers.arcgis.com%2Fpost-sign-in%2F&state=%7B%22id%22%3A%22T64KqpNTsl4HCxDIL03McTm7uxY6m1PirPfcM2u0IAY%22%2C%22originalUrl%22%3A%22https%3A%2F%2Fdevelopers.arcgis.com%2F%22%7D&locale=&style=&code_challenge_method=S256&code_challenge=ulnAw7iOdAd2j2KJXtKOcgrdXIulOml_uiWNmsMnxNg&showSignupOption=true&signuptype=developers'

gis = GIS(arcgis_url, arcgis_username, arcgis_password)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calculate_distance', methods=['POST'])
def calculate_distance():
    data = request.get_json()
    start_location = data['start_location']
    end_location = data['end_location']

    try:
        # Retrieve the ArcGIS API key from current_app.config
        arcgis_api_key = current_app.config['ARC_GIS_API_KEY']

        # Use the API key to authenticate with ArcGIS
        gis = GIS(arcgis_url, username=arcgis_username, password=arcgis_password, key=arcgis_api_key)

        start_point = gis.tools.geocoders[0].find_best_match(start_location)
        end_point = gis.tools.geocoders[0].find_best_match(end_location)

        if start_point and end_point:
            start_coords = start_point['location']
            end_coords = end_point['location']

            distance = calculate_distance_between_points(start_coords, end_coords)

            return jsonify({'distance': distance})
        else:
            return jsonify({'error': 'Location not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

def calculate_distance_between_points(start_coords, end_coords):
    start_x, start_y = start_coords['x'], start_coords['y']
    end_x, end_y = end_coords['x'], end_coords['y']

    # Add these functions to your app/routes/main.py

def calculate_travel_time(distance, speed):
    # Calculate travel time in hours
    time_hours = distance / speed
    return time_hours

def convert_hours_to_days_hours_minutes(hours):
    # Convert hours to days, hours, and minutes
    days = int(hours // 24)
    hours %= 24
    minutes = int((hours - int(hours)) * 60)
    return days, int(hours), minutes

# Inside calculate_distance() after distance_km and distance_miles calculations:

    # Calculate travel times for different vehicles
    speed_a380 = 737  # mph
    speed_concorde = 1354  # mph
    speed_bugatti = 304.7  # mph

    time_hours_a380 = calculate_travel_time(distance_miles, speed_a380)
    time_hours_concorde = calculate_travel_time(distance_miles, speed_concorde)
    time_hours_bugatti = calculate_travel_time(distance_miles, speed_bugatti)

    days_a380, hours_a380, minutes_a380 = convert_hours_to_days_hours_minutes(time_hours_a380)
    days_concorde, hours_concorde, minutes_concorde = convert_hours_to_days_hours_minutes(time_hours_concorde)
    days_bugatti, hours_bugatti, minutes_bugatti = convert_hours_to_days_hours_minutes(time_hours_bugatti)

    return calculated_distance_in_miles

if __name__ == '__main__':
    app.run()
