from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Returns an overview of the inventory.
    """
    overview = """
    Inventory Overview:
    - Coffee
    - Tea
    - Water
    - Soda
    - Juice
    - Beer
    - Wine
    - Spirits
    - Snacks
    """
    return overview.strip()
