import os
import logging
import json
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, session
import pandas as pd
import numpy as np
import google.generativeai as genai
from models.model_loader import load_models
from crop_database import get_crop_info, get_all_crops

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

# Configure session to avoid 4KB cookie limit
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# Use server-side storage for chat history instead of sessions

# Configure Google Gemini API
os.environ['GOOGLE_API_KEY'] = "AIzaSyCZGGDVIyjebUyHX8m0xO6f1pBD6KKjErc"
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
if GOOGLE_API_KEY:
    try:
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        # Using the correct model name - gemini-1.5-flash is available
        chat_model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        logger.error(f"Error initializing Gemini API: {str(e)}")
        chat_model = None
else:
    logger.warning("GOOGLE_API_KEY not set. Gemini API features will not work properly.")
    chat_model = None

# Load ML models
crop_model, fertilizer_model, solar_power_model, scaler, feature_order = load_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop')
def crop():
    return render_template('crop.html')

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizer.html')

@app.route('/solar')
def solar():
    return render_template('solar.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')
    
@app.route('/crop_prices')
def crop_prices():
    return render_template('crop_prices.html')
    
@app.route('/weather_forecast')
def weather_forecast():
    return render_template('weather_forecast.html')

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    try:
        data = request.json
        
        # Extract input parameters
        n = float(data.get('nitrogen'))
        p = float(data.get('phosphorus'))
        k = float(data.get('potassium'))
        temperature = float(data.get('temperature'))
        humidity = float(data.get('humidity'))
        ph = float(data.get('ph'))
        rainfall = float(data.get('rainfall'))
        
        # Prepare input for prediction
        input_data = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        scaler = crop_model['scaler']
        scaled_input = scaler.transform(input_data)
        prediction = crop_model['model'].predict(scaled_input)
        crop_dict = crop_model['crop_dict']
        
        # Get the recommended crop
        recommended_crop = [key for key, value in crop_dict.items() if value == prediction[0]][0]
        
        # Get comprehensive crop information
        crop_info = get_crop_info(recommended_crop)
        
        # Prepare environmental conditions from input
        environmental_conditions = {
            'soil_nutrients': {
                'nitrogen': f"{n} kg/ha",
                'phosphorus': f"{p} kg/ha", 
                'potassium': f"{k} kg/ha"
            },
            'climate': {
                'temperature': f"{temperature}°C",
                'humidity': f"{humidity}%",
                'ph': f"{ph}",
                'rainfall': f"{rainfall}mm"
            }
        }
        
        # Return comprehensive response
        response_data = {
            'success': True,
            'crop': recommended_crop,
            'environmental_conditions': environmental_conditions
        }
        
        # Add crop database information if available
        if crop_info:
            response_data.update({
                'growing_techniques': crop_info['techniques'],
                'seed_per_acre': crop_info['seed_per_acre'],
                'yield_estimate': crop_info['yield_estimate'],
                'growing_season': crop_info['growing_season'],
                'optimal_conditions': crop_info['optimal_conditions'],
                'fertilizer_schedule': crop_info['fertilizer_schedule']
            })
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Error predicting crop: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/predict_fertilizer', methods=['POST'])
def predict_fertilizer():
    try:
        data = request.json
        
        # Extract input parameters
        temperature = float(data.get('temperature'))
        humidity = float(data.get('humidity'))
        moisture = float(data.get('moisture'))
        soil_type = data.get('soil_type')
        crop_type = data.get('crop_type')
        nitrogen = float(data.get('nitrogen'))
        potassium = float(data.get('potassium'))
        phosphorous = float(data.get('phosphorous'))
        
        # Prepare input for prediction
        input_data = pd.DataFrame({
            'Temperature': [temperature],
            'Humidity': [humidity],
            'Moisture': [moisture],
            'Soil Type': [soil_type],
            'Crop Type': [crop_type],
            'Nitrogen': [nitrogen],
            'Potassium': [potassium],
            'Phosphorous': [phosphorous]
        })
        
        # Encode categorical features
        categorical_cols = fertilizer_model['categorical_cols']
        label_encoders = fertilizer_model['label_encoders']
        for col in categorical_cols:
            input_data[col] = label_encoders[col].transform(input_data[col])
        
        # Scale features
        scaler = fertilizer_model['scaler']
        scaled_input = scaler.transform(input_data)
        
        # Make prediction
        prediction = fertilizer_model['model'].predict(scaled_input)
        
        # Return response
        return jsonify({
            'success': True,
            'fertilizer': prediction[0]
        })
    except Exception as e:
        logger.error(f"Error predicting fertilizer: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/predict_solar', methods=['POST'])
def predict_solar():
    try:
        data = request.json
        
        # Extract input parameters
        distance_to_solar_noon = float(data.get('distance_to_solar_noon'))
        temperature = float(data.get('temperature'))
        wind_direction = float(data.get('wind_direction'))
        wind_speed = float(data.get('wind_speed'))
        sky_cover = float(data.get('sky_cover'))
        visibility = float(data.get('visibility'))
        humidity = float(data.get('humidity'))
        average_wind_speed_period = float(data.get('average_wind_speed_period'))
        average_pressure_period = float(data.get('average_pressure_period'))
        
        # Prepare input for prediction
        input_data = pd.DataFrame({
            'distance-to-solar-noon': [distance_to_solar_noon],
            'temperature': [temperature],
            'wind-direction': [wind_direction],
            'wind-speed': [wind_speed],
            'sky-cover': [sky_cover],
            'visibility': [visibility],
            'humidity': [humidity],
            'average-wind-speed-(period)': [average_wind_speed_period],
            'average-pressure-(period)': [average_pressure_period]
        }, columns=feature_order)
        
        # Scale features
        scaled_features = scaler.transform(input_data)
        
        # Make prediction
        prediction = solar_power_model.predict(scaled_features)
        
        # Return response
        return jsonify({
            'success': True,
            'power': float(prediction[0])
        })
    except Exception as e:
        logger.error(f"Error predicting solar power: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/chat_with_bot', methods=['POST'])
def chat_with_bot():
    try:
        data = request.json
        prompt = data.get('message', '')
        
        if not GOOGLE_API_KEY or not chat_model:
            return jsonify({
                'success': False,
                'error': "Chat service is not available. Please contact administrator."
            }), 500
        
        try:
            import uuid
            import time
            
            # Get or create session ID using simple approach
            session_id = request.headers.get('X-Session-ID') or str(uuid.uuid4())
            
            # Server-side storage for unlimited chat history
            if not hasattr(app, 'chat_histories'):
                app.chat_histories = {}
            
            if session_id not in app.chat_histories:
                app.chat_histories[session_id] = []
            
            # Add user message with timestamp
            app.chat_histories[session_id].append({
                "role": "user", 
                "content": prompt,
                "timestamp": time.time()
            })
            
            # Use the user's prompt directly like in Streamlit version
            # Let the AI model handle response length naturally
            
            # Use conversation history for context (last 10 exchanges)
            recent_history = app.chat_histories[session_id][-20:] if len(app.chat_histories[session_id]) > 20 else app.chat_histories[session_id]
            context_messages = []
            
            for msg in recent_history[:-1]:  # Exclude current user message
                if msg["role"] == "user":
                    context_messages.append({"role": "user", "parts": [msg["content"]]})
                elif msg["role"] == "assistant":
                    context_messages.append({"role": "model", "parts": [msg["content"]]})
            
            # Generate response with context like Streamlit version
            chat_session = chat_model.start_chat(history=context_messages)
            response = chat_session.send_message(prompt)
            full_response = response.text
            
            # Store bot response
            app.chat_histories[session_id].append({
                "role": "assistant", 
                "content": full_response,
                "timestamp": time.time()
            })
            
            # Clean old sessions periodically (keep last 50 messages per session)
            if len(app.chat_histories[session_id]) > 50:
                app.chat_histories[session_id] = app.chat_histories[session_id][-50:]
            
            return jsonify({
                'success': True,
                'response': full_response,
                'session_id': session_id,
                'message_count': len(app.chat_histories[session_id])
            })
            
        except Exception as api_error:
            logger.error(f"Error generating response: {str(api_error)}")
            return jsonify({
                'success': False,
                'error': f"Error generating response: {str(api_error)}"
            }), 500
            
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        return jsonify({
            'success': False,
            'error': f"Error in chat: {str(e)}"
        }), 500
        


@app.route('/get_crop_prices', methods=['POST'])
def get_crop_prices():
    try:
        data = request.json
        crop_type = data.get('crop', 'rice')
        market_region = data.get('region', 'all')
        
        import random
        
        # Base prices for different crops (₹/Quintal)
        base_prices = {
            'rice': {'min': 1800, 'max': 2200, 'avg': 2000},
            'wheat': {'min': 2000, 'max': 2400, 'avg': 2200},
            'maize': {'min': 1600, 'max': 2000, 'avg': 1800},
            'pulses': {'min': 6000, 'max': 8000, 'avg': 7000},
            'cotton': {'min': 5500, 'max': 6500, 'avg': 6000},
            'sugarcane': {'min': 280, 'max': 320, 'avg': 300},
            'potato': {'min': 800, 'max': 1200, 'avg': 1000},
            'onion': {'min': 1500, 'max': 2500, 'avg': 2000},
            'tomato': {'min': 2000, 'max': 4000, 'avg': 3000},
            'apple': {'min': 8000, 'max': 12000, 'avg': 10000},
            'mango': {'min': 4000, 'max': 7000, 'avg': 5500}
        }
        
        # State-specific market locations
        state_markets = {
            'punjab': ['Ludhiana Grain Mandi', 'Amritsar Agricultural Market', 'Jalandhar Wholesale Market', 'Patiala Grain Exchange', 'Bathinda Mandi', 'Moga Agricultural Center', 'Fazilka Grain Market', 'Barnala Rice Market'],
            'maharashtra': ['Pune Market Yard', 'Nashik Grain Mandi', 'Aurangabad Wholesale Market', 'Kolhapur Agricultural Center', 'Nagpur Cotton Market', 'Yavatmal Mandi', 'Akola Agricultural Market', 'Wardha Cotton Exchange'],
            'kerala': ['Palakkad Rice Market', 'Alappuzha Mandi', 'Thrissur Agricultural Market', 'Kottayam Rice Center', 'Kozhikode Coconut Market', 'Ernakulam Wholesale Market', 'Kannur Agricultural Center', 'Kollam Coconut Exchange'],
            'gujarat': ['Ahmedabad Jamalpur', 'Rajkot Agricultural Mandi', 'Surendranagar Cotton Center', 'Bhavnagar Wholesale Market', 'Junagadh Groundnut Market', 'Amreli Agricultural Mandi', 'Jamnagar Wholesale Center', 'Porbandar Oil Seeds Market'],
            'west_bengal': ['Kolkata Posta Bazar', 'Burdwan Agricultural Mandi', 'Hooghly Wholesale Market', 'Nadia Rice Center', 'Siliguri Jute Market', 'Malda Agricultural Center', 'Cooch Behar Wholesale Market', 'Jalpaiguri Jute Exchange'],
            'tamil_nadu': ['Chennai Koyambedu', 'Thanjavur Rice Market', 'Coimbatore Agricultural Mandi', 'Salem Wholesale Market', 'Tiruchirapalli Rice Center', 'Erode Sugar Market', 'Tirunelveli Agricultural Center', 'Dindigul Wholesale Market'],
            'karnataka': ['Bangalore Yeshwantpur', 'Mysore Agricultural Market', 'Hubli Wholesale Center', 'Belgaum Grain Market', 'Mandya Sugar Market', 'Hassan Coffee Exchange', 'Tumkur Agricultural Mandi', 'Chitradurga Wholesale Market'],
            'rajasthan': ['Jaipur Muhana Mandi', 'Jodhpur Agricultural Market', 'Kota Grain Exchange', 'Bikaner Wholesale Center', 'Udaipur Agricultural Mandi', 'Ajmer Grain Market', 'Alwar Wholesale Market', 'Bharatpur Agricultural Center'],
            'uttar_pradesh': ['Lucknow Alambagh', 'Kanpur Grain Market', 'Agra Agricultural Mandi', 'Varanasi Wholesale Market', 'Meerut Grain Exchange', 'Bareilly Agricultural Center', 'Gorakhpur Wholesale Market', 'Allahabad Grain Mandi'],
            'andhra_pradesh': ['Visakhapatnam Agricultural Market', 'Vijayawada Grain Mandi', 'Guntur Agricultural Center', 'Tirupati Wholesale Market', 'Kurnool Grain Exchange', 'Rajahmundry Rice Market', 'Nellore Agricultural Mandi', 'Anantapur Cotton Market'],
            'madhya_pradesh': ['Bhopal Grain Mandi', 'Indore Agricultural Market', 'Jabalpur Wholesale Center', 'Gwalior Grain Exchange', 'Ujjain Agricultural Mandi', 'Sagar Wholesale Market', 'Ratlam Grain Center', 'Satna Agricultural Market'],
            'haryana': ['Kurukshetra Grain Mandi', 'Karnal Agricultural Market', 'Panipat Wholesale Center', 'Hisar Grain Exchange', 'Rohtak Agricultural Mandi', 'Sirsa Wholesale Market', 'Ambala Grain Center', 'Yamunanagar Agricultural Market'],
            'delhi': ['Delhi Azadpur Mandi', 'Najafgarh Agricultural Market', 'Ghazipur Wholesale Center', 'Okhla Grain Market', 'Narela Agricultural Mandi', 'Shahdara Wholesale Market', 'Mundka Grain Center', 'Keshopur Agricultural Market'],
            'assam': ['Guwahati Tea Market', 'Jorhat Agricultural Center', 'Dibrugarh Tea Exchange', 'Tezpur Wholesale Market', 'Silchar Agricultural Mandi', 'Nagaon Rice Market', 'Goalpara Wholesale Center', 'Bongaigaon Agricultural Market']
        }
        
        # Get state-specific markets or use general markets for "all" option
        if market_region == 'all':
            markets = [
                'Delhi Azadpur Mandi', 'Mumbai Vashi APMC', 'Kolkata Posta Bazar',
                'Chennai Koyambedu', 'Bangalore Yeshwantpur', 'Hyderabad Gaddiannaram',
                'Pune Market Yard', 'Ahmedabad Jamalpur'
            ]
        else:
            markets = state_markets.get(market_region.lower(), [
                'Delhi Azadpur Mandi', 'Mumbai Vashi APMC', 'Kolkata Posta Bazar',
                'Chennai Koyambedu', 'Bangalore Yeshwantpur', 'Hyderabad Gaddiannaram',
                'Pune Market Yard', 'Ahmedabad Jamalpur'
            ])
        
        base_price = base_prices.get(crop_type, base_prices['rice'])
        
        # Generate sample price data
        prices = []
        for i, market in enumerate(markets[:8]):  # Show 8 markets
            price_variation = random.uniform(-0.15, 0.15)  # ±15% variation
            price = int(base_price['avg'] * (1 + price_variation))
            
            trend = random.choice(['up', 'down', 'stable'])
            quality = random.choice(['Grade A', 'Grade B', 'Premium', 'Standard'])
            
            prices.append({
                'market': market,
                'price': price,
                'trend': trend,
                'quality': quality
            })
        
        # Sort by price for better visualization
        prices.sort(key=lambda x: x['price'], reverse=True)
        
        # Chart data
        chart_data = {
            'labels': [p['market'].split()[0] for p in prices],  # Short names
            'prices': [p['price'] for p in prices],
            'colors': ['#4CAF50' if p['trend'] == 'up' else '#f44336' if p['trend'] == 'down' else '#FFC107' for p in prices],
            'borderColors': ['#388E3C' if p['trend'] == 'up' else '#d32f2f' if p['trend'] == 'down' else '#F57F17' for p in prices]
        }
        
        # Analysis
        avg_price = sum(p['price'] for p in prices) // len(prices)
        min_price = min(p['price'] for p in prices)
        max_price = max(p['price'] for p in prices)
        
        up_trend_count = sum(1 for p in prices if p['trend'] == 'up')
        down_trend_count = sum(1 for p in prices if p['trend'] == 'down')
        
        if up_trend_count > down_trend_count:
            sentiment = 'bullish'
        elif down_trend_count > up_trend_count:
            sentiment = 'bearish'
        else:
            sentiment = 'stable'
        
        analysis = {
            'average_price': avg_price,
            'price_range': {'min': min_price, 'max': max_price},
            'market_sentiment': sentiment,
            'insights': [
                f"Average {crop_type} price across markets is ₹{avg_price}/quintal",
                f"Price variation ranges from ₹{min_price} to ₹{max_price}",
                f"Market sentiment is {sentiment} with {up_trend_count} markets showing upward trend"
            ],
            'recommendations': [
                "Monitor daily price fluctuations for optimal selling time",
                "Consider transportation costs when selecting markets",
                "Quality grading significantly impacts final prices"
            ]
        }
        
        return jsonify({
            'success': True,
            'prices': prices,
            'chart_data': chart_data,
            'analysis': analysis
        })
            
    except Exception as e:
        logger.error(f"Error getting crop prices: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Unable to retrieve market price data.'
        }), 500

@app.route('/get_weather_forecast', methods=['POST'])
def get_weather_forecast():
    try:
        data = request.json
        region = data.get('region', 'punjab')
        days = int(data.get('days', 3))
        
        import random
        from datetime import datetime, timedelta
        
        # Region information
        region_data = {
            'punjab': {'name': 'Punjab (Wheat Belt)', 'temp_range': (15, 32)},
            'kerala': {'name': 'Kerala (Spice & Plantation)', 'temp_range': (22, 34)},
            'maharashtra': {'name': 'Maharashtra (Cotton & Grapes)', 'temp_range': (18, 36)},
            'assam': {'name': 'Assam (Tea Plantations)', 'temp_range': (20, 30)},
            'karnataka': {'name': 'Karnataka (Coffee Region)', 'temp_range': (16, 32)},
            'westbengal': {'name': 'West Bengal (Rice Bowl)', 'temp_range': (20, 34)},
            'gujarat': {'name': 'Gujarat (Groundnut Region)', 'temp_range': (16, 38)},
            'tamilnadu': {'name': 'Tamil Nadu (Rice & Sugarcane)', 'temp_range': (22, 36)},
            'rajasthan': {'name': 'Rajasthan (Desert Agriculture)', 'temp_range': (12, 40)},
            'uttarpradesh': {'name': 'Uttar Pradesh (Sugarcane Belt)', 'temp_range': (14, 34)}
        }
        
        region_info = region_data.get(region, region_data['punjab'])
        
        # Weather conditions and icons
        weather_conditions = [
            {'condition': 'Sunny', 'icon': 'fas fa-sun', 'precip_range': (0, 2)},
            {'condition': 'Partly Cloudy', 'icon': 'fas fa-cloud-sun', 'precip_range': (0, 5)},
            {'condition': 'Cloudy', 'icon': 'fas fa-cloud', 'precip_range': (2, 8)},
            {'condition': 'Light Rain', 'icon': 'fas fa-cloud-rain', 'precip_range': (5, 15)},
            {'condition': 'Moderate Rain', 'icon': 'fas fa-cloud-showers-heavy', 'precip_range': (10, 25)}
        ]
        
        # Generate current weather
        current_weather = random.choice(weather_conditions)
        current_temp = random.randint(region_info['temp_range'][0], region_info['temp_range'][1])
        
        current_data = {
            'temperature': current_temp,
            'condition': current_weather['condition'],
            'wind_speed': random.randint(5, 20),
            'humidity': random.randint(40, 85),
            'precipitation': random.randint(*current_weather['precip_range']),
            'icon': current_weather['icon']
        }
        
        # Generate forecast data
        forecast = []
        for i in range(days):
            date = datetime.now() + timedelta(days=i+1)
            weather = random.choice(weather_conditions)
            
            temp_high = random.randint(region_info['temp_range'][0] + 5, region_info['temp_range'][1])
            temp_low = random.randint(region_info['temp_range'][0], max(region_info['temp_range'][0], temp_high - 8))
            
            forecast.append({
                'day': date.strftime('%a, %b %d'),
                'condition': weather['condition'],
                'icon': weather['icon'],
                'temp_high': temp_high,
                'temp_low': temp_low,
                'humidity': random.randint(45, 80),
                'precipitation': random.randint(*weather['precip_range'])
            })
        
        # Agricultural insights based on weather
        insights = {
            'impact': f"Current weather conditions in {region_info['name']} are favorable for agricultural activities with moderate temperatures and controlled precipitation levels.",
            'recommendations': [
                "Monitor soil moisture levels regularly",
                "Adjust irrigation schedules based on precipitation forecasts",
                "Plan field operations during favorable weather windows",
                "Protect crops from extreme weather conditions"
            ],
            'crop_advice': [
                "Kharif crops: Suitable conditions for growth and development",
                "Rabi crops: Plan sowing activities based on weather patterns",
                "Cash crops: Monitor for pest and disease outbreaks during humid conditions"
            ]
        }
        
        return jsonify({
            'success': True,
            'data': {
                'location': region_info['name'],
                'current': current_data,
                'forecast': forecast,
                'agricultural_insights': insights
            }
        })
            
    except Exception as e:
        logger.error(f"Error getting weather forecast: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Unable to retrieve weather forecast data.'
        }), 500

# New AI-powered features

@app.route('/water_management')
def water_management():
    return render_template('water_management.html')

@app.route('/plant_disease')
def plant_disease():
    return render_template('plant_disease.html')

@app.route('/gov_schemes')
def gov_schemes():
    return render_template('gov_schemes.html')

def get_weather_forecast_data(lat, lon):
    """Fetch weather data from Open-Meteo API"""
    try:
        import requests
        url = f"https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,wind_speed_10m_max',
            'timezone': 'auto',
            'forecast_days': 7
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        logger.error(f"Error fetching weather data: {e}")
        return None

@app.route('/suggest_water_management', methods=['POST'])
def suggest_water_management():
    try:
        data = request.json
        crop = data.get('crop', 'wheat')
        soil_type = data.get('soil_type', 'loamy')
        field_size = float(data.get('field_size', 1.0))
        location = data.get('location', 'Punjab')
        irrigation_method = data.get('irrigation_method', 'drip')
        language = data.get('language', 'en')
        
        if not GOOGLE_API_KEY or not chat_model:
            return jsonify({
                'success': False,
                'error': "Water management service is not available. Please contact administrator."
            }), 500
        
        # Enhanced prompt for water management with current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_month = datetime.now().strftime("%B")
        current_year = datetime.now().year
        
        prompt = f"""You are an expert agricultural water management specialist. Create a comprehensive water management plan for {current_month} {current_year}.

Farmer Details:
- Crop: {crop}
- Soil Type: {soil_type}
- Field Size: {field_size} acres
- Location: {location}
- Current Irrigation Method: {irrigation_method}
- Date: {current_date}

Create a detailed water management plan in {language} that includes:

1. WATER REQUIREMENTS ANALYSIS:
   - Daily water needs based on crop type and growth stage
   - Soil moisture requirements for {soil_type} soil
   - Water efficiency for {irrigation_method} method
   - Seasonal adjustments for {current_month} {current_year}

2. IRRIGATION RECOMMENDATIONS:
   - Optimal irrigation frequency and timing
   - Best practices for {irrigation_method} irrigation
   - Water application rates and duration
   - Monitoring techniques

3. CONSERVATION STRATEGIES:
   - 5 specific water-saving techniques suitable for {crop}
   - Expected water savings percentage
   - Cost-benefit analysis
   - Sustainable practices

4. PRACTICAL GUIDANCE:
   - Soil moisture monitoring methods
   - Weather-based irrigation adjustments
   - Equipment maintenance and optimization
   - Troubleshooting common issues

5. SEASONAL CONSIDERATIONS:
   - {current_month} specific watering needs
   - Climate considerations for {location}
   - Crop growth stage requirements

Provide realistic, implementable advice for {crop} cultivation in {location} considering current weather conditions and best practices."""

        try:
            response = chat_model.generate_content(prompt)
            ai_response = response.text
            
            return jsonify({
                'success': True,
                'analysis': ai_response,
                'query_info': {
                    'crop': crop,
                    'soil_type': soil_type,
                    'field_size': field_size,
                    'location': location,
                    'irrigation_method': irrigation_method,
                    'language': language
                }
            })
            
        except Exception as api_error:
            logger.error(f"Error generating water management advice: {str(api_error)}")
            return jsonify({
                'success': False,
                'error': f"Error generating advice: {str(api_error)}"
            }), 500
            
    except Exception as e:
        logger.error(f"Error in water management: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/detect_plant_disease', methods=['POST'])
def detect_plant_disease():
    try:
        if 'image' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No image file uploaded'
            }), 400
        
        file = request.files['image']
        language = request.form.get('language', 'en')
        
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No image file selected'
            }), 400
        
        if not GOOGLE_API_KEY or not chat_model:
            return jsonify({
                'success': False,
                'error': "Plant disease detection service is not available. Please contact administrator."
            }), 500
        
        try:
            import base64
            from PIL import Image
            import io
            
            # Read and process the image
            image_bytes = file.read()
            image = Image.open(io.BytesIO(image_bytes))
            
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize image if too large (max 1024px)
            max_size = 1024
            if max(image.size) > max_size:
                ratio = max_size / max(image.size)
                new_size = tuple(int(dim * ratio) for dim in image.size)
                image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Convert to base64
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', quality=85)
            image_base64 = base64.b64encode(buffer.getvalue()).decode()
            
            # Enhanced prompt for plant disease detection
            prompt = f"""You are an expert plant pathologist and agricultural specialist. Analyze this plant image and provide a comprehensive disease diagnosis in {language}.

Provide a detailed analysis including:

1. PLANT IDENTIFICATION:
   - Plant type and variety if identifiable
   - Growth stage and overall health assessment

2. DISEASE DIAGNOSIS:
   - Primary disease(s) identified
   - Disease type (fungal, bacterial, viral, nutritional, environmental, pest)
   - Confidence level of diagnosis
   - Symptoms observed

3. TREATMENT RECOMMENDATIONS:
   - Immediate treatment steps
   - Organic treatment options
   - Chemical treatment if necessary
   - Prevention strategies

4. MANAGEMENT PLAN:
   - Cultural practices to prevent spread
   - Monitoring recommendations
   - Expected recovery timeline
   - When to seek professional help

5. ADDITIONAL ADVICE:
   - Environmental factors that may contribute
   - Nutritional recommendations
   - Irrigation and care adjustments

Be specific, practical, and provide actionable advice that farmers can implement immediately."""

            # Generate response using Gemini Vision
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content([
                prompt,
                {
                    'mime_type': 'image/jpeg',
                    'data': image_base64
                }
            ])
            
            ai_response = response.text
            
            return jsonify({
                'success': True,
                'analysis': ai_response,
                'query_info': {
                    'language': language,
                    'image_processed': True,
                    'analysis_type': 'Plant Disease Detection'
                }
            })
            
        except Exception as api_error:
            logger.error(f"Error in plant disease detection: {str(api_error)}")
            return jsonify({
                'success': False,
                'error': f"Error analyzing image: {str(api_error)}"
            }), 500
            
    except Exception as e:
        logger.error(f"Error in plant disease detection: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/get_gov_scheme_info', methods=['POST'])
def get_gov_scheme_info():
    try:
        data = request.json
        query = data.get('query', 'agricultural schemes')
        state = data.get('state', 'all')
        scheme_type = data.get('scheme_type', 'all')
        language = data.get('language', 'en')
        
        if not GOOGLE_API_KEY or not chat_model:
            return jsonify({
                'success': False,
                'error': "Government schemes service is not available. Please contact administrator."
            }), 500
        
        # Enhanced prompt for government schemes
        prompt = f"""You are an expert on Indian agricultural policies and government schemes. Provide comprehensive information about agricultural schemes in {language}.

Query: {query}
State Focus: {state}
Scheme Type: {scheme_type}

Provide detailed information including:

1. RELEVANT SCHEMES:
   - List 8-10 most relevant government schemes
   - Both central and state-level schemes
   - Include scheme names, implementing agencies

2. SCHEME DETAILS:
   For each scheme provide:
   - Eligibility criteria
   - Financial benefits/subsidies
   - Application process
   - Required documents
   - Implementation timeline

3. CATEGORIZATION:
   - Financial assistance schemes
   - Insurance schemes  
   - Subsidy schemes
   - Technology adoption schemes
   - Training and development programs

4. APPLICATION GUIDANCE:
   - Step-by-step application process
   - Online/offline application options
   - Contact information for assistance
   - Common mistakes to avoid

5. STATE-SPECIFIC INFORMATION:
   {f"- Focus on {state} state schemes" if state != 'all' else "- Cover major agricultural states"}
   - Regional implementation variations
   - Local contact points

6. CURRENT STATUS:
   - Recently launched schemes (2024-2025)
   - Updated benefit amounts
   - Application deadlines if any

Provide practical, actionable information that farmers can use immediately to access these schemes."""

        try:
            response = chat_model.generate_content(prompt)
            ai_response = response.text
            
            return jsonify({
                'success': True,
                'analysis': ai_response,
                'schemes': ai_response,  # Add this for compatibility
                'query': query,
                'language': language,
                'query_info': {
                    'query': query,
                    'state': state,
                    'scheme_type': scheme_type,
                    'language': language
                }
            })
            
        except Exception as api_error:
            logger.error(f"Error getting government scheme info: {str(api_error)}")
            return jsonify({
                'success': False,
                'error': f"Error generating scheme information: {str(api_error)}"
            }), 500
            
    except Exception as e:
        logger.error(f"Error in government schemes: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
