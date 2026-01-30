import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API keys not found in environment variables")

        # Futures Testnet client
        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )

        # Futures Testnet base URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        # 🔥 Timestamp sync (required for Futures)
        server_time = self.client.futures_time()["serverTime"]
        local_time = int(time.time() * 1000)
        self.client.timestamp_offset = server_time - local_time

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)
