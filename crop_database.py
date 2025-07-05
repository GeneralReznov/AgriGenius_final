"""
Comprehensive crop database with growing techniques, seed requirements, and yield estimates
"""

CROP_DATABASE = {
    'rice': {
        'name': 'Rice',
        'techniques': [
            'Transplanting method for better yield',
            'Maintain 2-3 cm water level in fields',
            'Apply organic matter before planting',
            'Use line planting with 20cm x 15cm spacing'
        ],
        'seed_per_acre': '15-20 kg',
        'yield_estimate': '2500-4000 kg/acre',
        'growing_season': '120-150 days',
        'optimal_conditions': {
            'temperature': '20-35°C',
            'rainfall': '1000-2000mm',
            'soil_ph': '5.5-7.0',
            'soil_type': 'Clay loam, well-drained'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 25kg urea + 50kg DAP per acre',
            'tillering': 'Apply 25kg urea per acre (21-30 days)',
            'panicle': 'Apply 25kg urea per acre (45-60 days)'
        }
    },
    'maize': {
        'name': 'Maize',
        'techniques': [
            'Direct seeding with proper spacing',
            'Ridge and furrow method for water management',
            'Intercropping with legumes for nitrogen',
            'Use hybrid varieties for better yield'
        ],
        'seed_per_acre': '8-10 kg',
        'yield_estimate': '2000-3500 kg/acre',
        'growing_season': '90-120 days',
        'optimal_conditions': {
            'temperature': '18-32°C',
            'rainfall': '500-1200mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Well-drained loamy soil'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 40kg DAP + 20kg MOP per acre',
            'knee_high': 'Apply 40kg urea per acre (30-35 days)',
            'tasseling': 'Apply 20kg urea per acre (50-60 days)'
        }
    },
    'chickpea': {
        'name': 'Chickpea',
        'techniques': [
            'Seed treatment with rhizobium culture',
            'Ridge planting for water conservation',
            'Avoid waterlogging during flowering',
            'Use resistant varieties for diseases'
        ],
        'seed_per_acre': '30-35 kg',
        'yield_estimate': '800-1500 kg/acre',
        'growing_season': '90-120 days',
        'optimal_conditions': {
            'temperature': '15-30°C',
            'rainfall': '300-600mm',
            'soil_ph': '6.2-7.8',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 40kg DAP per acre',
            'flowering': 'Foliar spray of DAP (2%) if needed',
            'pod_filling': 'Apply micronutrients if deficient'
        }
    },
    'kidneybeans': {
        'name': 'Kidney Beans',
        'techniques': [
            'Seed inoculation with rhizobium bacteria',
            'Plant in rows with 30cm spacing',
            'Provide support for climbing varieties',
            'Regular weeding and pest management'
        ],
        'seed_per_acre': '25-30 kg',
        'yield_estimate': '1000-1800 kg/acre',
        'growing_season': '90-110 days',
        'optimal_conditions': {
            'temperature': '18-24°C',
            'rainfall': '400-800mm',
            'soil_ph': '6.0-7.0',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 30kg DAP per acre',
            'flowering': 'Apply potash if soil test indicates deficiency',
            'pod_development': 'Foliar feeding with micronutrients'
        }
    },
    'pigeonpeas': {
        'name': 'Pigeon Peas',
        'techniques': [
            'Intercropping with cereals for better land use',
            'Deep plowing for root development',
            'Stake tall varieties to prevent lodging',
            'Harvest pods when fully mature'
        ],
        'seed_per_acre': '8-12 kg',
        'yield_estimate': '800-1200 kg/acre',
        'growing_season': '150-210 days',
        'optimal_conditions': {
            'temperature': '20-35°C',
            'rainfall': '600-1000mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Well-drained red or black soil'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 30kg DAP per acre',
            'flowering': 'Side dressing with compost',
            'pod_filling': 'Apply micronutrient mixture'
        }
    },
    'mothbeans': {
        'name': 'Moth Beans',
        'techniques': [
            'Drought-resistant crop suitable for arid regions',
            'Broadcast seeding followed by light harrowing',
            'Minimal irrigation required',
            'Harvest when pods turn brown'
        ],
        'seed_per_acre': '12-15 kg',
        'yield_estimate': '400-800 kg/acre',
        'growing_season': '75-90 days',
        'optimal_conditions': {
            'temperature': '25-35°C',
            'rainfall': '200-500mm',
            'soil_ph': '7.0-8.5',
            'soil_type': 'Sandy loam, drought-tolerant'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 20kg DAP per acre',
            'minimal_fertilizer': 'Drought-resistant, minimal fertilizer needs',
            'harvest': 'No additional fertilizer typically needed'
        }
    },
    'mungbean': {
        'name': 'Mung Bean',
        'techniques': [
            'Short duration crop ideal for crop rotation',
            'Line sowing for uniform germination',
            'Light irrigation at critical stages',
            'Harvest when 80% pods turn black'
        ],
        'seed_per_acre': '15-20 kg',
        'yield_estimate': '600-1000 kg/acre',
        'growing_season': '60-90 days',
        'optimal_conditions': {
            'temperature': '25-35°C',
            'rainfall': '300-600mm',
            'soil_ph': '6.2-7.2',
            'soil_type': 'Well-drained loamy soil'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 25kg DAP per acre',
            'flowering': 'Light application of potash',
            'pod_filling': 'Minimal additional fertilizer'
        }
    },
    'blackgram': {
        'name': 'Black Gram',
        'techniques': [
            'Suitable for both rain-fed and irrigated conditions',
            'Seed treatment with fungicide',
            'Maintain proper plant population',
            'Regular monitoring for pest and diseases'
        ],
        'seed_per_acre': '15-20 kg',
        'yield_estimate': '500-900 kg/acre',
        'growing_season': '70-90 days',
        'optimal_conditions': {
            'temperature': '25-35°C',
            'rainfall': '400-700mm',
            'soil_ph': '6.5-7.5',
            'soil_type': 'Well-drained clayey loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 30kg DAP per acre',
            'flowering': 'Foliar application of urea (2%)',
            'pod_development': 'Micronutrient spray if required'
        }
    },
    'lentil': {
        'name': 'Lentil',
        'techniques': [
            'Winter crop requiring cool weather',
            'Seed inoculation for nitrogen fixation',
            'Avoid excess moisture during maturity',
            'Harvest when leaves turn yellow'
        ],
        'seed_per_acre': '25-30 kg',
        'yield_estimate': '700-1200 kg/acre',
        'growing_season': '110-130 days',
        'optimal_conditions': {
            'temperature': '15-25°C',
            'rainfall': '300-500mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 35kg DAP per acre',
            'flowering': 'Apply potash if soil test indicates',
            'pod_filling': 'Minimal additional fertilizer'
        }
    },
    'pomegranate': {
        'name': 'Pomegranate',
        'techniques': [
            'Deep planting with proper drainage',
            'Regular pruning for shape and yield',
            'Drip irrigation for water efficiency',
            'Mulching to conserve moisture'
        ],
        'seed_per_acre': '100-120 plants',
        'yield_estimate': '8000-15000 kg/acre',
        'growing_season': 'Perennial (3-4 years to full production)',
        'optimal_conditions': {
            'temperature': '20-30°C',
            'rainfall': '500-800mm',
            'soil_ph': '6.5-7.5',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 20kg FYM + 1kg NPK per plant',
            'flowering': 'Foliar feeding with micronutrients',
            'fruit_development': 'Potash application for fruit quality'
        }
    },
    'banana': {
        'name': 'Banana',
        'techniques': [
            'Plant tissue culture saplings for disease-free crop',
            'Provide wind protection and support',
            'Regular de-suckering and leaf removal',
            'Harvest at proper maturity stage'
        ],
        'seed_per_acre': '400-500 plants',
        'yield_estimate': '25000-40000 kg/acre',
        'growing_season': 'Perennial (12-15 months per crop)',
        'optimal_conditions': {
            'temperature': '26-30°C',
            'rainfall': '1200-2500mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Deep, well-drained loamy soil'
        },
        'fertilizer_schedule': {
            'monthly': 'Apply 200g urea + 100g MOP per plant',
            'flowering': 'Increase potash application',
            'bunch_development': 'Apply micronutrients'
        }
    },
    'mango': {
        'name': 'Mango',
        'techniques': [
            'Grafted plants for better yield and quality',
            'Proper spacing for air circulation',
            'Regular pruning after harvest',
            'Integrated pest management practices'
        ],
        'seed_per_acre': '40-50 plants',
        'yield_estimate': '5000-12000 kg/acre',
        'growing_season': 'Perennial (3-5 years to bearing)',
        'optimal_conditions': {
            'temperature': '24-30°C',
            'rainfall': '750-2500mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Deep, well-drained alluvial soil'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 25kg FYM + 2kg NPK per plant',
            'pre_flowering': 'Apply potash for flower induction',
            'fruit_development': 'Balanced NPK application'
        }
    },
    'grapes': {
        'name': 'Grapes',
        'techniques': [
            'Training and pruning for proper vine structure',
            'Drip irrigation with fertigation',
            'Canopy management for light penetration',
            'Harvest at optimal sugar content'
        ],
        'seed_per_acre': '400-500 plants',
        'yield_estimate': '8000-15000 kg/acre',
        'growing_season': 'Perennial (2-3 years to production)',
        'optimal_conditions': {
            'temperature': '20-30°C',
            'rainfall': '600-1200mm',
            'soil_ph': '6.5-7.5',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 15kg FYM + 1.5kg NPK per plant',
            'flowering': 'Foliar application of micronutrients',
            'fruit_development': 'Potash for fruit quality'
        }
    },
    'watermelon': {
        'name': 'Watermelon',
        'techniques': [
            'Direct seeding or transplanting',
            'Mulching for moisture conservation',
            'Regular vine training and pruning',
            'Harvest when tendril near fruit dries'
        ],
        'seed_per_acre': '1-2 kg',
        'yield_estimate': '15000-25000 kg/acre',
        'growing_season': '90-120 days',
        'optimal_conditions': {
            'temperature': '20-35°C',
            'rainfall': '400-600mm',
            'soil_ph': '6.0-7.0',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 50kg DAP + 25kg MOP per acre',
            'flowering': 'Apply 25kg urea per acre',
            'fruit_development': 'Additional potash for sweetness'
        }
    },
    'muskmelon': {
        'name': 'Muskmelon',
        'techniques': [
            'Raised bed cultivation for drainage',
            'Plastic mulching for temperature control',
            'Hand pollination for better fruit set',
            'Support fruits to prevent ground contact'
        ],
        'seed_per_acre': '0.8-1.2 kg',
        'yield_estimate': '8000-15000 kg/acre',
        'growing_season': '90-110 days',
        'optimal_conditions': {
            'temperature': '18-30°C',
            'rainfall': '400-600mm',
            'soil_ph': '6.0-7.0',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 40kg DAP + 20kg MOP per acre',
            'flowering': 'Apply 20kg urea per acre',
            'fruit_filling': 'Foliar feeding with calcium'
        }
    },
    'cotton': {
        'name': 'Cotton',
        'techniques': [
            'Use certified BT cotton seeds',
            'Maintain proper plant spacing',
            'Regular monitoring for bollworm',
            'Multiple pickings for quality fiber'
        ],
        'seed_per_acre': '1.5-2.5 kg',
        'yield_estimate': '15-25 quintals/acre',
        'growing_season': '150-180 days',
        'optimal_conditions': {
            'temperature': '20-35°C',
            'rainfall': '500-1000mm',
            'soil_ph': '6.0-8.0',
            'soil_type': 'Deep, well-drained black soil'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 60kg DAP + 30kg MOP per acre',
            'squaring': 'Apply 40kg urea per acre (45 days)',
            'flowering': 'Apply 20kg urea per acre (75 days)'
        }
    },
    'jute': {
        'name': 'Jute',
        'techniques': [
            'Line sowing for uniform growth',
            'Proper water management during growth',
            'Retting process for fiber extraction',
            'Harvest at proper maturity for quality fiber'
        ],
        'seed_per_acre': '5-7 kg',
        'yield_estimate': '20-30 quintals/acre',
        'growing_season': '120-150 days',
        'optimal_conditions': {
            'temperature': '25-35°C',
            'rainfall': '1200-2500mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Alluvial soil with good drainage'
        },
        'fertilizer_schedule': {
            'pre_planting': 'Apply 40kg DAP + 20kg MOP per acre',
            'vegetative': 'Apply 40kg urea per acre (30 days)',
            'fiber_development': 'Apply 20kg urea per acre (60 days)'
        }
    },
    'coffee': {
        'name': 'Coffee',
        'techniques': [
            'Shade management for optimal growth',
            'Regular pruning and sucker removal',
            'Integrated pest and disease management',
            'Processing immediately after harvest'
        ],
        'seed_per_acre': '1200-1500 plants',
        'yield_estimate': '500-1200 kg/acre',
        'growing_season': 'Perennial (3-4 years to production)',
        'optimal_conditions': {
            'temperature': '15-25°C',
            'rainfall': '1500-3000mm',
            'soil_ph': '6.0-6.5',
            'soil_type': 'Well-drained red loamy soil'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 10kg FYM + 500g NPK per plant',
            'flowering': 'Apply organic matter and micronutrients',
            'berry_development': 'Potash application for bean quality'
        }
    },
    'coconut': {
        'name': 'Coconut',
        'techniques': [
            'Plant dwarf or hybrid varieties',
            'Intercropping with compatible crops',
            'Regular application of organic matter',
            'Harvest mature nuts at proper intervals'
        ],
        'seed_per_acre': '65-80 plants',
        'yield_estimate': '8000-12000 nuts/acre',
        'growing_season': 'Perennial (5-6 years to production)',
        'optimal_conditions': {
            'temperature': '27-35°C',
            'rainfall': '1200-3000mm',
            'soil_ph': '5.2-8.0',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 40kg FYM + 2kg NPK per plant',
            'quarterly': 'Split application of fertilizers',
            'micronutrients': 'Annual application of Mg, B, Zn'
        }
    },
    'papaya': {
        'name': 'Papaya',
        'techniques': [
            'Plant tissue culture seedlings',
            'Provide wind protection',
            'Regular removal of lower leaves',
            'Harvest fruits at proper maturity'
        ],
        'seed_per_acre': '500-600 plants',
        'yield_estimate': '40000-60000 kg/acre',
        'growing_season': 'Perennial (8-10 months to production)',
        'optimal_conditions': {
            'temperature': '22-32°C',
            'rainfall': '1000-2000mm',
            'soil_ph': '6.0-7.0',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'monthly': 'Apply 100g urea + 50g DAP per plant',
            'flowering': 'Increase potash application',
            'fruiting': 'Apply micronutrients regularly'
        }
    },
    'orange': {
        'name': 'Orange',
        'techniques': [
            'Use grafted plants on suitable rootstock',
            'Proper spacing and canopy management',
            'Integrated pest management',
            'Harvest at proper color and sugar content'
        ],
        'seed_per_acre': '80-100 plants',
        'yield_estimate': '8000-15000 kg/acre',
        'growing_season': 'Perennial (3-4 years to production)',
        'optimal_conditions': {
            'temperature': '20-30°C',
            'rainfall': '1000-2000mm',
            'soil_ph': '6.0-7.5',
            'soil_type': 'Well-drained sandy loam'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 20kg FYM + 1.5kg NPK per plant',
            'flowering': 'Apply micronutrients for fruit set',
            'fruit_development': 'Potash for fruit quality'
        }
    },
    'apple': {
        'name': 'Apple',
        'techniques': [
            'High-density planting systems',
            'Regular pruning and training',
            'Integrated pest and disease management',
            'Cold storage for extended shelf life'
        ],
        'seed_per_acre': '200-400 plants',
        'yield_estimate': '8000-20000 kg/acre',
        'growing_season': 'Perennial (3-5 years to production)',
        'optimal_conditions': {
            'temperature': '10-25°C',
            'rainfall': '1000-1500mm',
            'soil_ph': '6.0-7.0',
            'soil_type': 'Well-drained loamy soil'
        },
        'fertilizer_schedule': {
            'annual': 'Apply 25kg FYM + 2kg NPK per plant',
            'flowering': 'Apply calcium and boron',
            'fruit_development': 'Balanced NPK with micronutrients'
        }
    }
}

def get_crop_info(crop_name):
    """Get comprehensive information for a specific crop"""
    crop_name_lower = crop_name.lower().strip()
    return CROP_DATABASE.get(crop_name_lower, None)

def get_all_crops():
    """Get list of all available crops"""
    return list(CROP_DATABASE.keys())