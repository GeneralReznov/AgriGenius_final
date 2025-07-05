import pickle
import os
import logging

logger = logging.getLogger(__name__)

def load_model(model_path):
    """Load a pickle model"""
    if os.path.exists(model_path):
        try:
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            return model
        except Exception as e:
            logger.error(f"Error loading model from {model_path}: {str(e)}")
            return None
    else:
        logger.error(f"Model file not found: {model_path}")
        return None

def load_model_and_scaler(model_path):
    """Load model and scaler from a single file"""
    if os.path.exists(model_path):
        try:
            with open(model_path, 'rb') as model_file:
                model_data = pickle.load(model_file)
                return model_data['model'], model_data['scaler'], model_data.get('feature_order', None)
        except Exception as e:
            logger.error(f"Error loading model and scaler from {model_path}: {str(e)}")
            return None, None, None
    else:
        logger.error(f"Model file not found: {model_path}")
        return None, None, None

def load_models():
    """Load all models used in the application"""
    # Define model paths
    crop_model_path = 'models/crop_model.pkl'
    fertilizer_model_path = 'models/fertilizer_model.pkl'
    solar_power_model_path = 'models/SolarPower_model.pkl'
    
    # Load crop recommendation model
    crop_model = load_model(crop_model_path)
    
    # Load fertilizer recommendation model
    fertilizer_model = load_model(fertilizer_model_path)
    
    # Load solar power prediction model
    solar_power_model, scaler, feature_order = load_model_and_scaler(solar_power_model_path)
    
    return crop_model, fertilizer_model, solar_power_model, scaler, feature_order
