import argparse
from rich.console import Console
from rich.prompt import Prompt, FloatPrompt

from bot.orders import OrderService
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

console = Console()

def interactive_mode():
    symbol = Prompt.ask("Symbol", default="BTCUSDT")
    side = Prompt.ask("Side", choices=["BUY", "SELL"])
    order_type = Prompt.ask("Order Type", choices=["MARKET", "LIMIT", "STOP_LIMIT"])
    quantity = FloatPrompt.ask("Quantity")

    price = stop_price = None
    if order_type in ["LIMIT", "STOP_LIMIT"]:
        price = FloatPrompt.ask("Limit Price")
    if order_type == "STOP_LIMIT":
        stop_price = FloatPrompt.ask("Stop Trigger Price")

    return symbol, side, order_type, quantity, price, stop_price


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)
    parser.add_argument("--interactive", action="store_true")

    args = parser.parse_args()

    try:
        if args.interactive:
            symbol, side, order_type, quantity, price, stop_price = interactive_mode()
        else:
            missing = []
            if not args.symbol: missing.append("symbol")
            if not args.side: missing.append("side")
            if not args.type: missing.append("type")
            if not args.quantity: missing.append("quantity")

            if missing:
                raise ValueError(
                    f"Missing required arguments: {', '.join(missing)}"
                )

            symbol = args.symbol
            side = args.side
            order_type = args.type
            quantity = args.quantity
            price = args.price
            stop_price = args.stop_price

        # ✅ Validations
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        if order_type == "STOP_LIMIT" and not stop_price:
            raise ValueError("stop-price is required for STOP_LIMIT orders")

        console.print("\n[bold]Placing order:[/bold]")
        console.print(f"Symbol: {symbol}")
        console.print(f"Side: {side}")
        console.print(f"Type: {order_type}")
        console.print(f"Quantity: {quantity}")
        if price:
            console.print(f"Price: {price}")
        if stop_price:
            console.print(f"Trigger Price: {stop_price}")

        service = OrderService()
        response = service.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price,
        )

        console.print("\n[green bold]Order Successful ✅[/green bold]")
        console.print(f"Order ID: {response.get('orderId')}")
        console.print(f"Status: {response.get('status')}")
        console.print(f"Executed Qty: {response.get('executedQty')}")
        console.print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        console.print(f"\n[red bold]Order Failed ❌: {str(e)}[/red bold]")


if __name__ == "__main__":
    main()
