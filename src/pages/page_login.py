import streamlit

# Streamlit Page for Inputting API Keys, Private Keys, etc.

_Ini = streamlit.session_state.ini

streamlit.title("Login Page")

platform_select, api_key_input = streamlit.columns(2)
with platform_select:
    platform_option = streamlit.selectbox(
        "Select Broker / Exchange Platform",
        {"Trading212"},
        index=None,
    )

with api_key_input:
    if platform_option:
        input_API_key = streamlit.text_input(
            label="API Key",
            value=_Ini.get(platform_option)
        )

        if streamlit.button("Submit"):
            # streamlit.session_state.logged_in
            _Ini.set(platform_option, input_API_key)
            _Ini.write()

            streamlit.session_state.logged_in = True

            streamlit.rerun()

            # TODO
            # 1. Validate Key
            # 3. Generate a Portfolio
            # 4. Save to Config's Json


