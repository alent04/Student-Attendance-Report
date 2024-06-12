import streamlit as st

# Load secrets
st.secrets["username"] = st.secrets["username"]
st.secrets["password"] = st.secrets["password"]

# Function to check login credentials
def authenticate(username, password):
    correct_username = st.secrets["username"]
    correct_password = st.secrets["password"]
    return username == correct_username and password == correct_password

# Main function for the login page
def login(secrets):
    st.title("Login to Your App")
    
    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Check if login button is clicked
    if st.button("Login"):
        if authenticate(username, password, secrets):
            st.success("Login successful! Redirecting to main app...")
            # Redirect to main app
            # Replace 'main_app_url' with the URL of your main app
            st.experimental_set_query_params(login=True)
        else:
            st.error("Invalid username or password. Please try again.")

def main():
    # Load secrets
    try:
        secrets = {
            "username": st.secrets["username"],
            "password": st.secrets["password"]
        }
    except KeyError:
        st.error("Could not find secrets. Please make sure they are added to Streamlit Cloud app settings.")
        return
    
    if "login" not in st.query_params:
        login(secrets)
    else:
        # Redirect to main app
        # Replace 'mew.py' with the filename of your main app
        import index

if __name__ == "__main__":
    main()
