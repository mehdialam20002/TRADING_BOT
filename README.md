Binance Futures Testnet Trading Bot (Python)
Overview

This repository contains a CLI-based Python trading bot built for Binance Futures Testnet (USDT-M).
The application allows users to place Market, Limit, and Stop-Limit orders with a clean, modular architecture, proper input validation, logging, and error handling.

This project was developed as part of the Junior Python Developer – Crypto Trading Bot application task.

Objective

Place orders on Binance Futures Testnet (USDT-M)

Support Market, Limit, and Stop-Limit orders

Provide a clean, reusable backend structure

Handle real-world Binance Futures API errors

Offer a clear CLI experience with logging and validation

Features
Core Features (Must-have)

✅ Market order placement

✅ Limit order placement

✅ BUY and SELL side support

✅ Binance Futures Testnet (USDT-M)

✅ CLI-based input using argparse

✅ Input validation (symbol, side, type, quantity, price)

✅ Clear order request & response output

✅ Structured codebase (separation of concerns)

✅ Detailed logging of API requests, responses, and errors

✅ Graceful exception handling

Bonus Features (Optional)

⭐ Stop-Limit order support (Futures-correct implementation)

⭐ Enhanced CLI UX

Interactive mode with prompts and choices

User-friendly validation messages

⭐ Lightweight UI

Simple Streamlit-based interface for order placement

Tech Stack

Python 3.x

python-binance

argparse

rich (enhanced CLI UX)

logging

python-dotenv

streamlit (lightweight UI – optional bonus)

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
├── ui.py                # Lightweight Streamlit UI (bonus)
├── requirements.txt
├── README.md
├── .env                 # Environment variables (ignored in Git)
└── logs/
    └── orders.log       # API request/response/error logs

Setup Instructions
1. Clone the Repository
git clone https://github.com/mehdialam20002/TRADING_BOT.git
cd TRADING_BOT

2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret


⚠️ API keys are stored only in environment variables and are not committed to Git.

Usage
Market Order (BUY)
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order (SELL)
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 90000

Stop-Limit Order (Bonus)
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT \
--quantity 0.002 --price 90000 --stop-price 89000

Interactive CLI Mode (Bonus)
python cli.py --interactive


Prompts user for inputs

Prevents invalid selections

Provides better UX for manual testing

Lightweight UI (Bonus)

Run the Streamlit-based UI:

streamlit run ui.py


The UI allows:

Symbol selection

Order type selection

Quantity, price, and trigger price inputs

Order placement with real-time feedback

Output Details

The CLI prints:

Order request summary

Order response details:

orderId

status

executedQty

avgPrice (if available)

Final success or failure message

Note: For Futures Market and Stop-Limit orders, some fields may initially be NEW or None due to asynchronous execution, which is expected behavior.

Logging

All API interactions are logged to:

logs/orders.log


Logs include:

Order request parameters

Raw Binance API responses

Error messages and exceptions

Sample logs are present for:

One Market order

One Limit order

One Stop-Limit order

Error Handling

The application gracefully handles:

Invalid CLI inputs

Missing required parameters

Invalid trading symbols

Binance API errors (e.g. timestamp sync, minimum notional)

Network or SDK-level exceptions

Assumptions

Only USDT-M Futures are supported

Binance Testnet environment only

No leverage or position management

No order cancellation or position closing logic

Focus is on order placement and robustness

Notes

Binance Futures Market orders may return status NEW initially due to asynchronous execution.

Stop-Limit orders are conditional and may not return a full order object until the trigger price is reached.

This behavior is expected and handled gracefully.

Submission

This repository is submitted as part of the Junior Python Developer – Crypto Trading Bot hiring assignment.

Author

Mehdi Alam
GitHub: https://github.com/mehdialam20002