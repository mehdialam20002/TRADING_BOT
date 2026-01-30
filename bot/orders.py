from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(
                f"Request: symbol={symbol}, side={side}, type={order_type}, "
                f"quantity={quantity}, price={price}"
            )

            order_params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                order_params["price"] = price
                order_params["timeInForce"] = "GTC"

            response = self.client.place_order(**order_params)

            logger.info(f"Response: {response}")
            return response

        except Exception as e:
            logger.error(f"Order failed: {str(e)}")
            raise
