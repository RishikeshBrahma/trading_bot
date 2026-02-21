import click
import time
from bot.client import get_binance_client
from bot.orders import place_order
from bot.validators import (
    validate_symbol, validate_side, validate_order_type,
    validate_quantity, validate_price
)

def print_header(text):
    click.echo(click.style(f"\n{'='*40}", fg='cyan'))
    click.echo(click.style(f" {text}", fg='cyan', bold=True))
    click.echo(click.style(f"{'='*40}", fg='cyan'))

@click.command()
def main():
    """Binance Futures Interactive Trading Bot"""
    print_header("WELCOME TO TRADING BOT")

    try:
        
        symbol = click.prompt(
            click.style("Enter Symbol", fg='yellow'), 
            default="BTCUSDT", 
            type=str
        ).upper()
        
        side = click.prompt(
            click.style("Side (BUY/SELL)", fg='yellow'), 
            type=click.Choice(['BUY', 'SELL'], case_sensitive=False)
        ).upper()
        
        order_type = click.prompt(
            click.style("Order Type (MARKET/LIMIT)", fg='yellow'), 
            type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False)
        ).upper()
        
        quantity = click.prompt(
            click.style("Quantity", fg='yellow'), 
            type=float
        )
        
        price = None
        if order_type == 'LIMIT':
            price = click.prompt(
                click.style("Limit Price", fg='yellow'), 
                type=float
            )

        
        print_header("ORDER CONFIRMATION")
        click.echo(f"  🔹 Symbol:   {click.style(symbol, bold=True)}")
        click.echo(f"  🔹 Side:     {click.style(side, fg='green' if side == 'BUY' else 'red')}")
        click.echo(f"  🔹 Type:     {order_type}")
        click.echo(f"  🔹 Quantity: {quantity}")
        if price:
            click.echo(f"  🔹 Price:    {price}")

        if not click.confirm(click.style('\nDo you want to proceed with this order?', fg='magenta', bold=True), default=True):
            click.secho("\n Order Aborted by User.", fg='red')
            return

        
        click.echo(click.style("\n[1/2] Connecting to Binance Testnet...", fg='blue'))
        client = get_binance_client()
        
        click.echo(click.style("[2/2] Transmitting Order...", fg='blue'))
        response = place_order(client, symbol, side, order_type, quantity, price)

        
        print_header("TRANSACTION RESULTS")
        if response:
            click.secho(" SUCCESS: Order Processed!", fg='green', bold=True)
            click.echo(f"  ID:     {response.get('orderId')}")
            click.echo(f"  Status: {response.get('status')}")
            click.echo(f"  Qty:    {response.get('executedQty')}")
            if response.get('avgPrice'):
                click.echo(f"  Avg:    {response.get('avgPrice')}")
        else:
            click.secho(" FAILURE: Order Rejected.", fg='red', bold=True)
            click.echo("Check 'logs/bot_activity.log' for the API error details.")

    except Exception as e:
        click.secho(f"\n Unexpected Error: {e}", fg='red')

if __name__ == '__main__':
    main()