import logging
import os

def setup_logger():
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Create a custom logger
    logger = logging.getLogger('trading_bot')
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if the logger is called multiple times
    if not logger.handlers:
        # File handler to write logs to a file
        file_handler = logging.FileHandler('logs/bot_activity.log')
        file_handler.setLevel(logging.INFO)

        # Create formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

    return logger