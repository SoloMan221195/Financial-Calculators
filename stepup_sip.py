import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("📈 Step-Up SIP Calculator")
st.write("A simple tool to calculate SIP maturity with an annual step-up percentage.")
sip = st.number_input("Monthly SIP (₹)", value=5000, min_value=100)
step_up = st.number_input("Annual Step-Up (%)", value=10, min_value=0)
rate = st.number_input("Expected Annual Return (%)", value=12, min_value=1)
years = st.number_input("Investment Duration (Years)", value=10, min_value=1)
def calculate_stepup_sip(sip, step_up, rate, years):
    monthly_rate = rate / 12 / 100
    step_up_factor = 1 + (step_up / 100)
    balance = 0
    yearly_values = []
    invested = 0
    for year in range(1, years + 1):
        yearly_sip = sip * (step_up_factor ** (year - 1))
        for _ in range(12):
            balance = balance * (1 + monthly_rate) + yearly_sip
            invested += yearly_sip
        yearly_values.append({"Year": year, "Portfolio Value": balance})
    df = pd.DataFrame(yearly_values)
    return df, invested, balance
df, invested, maturity = calculate_stepup_sip(sip, step_up, rate, years)
st.subheader("📊 Results")
st.write(f"**Total Invested:** ₹{invested:,.0f}")
st.write(f"**Maturity Amount:** ₹{maturity:,.0f}")
st.subheader("📈 Growth Chart")
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Portfolio Value"], marker="o")
plt.xlabel("Year")
plt.ylabel("Portfolio Value (₹)")
plt.grid(True)
st.pyplot(plt)