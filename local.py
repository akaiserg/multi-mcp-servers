from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")


@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.

    Args:
        content: The content of the note to append.
    
    """
    file_path = "notes.txt"
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Note appended to {file_path}"
    except Exception as e:
        return f"Error appending note: {e}"
    


@mcp.tool()
def read_notes_from_file() -> str:
    """
    Reads the notes from the user's local notes.
    """
    file_path = "notes.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found"
    except FileNotFoundError:
        return "No notes found"
    except Exception as e:
        return f"Error reading notes: {e}"
    

if __name__ == "__main__":
    mcp.run()