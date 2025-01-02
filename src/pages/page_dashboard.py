import streamlit

streamlit.title("Dashboard - DEMO")
streamlit.divider()

streamlit.subheader("Good Morning!")
streamlit.markdown("US Markets are closed.")
streamlit.divider()

streamlit.header("**Portfolio Value**")

total_portfolio, total_investment, free_funds = streamlit.columns(3)
total_portfolio.metric(label="Total Portfolio", value="£6026.42", delta="+£1794.42 (42.4%)")
total_investment.metric(label="Invested", value="£4232", delta="£200 in realized gains.", delta_color="off")
free_funds.metric(label="Free Funds", value="£102.30", delta="£4.2 in Dividends.", delta_color="off")
