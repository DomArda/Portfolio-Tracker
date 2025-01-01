import streamlit
import portfolio_gen

streamlit.title("Dashboard")
streamlit.divider()

streamlit.header("**Portfolio Value**")
streamlit.header("£6026.42")
streamlit.divider()

streamlit.metric(label="Free Funds", value="£602.30", delta="£4.2 in Dividends", delta_color="off")
streamlit.metric(label="Invested", value="£4232", delta="+42.4%")
