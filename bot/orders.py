from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

# Initialize logger
logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol}...")
        
        # Base parameters required for all orders
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity,
        }
        
        # Limit orders require both a price and a timeInForce parameter
        if order_type == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC' 
            
        # Execute the futures order
        response = client.futures_create_order(**params)
        
        logger.info(f"Order placed successfully. Order ID: {response.get('orderId')}")
        return response
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Error while placing order: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error while placing order: {e}")
        return None