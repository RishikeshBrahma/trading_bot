def validate_symbol(symbol: str) -> str:
    return symbol.upper()

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity

def validate_price(price: float, order_type: str) -> float:
    if order_type.upper() == 'LIMIT' and price is None:
        raise ValueError("Price is strictly required for LIMIT orders.")
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0.")
    return price