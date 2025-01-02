import streamlit

streamlit.title("Login Page")

api_key_input = streamlit.text_input("Input Trading212 API Key")

if streamlit.button("Submit"):
    if api_key_input:
        # streamlit.session_state.logged_in

        streamlit.session_state.logged_in = True
        streamlit.rerun()

    else:
        streamlit.error("No API Key provided")