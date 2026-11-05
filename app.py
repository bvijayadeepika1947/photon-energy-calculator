
import streamlit as st
import pandas as pd

# Physical constants
h = 6.62607015e-34
c = 299792458
e = 1.602176634e-19

st.set_page_config(
    page_title="Photon Energy Calculator",
    page_icon="⚛️",
    layout="wide"
)

# Colourful design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #06143b, #102d68);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #071b55, #174b9b, #6025a8);
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    border: 2px solid #38c9ff;
    box-shadow: 0 0 20px #168bff;
}
.hero h1 {
    font-size: 38px;
    color: #ffffff !important;
}
.hero p {
    font-size: 18px;
}
.info-card {
    background: linear-gradient(135deg, #163d85, #422078);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #53cfff;
    margin: 10px 0;
}
.formula {
    background: #e9f1ff;
    color: #10245d;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 27px;
    font-weight: bold;
}
.rainbow {
    height: 35px;
    border-radius: 15px;
    background: linear-gradient(
        to right,
        violet, blue, cyan, lime, yellow, orange, red
    );
    margin: 15px 0;
}
.stButton button {
    background: linear-gradient(90deg, #673bff, #00aaff);
    color: white;
    border-radius: 15px;
    border: none;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <h1>⚛️ PHOTON ENERGY CALCULATOR</h1>
    <h3>A Python-Based Spectroscopy Project</h3>
    <p>✨ Discover the science of light and energy ✨</p>
    <div style="font-size:65px;">🔬 🌈 💡 ⚛️</div>
    <p>Small particles... Huge energy!</p>
</div>
""", unsafe_allow_html=True)

st.write("")

home, theory, calculator, applications, quiz = st.tabs([
    "🏠 Home",
    "📚 Theory",
    "🧮 Calculator",
    "🔬 Applications",
    "🎯 Quiz"
])

# HOME
with home:
    st.header("🌟 Welcome to the World of Photons!")

    st.markdown("""
    <div class="info-card">
    <h2>💡 What is a Photon?</h2>
    <p>A photon is a tiny packet of electromagnetic energy.
    Light consists of photons, and every photon carries energy.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🌈 Explore the colours of light")
    st.markdown('<div class="rainbow"></div>',
                unsafe_allow_html=True)

    st.write("Violet light has more energy than red light.")

    st.subheader("🎯 Project Objectives")
    st.markdown("""
    - Understand photon energy.
    - Learn Planck's equation.
    - Calculate energy using Python.
    - Understand the wavelength-energy relationship.
    - Explore applications in spectroscopy.
    """)

    st.info("Explore the tabs above to discover more!")

# THEORY
with theory:
    st.header("📚 Theory of Photon Energy")

    st.write("""
    Light is electromagnetic radiation. It travels in the form
    of energy packets called photons.
    """)

    st.markdown("""
    <div class="formula">
    E = hc / λ
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Meaning of the symbols")

    st.markdown("""
    - **E** = Energy of a photon (Joule)
    - **h** = Planck's constant
    - **c** = Speed of light
    - **λ** = Wavelength in metres
    """)

    st.subheader("Physical constants")

    st.write("Planck's constant:")
    st.latex(r"h = 6.626 \times 10^{-34}\ J\,s")

    st.write("Speed of light:")
    st.latex(r"c = 2.998 \times 10^8\ m/s")

    st.subheader("🔍 Important relationship")

    st.success("""
    Shorter wavelength → Higher photon energy

    Longer wavelength → Lower photon energy
    """)

    st.markdown("""
    <div class="info-card">
    <h3>🌈 Visible Light Spectrum</h3>
    <div class="rainbow"></div>
    <p>Violet: shorter wavelength and higher energy.</p>
    <p>Red: longer wavelength and lower energy.</p>
    </div>
    """, unsafe_allow_html=True)

# CALCULATOR
with calculator:
    st.header("🧮 Calculate Photon Energy")

    st.write("Enter the wavelength of light in nanometres.")

    wavelength = st.number_input(
        "Wavelength (nm)",
        min_value=1.0,
        max_value=100000.0,
        value=500.0,
        step=10.0
    )

    wavelength_m = wavelength * 1e-9
    frequency = c / wavelength_m
    energy_j = h * c / wavelength_m
    energy_ev = energy_j / e

    st.subheader("✨ Your Results")

    col1, col2 = st.columns(2)

    col1.metric("Energy (Joules)", f"{energy_j:.4e} J")
    col2.metric("Energy (eV)", f"{energy_ev:.4f} eV")

    st.metric("Frequency", f"{frequency:.4e} Hz")

    st.subheader("📝 Calculation")

    st.latex(r"E = \frac{hc}{\lambda}")

    st.write(
        f"Wavelength = {wavelength} nm "
        f"= {wavelength_m:.4e} m"
    )

    st.success(f"Photon energy = {energy_j:.4e} Joules")

    st.subheader("📈 Energy vs Wavelength Graph")

    wavelengths = list(range(380, 751, 10))

    energies = [
        (h * c / (x * 1e-9)) / e
        for x in wavelengths
    ]

    graph = pd.DataFrame({
        "Wavelength (nm)": wavelengths,
        "Energy (eV)": energies
    })

    st.line_chart(
        graph,
        x="Wavelength (nm)",
        y="Energy (eV)"
    )

    st.caption(
        "The graph shows that photon energy decreases "
        "when wavelength increases."
    )

# APPLICATIONS
with applications:
    st.header("🔬 Applications of Photon Energy")

    st.markdown("""
    <div class="info-card">
    <h3>🧪 1. Electronic Spectroscopy</h3>
    <p>Used to study electronic transitions in atoms
    and molecules when light is absorbed or emitted.</p>
    </div>
    <div class="info-card">
    <h3>✨ 2. Fluorescence</h3>
    <p>Some substances absorb light and emit light
    of a different wavelength.</p>
    </div>
    <div class="info-card">
    <h3>🏥 3. Medical Applications</h3>
    <p>Spectroscopic techniques help analyse biological
    samples and substances in medical research.</p>
    </div>
    <div class="info-card">
    <h3>☀️ 4. Solar Energy</h3>
    <p>Solar cells use light energy to produce
    electrical energy.</p>
    </div>
    """, unsafe_allow_html=True)

# QUIZ
with quiz:
    st.header("🎯 Test Your Chemistry Knowledge!")

    questions = [
        (
            "What is a photon?",
            ["A packet of light energy", "A proton", "A neutron"],
            "A packet of light energy"
        ),
        (
            "What is the photon energy formula?",
            ["E = mc", "E = hc/λ", "E = h + c"],
            "E = hc/λ"
        ),
        (
            "What happens when wavelength decreases?",
            ["Energy decreases", "Energy increases",
             "Energy stays the same"],
            "Energy increases"
        ),
        (
            "What is the SI unit of energy?",
            ["Metre", "Joule", "Hertz"],
            "Joule"
        ),
        (
            "Which light has higher energy?",
            ["Red", "Violet", "Both equal"],
            "Violet"
        )
    ]

    answers = []

    for i, (question, options, correct) in enumerate(questions):
        answer = st.radio(
            f"Q{i+1}. {question}",
            options,
            key=f"quiz_{i}"
        )
        answers.append(answer)

    if st.button("Submit My Answers"):
        score = sum(
            answers[i] == questions[i][2]
            for i in range(len(questions))
        )

        st.success(f"Your score: {score}/5")

        if score == 5:
            st.balloons()
            st.success("Excellent! You are a Photon Expert!")

        for i, answer in enumerate(answers):
            correct = questions[i][2]
            if answer == correct:
                st.write(f"Q{i+1}: Correct! ✅")
            else:
                st.write(
                    f"Q{i+1}: Correct answer: {correct}"
                )

st.divider()

st.markdown("""
<div class="hero">
<h3>💙 Thank You for Exploring!</h3>
<p>Engineering Chemistry | Python | Spectroscopy</p>
<p>Made with Python and Streamlit</p>
</div>
""", unsafe_allow_html=True)
        
