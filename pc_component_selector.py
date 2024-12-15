import pandas as pd
import streamlit as st

# Load the CSV file
file_path = 'C:\\Users\\Dhari\\Desktop\\PC_Components_with_Budget.csv'
data = pd.read_csv(file_path)

# Streamlit app
def main():
    st.title("PC Component Selector")
    
    # Ask user for their purpose
    purpose = st.selectbox(
        "What is your primary use for the PC?",
        ["Gamer", "Editor", "Developer", "Casual User", "Other"]
    )
    
    # Ask user for their budget
    budget = st.number_input(
        "Enter your budget (in USD):",
        min_value=0,
        value=1000,
        step=100
    )
    
    # Filter components based on purpose and budget
    if st.button("Show Recommendations"):
        if "Purpose" in data.columns and "Budget" in data.columns:
            # Filter components based on user's purpose and budget
            filtered_data = data[
                (data["Purpose"].str.contains(purpose, case=False, na=False)) &
                (data["Budget"] <= budget)
            ]
            
            if not filtered_data.empty:
                st.subheader("Recommended Components:")
                st.dataframe(filtered_data)
            else:
                st.write("No components match your criteria. Try increasing your budget.")
        else:
            st.error("The uploaded file does not have the required columns: 'Purpose' and 'Budget'.")
        
# Run the app
if __name__ == "__main__":
    main()
