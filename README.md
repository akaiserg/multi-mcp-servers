# Multi-MCP Servers

A collection of Model Context Protocol (MCP) servers providing local note-taking and screenshot functionality.

## What is MCP?

The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect with external data sources and tools. MCP allows AI models to:

- Access real-time information from various sources
- Interact with external systems and APIs
- Maintain context across different applications
- Extend their capabilities through custom tools

This project implements multiple MCP servers that provide different tools, allowing AI assistants to take notes and capture screenshots from your local system.

## Overview

This project contains two MCP servers:

1. **LocalNotes** (`local.py`) - Manages notes stored in a local text file
2. **ScreenShot Demo** (`screenshot.py`) - Captures screenshots of your screen

Both servers can be used independently or together to enhance AI assistant capabilities with note-taking and visual capture functionality.

## Features

### LocalNotes Server
- **Add Notes**: Append new notes to your local notes file
- **Read Notes**: Retrieve all stored notes
- **Local Storage**: Notes are stored in a simple text file (`notes.txt`)
- **Error Handling**: Robust error handling for file operations

### ScreenShot Server
- **Screen Capture**: Take screenshots of your current screen
- **Image Processing**: Returns optimized JPEG images
- **Real-time Capture**: Captures whatever is currently displayed on screen

## Requirements

- Python 3.11 or higher
- MCP CLI package
- PyAutoGUI (for screenshot functionality)

## Installation

### Option 1: Direct Installation with uvx (Recommended)

You can run the MCP servers directly from the GitHub repository using uvx:

```bash
uvx --from git+https://github.com/akaiserg/multi-mcp-servers.git mcp-server
```

This will install and run the MathCalculator MCP server directly without needing to clone the repository.

### Option 2: Local Development Setup

1. Clone this repository:
```bash
git clone https://github.com/akaiserg/multi-mcp-servers.git
cd multi-mcp-servers
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

## Usage

### Running the MCP Servers

#### Using uvx (Recommended)
To run the MathCalculator MCP server directly from GitHub:
```bash
uvx --from git+https://github.com/akaiserg/multi-mcp-servers.git mcp-server
```

#### Local Development - Individual Servers
To run specific servers locally during development:

**LocalNotes Server:**
```bash
python local.py
```

**ScreenShot Server:**
```bash
python screenshot.py
```

**Crypto Server:**
```bash
python crypto.py
```

**Prompt Server:**
```bash
python prompt.py
```

**MathCalculator Server:**
```bash
python src/mcpserver/deployment.py
```

Each server will start and listen for MCP protocol communications on separate instances.

### Available Tools

#### LocalNotes Server Tools

##### 1. `add_note_to_file`
- **Description**: Appends content to your local notes file
- **Parameter**: `content` (string) - The note content to append
- **Returns**: Success/error message

**Example Usage:**
```
AI Assistant: "I'll save this important information for you."
Tool Call: add_note_to_file("Meeting notes: Discussed project timeline, deadline is Dec 15th")
Response: "Note appended to notes.txt"
```

##### 2. `read_notes_from_file`
- **Description**: Reads all notes from your local notes file
- **Parameters**: None
- **Returns**: All stored notes or "No notes found" if empty

**Example Usage:**
```
AI Assistant: "Let me check your saved notes."
Tool Call: read_notes_from_file()
Response: "my note
Meeting notes: Discussed project timeline, deadline is Dec 15th"
```

#### ScreenShot Server Tools

##### 1. `capture_screenshot`
- **Description**: Captures the current screen and returns it as an image
- **Parameters**: None
- **Returns**: JPEG image of the current screen

**Example Usage:**
```
AI Assistant: "I'll take a screenshot of your current screen."
Tool Call: capture_screenshot()
Response: [Returns optimized JPEG image of the screen]
```

### Integration with MCP Clients

Both servers can be integrated with any MCP-compatible client. Here are some examples:

#### Claude Desktop Integration

**Option 1: Using uvx (Recommended)**
Add the MCP server to your Claude Desktop configuration using uvx:
```json
{
  "mcpServers": {
    "math-calculator": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/akaiserg/multi-mcp-servers.git", "mcp-server"]
    }
  }
}
```

**Option 2: Local Development Setup**
Add servers to your Claude Desktop MCP configuration for local development:
```json
{
  "mcpServers": {
    "local-notes": {
      "command": "python",
      "args": ["/path/to/your/project/local.py"]
    },
    "screenshot": {
      "command": "python",
      "args": ["/path/to/your/project/screenshot.py"]
    },
    "math-calculator": {
      "command": "python",
      "args": ["/path/to/your/project/src/mcpserver/deployment.py"]
    }
  }
}
```

#### Example Conversation with AI Assistant
```
User: "Can you save a note about my grocery list and then take a screenshot?"
AI: "I'll save that note for you and capture a screenshot of your current screen."
[AI calls add_note_to_file("Grocery list: milk, bread, eggs, apples")]
[AI calls capture_screenshot()]
AI: "I've saved your grocery list to your local notes and captured a screenshot of your screen!"

User: "What notes do I have saved?"
AI: "Let me check your saved notes."
[AI calls read_notes_from_file()]
AI: "Here are your saved notes: 
- my note
- Grocery list: milk, bread, eggs, apples"
```

## File Structure

```
multi-mcp-servers/
├── local.py          # LocalNotes MCP server implementation
├── screenshot.py     # ScreenShot MCP server implementation
├── main.py           # Basic entry point
├── notes.txt         # Local notes storage
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
├── .gitignore       # Git ignore patterns
├── .python-version  # Python version specification
└── README.md        # This file
```

## Development

### Project Structure

- `local.py`: Contains the LocalNotes MCP server implementation using FastMCP
- `screenshot.py`: Contains the ScreenShot MCP server implementation using FastMCP and PyAutoGUI
- `main.py`: Basic Python entry point (template)
- `notes.txt`: Local file where notes are stored
- `pyproject.toml`: Project configuration and dependencies

### Dependencies

The project depends on:
- `mcp[cli]>=1.11.0`: Model Context Protocol implementation
- `pyautogui>=0.9.54`: Screen capture functionality

### Extending the Servers

You can easily add more tools to either server by adding new functions with the `@mcp.tool()` decorator:

#### Adding a tool to LocalNotes:
```python
@mcp.tool()
def clear_notes() -> str:
    """Clears all notes from the file."""
    try:
        with open("notes.txt", "w", encoding="utf-8") as f:
            f.write("")
        return "All notes cleared"
    except Exception as e:
        return f"Error clearing notes: {e}"
```

#### Adding a tool to ScreenShot:
```python
@mcp.tool()
def capture_region_screenshot(x: int, y: int, width: int, height: int) -> Image:
    """Captures a specific region of the screen."""
    buffer = io.BytesIO()
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    return Image(data=buffer.getvalue(), format="jpeg")
```

### Creating Additional MCP Servers

You can create new MCP servers by following the same pattern:

1. Import FastMCP
2. Create an instance with a unique name
3. Add tools using the `@mcp.tool()` decorator
4. Run the server with `mcp.run()`

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

[Add your license information here]

## Support

[Add support information here]
