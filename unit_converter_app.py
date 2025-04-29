import streamlit as st

st.title("🔄 Unit Converter App")

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'pounds': 453.592,
        'ounces': 28.3495,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        return value * 9/5 + 32 if to_unit == 'Fahrenheit' else value + 273.15
    elif from_unit == 'Fahrenheit':
        return (value - 32) * 5/9 if to_unit == 'Celsius' else (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        return value - 273.15 if to_unit == 'Celsius' else (value - 273.15) * 9/5 + 32

# Streamlit UI
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ["meters", "kilometers", "miles", "feet"]
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_length(value, from_unit, to_unit)
elif conversion_type == "Weight":
    units = ["grams", "kilograms", "pounds", "ounces"]
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_weight(value, from_unit, to_unit)
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter Value", format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    result = convert_temperature(value, from_unit, to_unit)

# Output
st.success(f"Converted value: {result:.2f} {to_unit}")
