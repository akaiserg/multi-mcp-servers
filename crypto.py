from mcp.server.fastmcp import FastMCP
import requests
mcp = FastMCP("Crypto")


@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Gets the current price of a cryptocurrency.

    Args:
        crypto: symbol of the cryptocurrency to get the price of (e.g. 'bitcoin', 'ethereum').
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data.get(crypto.lower(),{}).get('usd')
        if price is not None:
            return f"The current price of {crypto} is ${price} USD"
        else:
            return f"Could not find the price for {crypto}"
    except Exception as e:
        return f"Error getting the price for {crypto}: {e}"

if __name__ == "__main__":
    mcp.run()