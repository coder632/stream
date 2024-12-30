import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Simple Streamlit App")

# Sidebar for user input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("Enter your name", "Guest")
st.sidebar.write(f"Hello, {user_name}!")

# Slider for numeric input
num = st.sidebar.slider("Select a number", 1, 100, 50)

# Display the chosen number
st.write(f"You selected the number: {num}")

# Generate random data
st.subheader("Random Data Visualization")
data = pd.DataFrame(np.random.randn(100, 3), columns=['A', 'B', 'C'])

# Line chart
st.line_chart(data)

# Display raw data if checkbox is selected
if st.checkbox("Show raw data"):
    st.write(data)

# Generate and display a custom chart
st.subheader("Custom Matplotlib Chart")
fig, ax = plt.subplots()
ax.hist(data['A'], bins=20, color='blue', alpha=0.7)
ax.set_title("Histogram of Column A")
st.pyplot(fig)

# Text input and display
user_message = st.text_area("Leave a message")
if user_message:
    st.write(f"Your message: {user_message}")

# Button to trigger an action
if st.button("Click me!"):
    st.write("Button clicked!")

# Footer
st.write("Thanks for using this app!")
