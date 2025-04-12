import streamlit as st

# All supported conversions
conversion_data = {
    "Length": {
        "meter": 1,
        "centimetre": 100,
        "millimetre": 1000,
        "kilometer": 0.001,
        "foot": 3.28084,
        "mile": 0.000621371
    },
    "Weight": {
        "kg": 1,
        "gram": 1000,
        "pound": 2.20462
    },
    "Volume": {
        "liter": 1,
        "milliliter": 1000,
        "gallon": 0.264172
    },
    "Speed": {
        "mps": 1,
        "kmph": 3.6,
        "mph": 2.23694
    },
    "Pressure": {
        "pascal": 1,
        "bar": 1e-5,
        "psi": 0.000145038
    },
    "Time": {
        "second": 1,
        "minute": 1/60,
        "hour": 1/3600
    },
    "Temperature": {
        "celsius": "temp",
        "fahrenheit": "temp"
    }
}

# Temperature logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9

# Streamlit settings
st.set_page_config("Unit Converter", layout="centered")
st.markdown("## 🔄 Unit Converter")

# Select category and units
category = st.selectbox("Choose a category", list(conversion_data.keys()))
units = list(conversion_data[category].keys())

# Row 1: Input and Output values
col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    input_value = st.number_input(" ", value=1.0, step=0.1, label_visibility="collapsed")
with col2:
    st.markdown("<h2 style='text-align:center;'>=</h2>", unsafe_allow_html=True)
with col3:
    # Conversion logic
    if category == "Temperature":
        result = convert_temperature(input_value, units[0], units[1])
    else:
        base = input_value / conversion_data[category][units[0]]
        result = base * conversion_data[category][units[1]]

    formatted_result = f"{result:.4f}".rstrip('0').rstrip('.') if '.' in f"{result:.4f}" else f"{result:.4f}"
    st.text_input(" ", value=formatted_result, label_visibility="collapsed", disabled=True)

# Row 2: Units below values
col4, col5, col6 = st.columns([3, 1, 3])
with col4:
    from_unit = st.selectbox(" ", options=units, index=0, label_visibility="collapsed")
with col5:
    st.write(" ")
with col6:
    to_unit = st.selectbox("  ", options=units, index=1, label_visibility="collapsed")

# Formula section
st.markdown("---")
if category == "Temperature":
    if from_unit == to_unit:
        formula = "Same unit, no conversion"
    elif from_unit == "celsius":
        formula = "(°C × 9/5) + 32"
    else:
        formula = "(°F − 32) × 5/9"
else:
    multiplier = conversion_data[category][to_unit] / conversion_data[category][from_unit]
    formula = f"{input_value} × {multiplier:.4f} = {result:.4f}"

st.markdown(f"""
<div style='padding:10px; background-color:#fff3cd; border:1px solid #ffeeba; border-radius:5px;'>
<b>Formula:</b> {formula}
</div>
""", unsafe_allow_html=True)
