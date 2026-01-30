Binance Futures Testnet Trading Bot (Python)
Overview

This project is a CLI-based Python trading bot built for Binance Futures Testnet (USDT-M).
It allows placing Market and Limit orders with proper input validation, structured code, logging, and robust error handling.

The project is developed as part of the Junior Python Developer – Crypto Trading Bot application task.

Objective

Place orders on Binance Futures Testnet (USDT-M)

Demonstrate clean, reusable backend design

Handle real-world API errors and edge cases

Provide clear CLI interaction and logging

Features

✅ Market and Limit order placement

✅ BUY and SELL side support

✅ Binance Futures Testnet (USDT-M)

✅ CLI-based input using argparse

✅ Input validation (side, type, quantity, price)

✅ Structured code (separate client, logic, validation, CLI)

✅ Detailed logging of API requests, responses, and errors

✅ Graceful exception handling

Tech Stack

Python 3.x

python-binance

argparse

logging

python-dotenv

Project Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance Futures Testnet client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
│
├── cli.py               # CLI entry point
├── requirements.txt
├── README.md
├── .env                 # Environment variables (ignored in Git)
└── logs/
    └── orders.log       # API request/response logs

Setup Instructions
1. Clone the Repository
git clone https://github.com/mehdialam20002/TRADING_BOT.git
cd TRADING_BOT

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret


⚠️ API keys are never committed to the repository.

Usage
Market Order (BUY)
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order (SELL)
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000

Output Details

The CLI prints:

Order request summary

Order response details:

orderId

status

executedQty

avgPrice (if available)

Final success or failure message

Logging

All API interactions are logged to:

logs/orders.log


Logs include:

Order request parameters

Raw API responses

Error messages and exceptions

Sample logs are included for:

One MARKET order

One LIMIT order

Error Handling

The application gracefully handles:

Invalid CLI inputs

Missing required parameters

Binance API errors (e.g. timestamp sync, minimum notional)

Network or SDK exceptions

Assumptions

Only USDT-M Futures are supported

Testnet environment only

No leverage or position management

No UI (CLI-based as required)

Notes

Binance Futures Market orders may initially return status NEW due to asynchronous execution.

Execution details may update after order placement, which is expected Futures behavior.

Submission

This repository is submitted as part of the Junior Python Developer – Crypto Trading Bot assignment.

Author

Mehdi Alam
GitHub: https://github.com/mehdialam20002