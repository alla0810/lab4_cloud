import json

def process_emission_data(data):
    """Process vehicle emission data and calculate max CO2 values."""
    try:
        if 'vehicle_CO2' not in data:
            return {
                'status': 'error',
                'message': 'Missing CO2 data in the input',
                'max_CO2': None
            }

        co2_data = data['vehicle_CO2']

        if isinstance(co2_data, list):
            max_co2 = max(co2_data)
        else:
            max_co2 = float(co2_data)

        status = get_emission_status(max_co2)

        return {
            'status': status,
            'max_CO2': max_co2,
            'timestamp': data.get('timestamp', None),
            'vehicle_id': data.get('vehicle_id', None)
        }

    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error processing data: {str(e)}',
            'max_CO2': None
        }

def get_emission_status(co2_level):
    """Determine the emission status based on CO2 level."""
    if co2_level < 200:
        return 'good'
    elif co2_level < 350:
        return 'normal'
    elif co2_level < 500:
        return 'elevated'
    else:
        return 'critical'

# For testing
if __name__ == "__main__":
    test_data = {
        'vehicle_id': 'car001',
        'timestamp': '2023-11-09T14:30:00Z',
        'vehicle_CO2': [220, 350, 180, 420]
    }

    result = process_emission_data(test_data)
    print(json.dumps(result, indent=2))
