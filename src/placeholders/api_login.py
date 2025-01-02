import streamlit

streamlit.title("Platform API Input - DEMO")
streamlit.divider()

platform_select, api_key_input = streamlit.columns(2)

with platform_select:
    platform_option = streamlit.selectbox(
        "Select Broker / Exchange Platform",
        {"Trading212", "Kraken"},
        index=None,
        placeholder="Select here",
    )

with api_key_input:
    if platform_option == "Kraken":
        input_API_key = streamlit.text_input("Input API Key")
        input_private_key = streamlit.text_input("Input Private Key")

        if streamlit.button("Submit"):
            if not input_API_key:
                streamlit.error("API Key is required!")

            if not input_private_key:
                streamlit.error("Private Key is required!")

            if input_API_key and input_private_key:
                streamlit.success("API Key and Private Key are correct!")

    elif platform_option:
        input_API_key = streamlit.text_input("Input API Key")

        if streamlit.button("Submit"):
            if input_API_key:
                streamlit.success(f"API Key is correct!")

            else:
                streamlit.error("API Key is required!")
