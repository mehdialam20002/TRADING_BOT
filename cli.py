import argparse
from urllib import response
from bot.orders import OrderService
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        print("\nPlacing order:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        service = OrderService()
        response = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\nFull API Response:")
        print(response)

    except Exception as e:
        print(f"\nOrder Failed ❌: {str(e)}")

if __name__ == "__main__":
    main()
