
# AgriGenius 360° - AI-Driven Agricultural Advisory Platform

A comprehensive agricultural advisory platform that combines machine learning, real-time data analysis, and interactive visual technologies to empower farmers with intelligent crop recommendations, market insights, and advanced AI-powered farming solutions.

## 🌟 Features

### Core ML Features
- **Crop Recommendation**: ML-driven recommendations based on soil and climate conditions
- **Fertilizer Prediction**: Smart fertilizer suggestions for optimal crop growth
- **Solar Power Estimation**: Solar energy potential calculations for farm operations

### AI-Powered Advanced Features
- **💬 AI Chat Assistant**: Intelligent farming assistant powered by Google Gemini
- **💧 Water Management System**: AI-powered irrigation optimization and water conservation strategies
- **🔬 Plant Disease Detection**: Computer vision-based disease identification from plant images
- **🏛️ Government Schemes Finder**: AI assistant for discovering relevant agricultural subsidies and schemes

### Data & Analytics
- **Market Prices**: Real-time crop price information across different markets
- **Weather Forecast**: Weather predictions for agricultural planning
- **Visual Analytics**: Interactive charts and data visualization

### Water Management System
- Smart irrigation scheduling based on crop type, soil conditions, and weather
- Water conservation strategies with efficiency calculations
- Soil moisture monitoring recommendations
- Seasonal water requirement analysis

### Plant Disease Detection
- Upload plant images for instant disease diagnosis
- AI-powered identification of fungal, bacterial, viral, and nutritional issues
- Treatment recommendations with organic and chemical options
- Prevention strategies and management plans

### Government Schemes Finder
- AI-powered search for relevant agricultural schemes and subsidies
- State-specific and central government scheme information
- Step-by-step application guidance
- Eligibility criteria and required documentation details

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- pip or uv package manager

### Local Installation

1. **Extract the project**
   ```bash
   cd agri_genius_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   SESSION_SECRET=your_secret_key_here
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

   To get a Google Gemini API key:
   - Visit https://makersuite.google.com/app/apikey
   - Create a new API key
   - Copy and paste it in your `.env` file

4. **Run the application**
   ```bash
   python main.py
   ```
   
   Or using gunicorn for production:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

5. **Access the application**
   Open your browser and navigate to: http://localhost:5000

## 📁 Project Structure

```
AgriGenius360/
├── app.py                # Main Flask application with all routes
├── crop_database.py      # Crop information database
├── models/               # ML models and utilities
│   ├── model_loader.py   # Model loading utilities
│   ├── crop_model.pkl    # Trained crop recommendation model
│   ├── fertilizer_model.pkl # Trained fertilizer prediction model
│   └── SolarPower_model.pkl # Trained solar power model
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── crop.html         # Crop recommendation
│   ├── fertilizer.html   # Fertilizer prediction
│   ├── solar.html        # Solar power estimation
│   ├── chat.html         # AI chat assistant
│   ├── water_management.html    # Water management system
│   ├── plant_disease.html       # Plant disease detection
│   ├── gov_schemes.html         # Government schemes finder
│   ├── crop_prices.html         # Market price analysis
│   └── weather_forecast.html    # Weather predictions
├── static/             # Static assets
│   ├── css/            # Stylesheets with animated backgrounds
│   ├── js/             # JavaScript files with particle effects
│   ├── images/         # Image assets and SVG icons
│   └── svg/            # SVG icons for features
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## 🔗 API Endpoints

### Core Features
- `/` - Homepage
- `/crop` - Crop recommendation page
- `/fertilizer` - Fertilizer prediction page
- `/solar` - Solar power estimation page
- `/chat` - AI chat assistant
- `/water_management` - Water management system
- `/plant_disease` - Plant disease detection
- `/gov_schemes` - Government schemes finder

## 🧠 AI Models & Technology

- **Machine Learning**: scikit-learn models for crop, fertilizer, and solar predictions
- **Computer Vision**: Google Gemini Vision for plant disease detection
- **Natural Language Processing**: Google Gemini for chat assistance and scheme recommendations
- **Data Processing**: pandas, numpy for data manipulation
- **Web Framework**: Flask with responsive Bootstrap UI

## 🌍 Multi-language Support

The AI-powered features support multiple Indian languages:
- English
- Hindi (हिंदी)
- Telugu (తెలుగు)
- Tamil (தமிழ்)
- Bengali (বাংলা)
- Marathi (मराठी)
- Gujarati (ગુજરાતી)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- Punjabi (ਪੰਜਾਬੀ)

## 🔧 Dependencies

Main dependencies include:
- Flask - Web framework
- scikit-learn - Machine learning models
- pandas, numpy - Data processing
- google-generativeai - AI chat and vision functionality
- Pillow - Image processing for disease detection
- gunicorn - WSGI HTTP Server

## 🚨 Troubleshooting

### AI Features Not Working
- Ensure GOOGLE_API_KEY is set in your environment
- Check that the API key is valid and has proper permissions
- Verify internet connectivity for API calls

### Image Upload Issues (Plant Disease Detection)
- Ensure images are in supported formats (JPEG, PNG)
- Check file size limits (max 10MB recommended)
- Verify that the uploads directory has write permissions

### Model Loading Errors
- Ensure all .pkl files are present in the models/ directory
- Check Python version compatibility (3.11+ recommended)

### Port Issues
- Default port is 5000
- Change port in main.py if needed: `app.run(host='0.0.0.0', port=YOUR_PORT)`

## 🎯 Usage Examples

### Water Management
1. Select your crop type and field conditions
2. Get AI-powered irrigation recommendations
3. Implement water conservation strategies
4. Monitor and optimize water usage

### Plant Disease Detection
1. Upload a clear image of the affected plant
2. Select your preferred language for results
3. Get instant AI diagnosis and treatment recommendations
4. Follow the provided management plan

### Government Schemes
1. Describe your farming needs or search for specific schemes
2. Get personalized scheme recommendations
3. Access step-by-step application guidance
4. Find relevant contact information and deadlines

## 📞 Support

For issues or questions, please check the error logs in your terminal when running the application. The AI features require a valid Google Gemini API key for full functionality.

## 📄 License

This project is for educational and agricultural assistance purposes. Designed to empower farmers with AI-driven insights and recommendations.

## 🤝 Contributing

AgriGenius 360° is built to help farmers make data-driven decisions and improve agricultural productivity through the power of artificial intelligence and machine learning.
