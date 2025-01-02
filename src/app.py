import streamlit

# Streamlit entry point

# Session state
if "logged_in" not in streamlit.session_state:
    # This basically means whether the User has supplied API keys already.
    streamlit.session_state.logged_in = False

# Pages
login_page = streamlit.Page("pages/page_login.py", title="API Keys.", default=True)
dashboard_page = streamlit.Page("pages/page_dashboard.py", title="Dashboard")

# Login Logic
if streamlit.session_state.logged_in:
    page = streamlit.navigation(
        {
            "Settings" : [login_page],
            "Account" : [dashboard_page],
        }
    )

else:
    # Has not supplied any API Keys
    page = streamlit.navigation([login_page])

page.run()
