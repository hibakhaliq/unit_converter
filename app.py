import streamlit as st

#title

st.title("Unit Converter")

#unit converters
conversion_types = ["Length","Weight","Temprature"]

#choice
conversion_choice = st.selectbox ("Choose your conversion Type:",conversion_types)

if conversion_choice == "Length":
    length_units = ["Meters","Kilometers","Feet","Inches","Centimeters"]
    input_value = st.number_input("Enter your value to convert:",min_value=0.0,format="%.2f")
    from_unit = st.selectbox("From unit:",length_units)
    to_unit = st.selectbox("To unit:",length_units)

    #dictionary
    length_conversion = {
        "Meters":1,
        "Kilometers":1000,
        "Feet":0.3048,
        "Inches":0.0254,
        "Centimeters":0.01
    }

    #logic

    if st.button("Convert Length"):
        result = input_value * (length_conversion[from_unit]/length_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result} {to_unit}") 

 # weight conversion
  
elif conversion_choice == "Weight":
    weight_units = ["Kilograms","Grams","Pounds","Ounces"]
    input_value = st.number_input("Enter your value to convert:",min_value=0.0,format="%.2f")
    from_unit = st.selectbox("From unit:",weight_units)
    to_unit = st.selectbox("To unit:",weight_units)

    #dictionary
    weight_conversion = {
        "Kilograms":1,
        "Grams":0.001,
        "Pounds":0.453592,
        "Ounces":0.0283495
    }

    #logic
    if st.button("Convert Weight"):
        result = input_value * (weight_conversion[from_unit]/weight_conversion[to_unit])
        st.success(f"{input_value} {from_unit} is equal to {result} {to_unit}") 

 #temprature conversion
elif conversion_choice == "Temprature":
    temprature_units = ["Celsius","Fahrenheit","Kelvin"]
    input_value = st.number_input("Enter your value to convert:",min_value=0.0,format="%.2f")
    from_unit = st.selectbox("From unit:",temprature_units)
    to_unit = st.selectbox("To unit:",temprature_units)

    #logic
    def convert_temprature(value,from_unit,to_unit):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    

if st.button("Convert Temprature"):
    result = convert_temprature(input_value,from_unit,to_unit)
    st.success(f"{input_value} {from_unit} is equal to {result} {to_unit}")


