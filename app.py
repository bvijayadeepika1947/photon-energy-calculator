import streamlit as st

# Physical constants
h = 6.62607015e-34
c = 299792458
e = 1.602176634e-19

st.set_page_config(
    page_title="Photon Energy Calculator",
    page_icon="⚛️"
)

st.title("⚛️ Photon Energy Calculator")

st.write(
    "Calculate the energy and frequency of a photon "
    "using its wavelength."
)

st.subheader("Enter Wavelength")

wavelength = st.number_input(
    "Wavelength (in nanometres)",
    min_value=1.0,
    value=500.0,
    step=10.0
)

# Convert nanometres into metres
wavelength_m = wavelength * 1e-9

# Calculate frequency and energy
frequency = c / wavelength_m
energy_j = h * frequency
energy_ev = energy_j / e

st.subheader("Calculation Results")

col1, col2 = st.columns(2)

with col1:
    st.metric("Energy (Joules)", f"{energy_j:.4e} J")

with col2:
    st.metric("Energy (eV)", f"{energy_ev:.4f} eV")

st.metric("Frequency", f"{frequency:.4e} Hz")

st.subheader("Formula Used")

st.latex(r"E = \frac{hc}{\lambda}")

st.write("Where:")
st.write("- E = Energy of photon")
st.write("- h = Planck's constant")
st.write("- c = Speed of light")
st.write("- λ = Wavelength in metres")

st.subheader("Energy vs Wavelength")

wavelengths = list(range(380, 751, 10))
energies = [
    (h * c / (x * 1e-9)) / e
    for x in wavelengths
]

chart_data = {
    "Wavelength (nm)": wavelengths,
    "Energy (eV)": energies
}

st.line_chart(
    chart_data,
    x="Wavelength (nm)",
    y="Energy (eV)"
)

st.info(
    "A shorter wavelength has higher photon energy, "
    "while a longer wavelength has lower photon energy."
)

st.success("Thank you for using our Photon Energy Calculator!")
