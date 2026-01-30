from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None,
        stop_price: float = None
    ):
        try:
            order_params = {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
            }

            if order_type == "MARKET":
                order_params["type"] = "MARKET"

            elif order_type == "LIMIT":
                order_params.update({
                    "type": "LIMIT",
                    "price": price,
                    "timeInForce": "GTC",
                })

            elif order_type == "STOP_LIMIT":
                # ✅ Correct Futures STOP-LIMIT
                order_params.update({
                    "type": "STOP",
                    "price": price,
                    "triggerPrice": stop_price,   # 🔥 Futures uses triggerPrice
                    "timeInForce": "GTC",
                })

            logger.info(f"Request: {order_params}")
            response = self.client.place_order(**order_params)
            logger.info(f"Response: {response}")

            return response

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise
