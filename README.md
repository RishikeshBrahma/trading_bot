#  Binance Futures Trading Bot (Testnet)

A robust, modular Python CLI application built to interact with the Binance Futures Testnet (USDT-M). This project demonstrates professional software engineering practices, including structured code, comprehensive logging, and an interactive user experience.

##  Features
- **Core Trading:** Place `MARKET` and `LIMIT` orders for both `BUY` and `SELL` sides.
- **Interactive CLI (Bonus):** Guided prompts with real-time validation and a formatted UI using the `click` library.
- **Robust Validation:** Local input verification for symbols, quantities, and prices to minimize API errors.
- **Detailed Logging:** All API requests, responses, and errors are captured in `logs/bot_activity.log`.
- **Error Handling:** Graceful management of network failures, insufficient margin, and exchange-specific filter errors.

---

##  Setup & Installation

### 1. Prerequisites
- Python 3.8 or higher
- Binance Futures Testnet API Key and Secret

### 2. Environment Setup
Clone the repository and navigate to the project directory:
```bash
cd trading_bot
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# source .venv/bin/activate    # On macOS/Linux
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configuration
Create a .env file in the root directory:

Code snippet
BINANCE_TESTNET_API_KEY=your_actual_api_key_here
BINANCE_TESTNET_API_SECRET=your_actual_secret_key_here
Note: The .env file is ignored by Git for security.

 How to Run
Launch the interactive bot by running:

Bash
python cli.py
Examples of Valid Inputs:
Market Order:

Symbol: BTCUSDT

Side: BUY

Type: MARKET

Quantity: 0.002 (Min. Notional > 100 USDT)

Limit Order:

Symbol: BTCUSDT

Side: BUY

Type: LIMIT

Quantity: 0.002

Price: 65000 (Must be near current market price)

Project Structure
Plaintext
trading_bot/
├── bot/
│   ├── client.py         # Binance client wrapper & authentication
│   ├── orders.py         # Order placement execution logic
│   ├── validators.py     # Business logic for input validation
│   └── logging_config.py # Centralized logging setup
├── logs/                 # Auto-generated directory for log files
├── cli.py                # Main entry point with Enhanced CLI UX
├── requirements.txt      # Project dependencies
└── README.md             # Documentation
 Assumptions
Min Notional: The bot assumes the user is aware of Binance's minimum order value (typically > 100 USDT on Testnet for BTC).

Connectivity: Requires an active internet connection to reach the Binance Testnet API.

Symbol Format: Symbols should be entered in the standard Binance format (e.g., BTCUSDT).

#Output / CLI :-
 python cli.py

========================================
 WELCOME TO TRADING BOT
========================================
Enter Symbol [BTCUSDT]:
Side (BUY/SELL) (BUY, SELL): BUY
Order Type (MARKET/LIMIT) (MARKET, LIMIT): LIMIT
Quantity: 0.002
Limit Price: 60000

========================================
 ORDER CONFIRMATION
========================================
  🔹 Symbol:   BTCUSDT
  🔹 Side:     BUY
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y

  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Type:     LIMIT
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y

[1/2] Connecting to Binance Testnet...
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y

[1/2] Connecting to Binance Testnet...
  🔹 Type:     LIMIT
  🔹 Quantity: 0.002
  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y

  🔹 Price:    60000.0

Do you want to proceed with this order? [Y/n]: y

[1/2] Connecting to Binance Testnet...
Do you want to proceed with this order? [Y/n]: y

[1/2] Connecting to Binance Testnet...
[2/2] Transmitting Order...

========================================
[1/2] Connecting to Binance Testnet...
[2/2] Transmitting Order...

========================================
 TRANSACTION RESULTS
========================================
[2/2] Transmitting Order...

========================================
 TRANSACTION RESULTS
========================================
 TRANSACTION RESULTS
========================================
✅ SUCCESS: Order Processed!
  ID:     12437887115
  Status: NEW
  Qty:    0.000
  Avg:    0.00