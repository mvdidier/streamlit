import streamlit as st

# Title and Introduction
st.title("Decision-Making Wizard for Web Components")
st.markdown("""
Welcome to the decision-making wizard. This tool will help you determine whether to **buy**, **reuse**, 
or **develop** a web component based on your specific needs and constraints.
""")

# Step 1: Define Component Requirements
st.header("Step 1: Define Requirements")
functionality = st.text_input("What functionality does the component need?")
complexity = st.radio("How complex is the functionality?", ("Low", "Medium", "High"))
urgency = st.radio("How urgent is the need for the component?", ("Low", "Medium", "High"))

# Step 2: Budget and Resources
st.header("Step 2: Assess Budget and Resources")
budget = st.number_input("What is your budget for the component? ($)", min_value=0)
team_expertise = st.radio("Does your team have expertise to develop the component?", ("Yes", "No"))
available_time = st.slider("How much time is available to develop or integrate the component? (weeks)", 1, 52, 4)

# Step 3: Explore Alternatives
st.header("Step 3: Evaluate Alternatives")
market_availability = st.radio("Is a similar component available in the market?", ("Yes", "No"))
reusability = st.radio("Can you reuse an existing component from another project?", ("Yes", "No"))

# Decision Logic
if st.button("Get Recommendation"):
    if complexity == "Low" and market_availability == "Yes":
        st.success("Recommendation: Buy a pre-built component to save time and effort.")
    elif reusability == "Yes" and team_expertise == "Yes":
        st.success("Recommendation: Reuse an existing component from your projects.")
    elif complexity == "High" and team_expertise == "No" and budget > 5000:
        st.success("Recommendation: Consider hiring a third-party to develop the component.")
    else:
        st.warning("Recommendation: Develop the component in-house if the team has expertise and sufficient time.")

# Optional Notes
st.header("Additional Notes")
st.text_area("Add any additional notes or considerations here.")
