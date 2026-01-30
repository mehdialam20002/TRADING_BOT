import streamlit as st
from bot.orders import OrderService

st.title("Binance Futures Testnet Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
quantity = st.number_input("Quantity", min_value=0.001)

price = stop_price = None
if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input("Limit Price", min_value=1.0)
if order_type == "STOP_LIMIT":
    stop_price = st.number_input("Stop Price", min_value=1.0)

if st.button("Place Order"):
    service = OrderService()
    res = service.place_order(
        symbol, side, order_type, quantity, price, stop_price
    )
    st.success(res)
