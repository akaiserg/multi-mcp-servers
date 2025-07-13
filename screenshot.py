from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image   
import pyautogui
import io

mcp = FastMCP("ScreenShot Demo")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Caputres the current screen and returns it as an image. Use this tool whenever the user needs a screenshot of their activity.
    """
    buffer = io.BytesIO()
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getvalue(),format="jpeg")



if __name__ == "__main__":
    mcp.run()