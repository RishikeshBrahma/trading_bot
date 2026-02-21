import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

# Initialize logger
logger = setup_logger()

def get_binance_client():
    # Load environment variables from the .env file
    load_dotenv()
    
    api_key = os.getenv('BINANCE_TESTNET_API_KEY')
    api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')
    
    if not api_key or not api_secret:
        logger.error("API keys not found. Please check your .env file.")
        raise ValueError("Missing Binance API credentials.")

    try:
        logger.info("Initializing connection to Binance Futures Testnet...")
        # The testnet=True flag routes calls to the testnet URL
        client = Client(api_key, api_secret, testnet=True)
        
        # Ping the server to verify the network connection
        client.ping()
        logger.info("Successfully connected to the Binance Futures Testnet.")
        
        return client
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Error during initialization: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during client setup: {e}")
        raise