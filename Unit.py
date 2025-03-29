import streamlit as st


# App Title:
st.title("🌍 Unit Convertor App")

# unit conversion:
conversion_types = ["Length","Weight","Temperature"]
# user choose conversion:
conversion_choice = st.selectbox("Choose Conversion Type:",conversion_types)

# Length conversion:

if conversion_choice == "Length":
    length_units = ["Meters","Kilometers","Feet","Inches","Centimeters"]
    input_value = st.number_input("Enter length Value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",length_units)
    to_unit = st.selectbox("To Unit:",length_units)

# conversion dict:
    length_conversion = {
        "Meters":1,
        "Kilometers":1000,
        "Feet":0.3048,
        "Inches":0.0254,
        "Centimeters":0.01,
    }
    
    # conversion logic:
    if st.button("Convert"):
     result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
     st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')


# weight conversion:
elif conversion_choice == "Weight":
    weight_units = ["Kilograms","Grams","Pounds","Ounces"]
    input_value = st.number_input("Enter Weight Value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",weight_units)
    to_unit = st.selectbox("To Unit:",weight_units)

    # conversion Dict:
    weight_conversion = {
        "Kilograms":1,
        "Grams":0.001,
        "Pounds":0.453592,
        "Ounces":0.0283495,
    }

    # conversion logic:
    if st.button("Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')


    # Temperature conversion:
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius","Fahrenhit","Kelvin"]
    input_value = st.number_input("Enter Temperature Value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From unit:",temperature_units)
    to_unit = st.selectbox("To Unit:",temperature_units)

    def convert_temperature(value, from_units, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenhit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenhit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value-32)* 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value -273.15
            elif to_unit == "Fahrenhit":
                return (value -273.15) * 9/5 +32
        return value
    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit,to_unit)
        st.success(f"{input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}")