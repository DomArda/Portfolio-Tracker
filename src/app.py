import streamlit
from config import Config

# Streamlit entry point

# Session state
if "logged_in" not in streamlit.session_state:
    # This basically means whether the User has supplied API keys already.
    streamlit.session_state.logged_in = False

# Config States
if "ini" not in streamlit.session_state:
    streamlit.session_state.ini = Config.Ini()
if "json" not in streamlit.session_state:
    streamlit.session_state.json = Config.Json()

# Pages
login_page = streamlit.Page("pages/page_login.py", title="🔑 API Keys", default=True)
dashboard_page = streamlit.Page("pages/page_dashboard.py", title="📈 Dashboard")

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
