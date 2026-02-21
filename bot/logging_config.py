import logging
import os

def setup_logger():
    
    if not os.path.exists('logs'):
        os.makedirs('logs')

    
    logger = logging.getLogger('trading_bot')
    logger.setLevel(logging.INFO)

    # Prevent adding multiple handlers if the logger is called multiple times
    if not logger.handlers:
       
        file_handler = logging.FileHandler('logs/bot_activity.log')
        file_handler.setLevel(logging.INFO)

       
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        
        logger.addHandler(file_handler)

    return logger