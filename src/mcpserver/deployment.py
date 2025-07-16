from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MathCalculator")

@mcp.tool()
def add_numbers(number1: float, number2: float) -> str:
    """
    Adds two numbers together.
    
    Args:
        number1: First number to add
        number2: Second number to add
        
    Returns:
        String containing the calculation and result
    """
    try:
        result = number1 + number2
        return f"{number1} + {number2} = {result}"
    except Exception as e:
        return f"Error in addition: {e}"

@mcp.tool()
def subtract_numbers(number1: float, number2: float) -> str:
    """
    Subtracts the second number from the first number.
    
    Args:
        number1: The number to subtract from
        number2: The number to subtract
        
    Returns:
        String containing the calculation and result
    """
    try:
        result = number1 - number2
        return f"{number1} - {number2} = {result}"
    except Exception as e:
        return f"Error in subtraction: {e}"

@mcp.tool()
def multiply_numbers(number1: float, number2: float) -> str:
    """
    Multiplies two numbers together.
    
    Args:
        number1: First number to multiply
        number2: Second number to multiply
        
    Returns:
        String containing the calculation and result
    """
    try:
        result = number1 * number2
        return f"{number1} × {number2} = {result}"
    except Exception as e:
        return f"Error in multiplication: {e}"

@mcp.tool()
def divide_numbers(number1: float, number2: float) -> str:
    """
    Divides the first number by the second number.
    
    Args:
        number1: The number to be divided (dividend)
        number2: The number to divide by (divisor)
        
    Returns:
        String containing the calculation and result
    """
    try:
        if number2 == 0:
            return "Error: Division by zero is not allowed"
        
        result = number1 / number2
        return f"{number1} ÷ {number2} = {result}"
    except Exception as e:
        return f"Error in division: {e}"

@mcp.tool()
def calculate_percentage(value: float, percentage: float) -> str:
    """
    Calculates a percentage of a given value.
    
    Args:
        value: The base value
        percentage: The percentage to calculate (e.g., 25 for 25%)
        
    Returns:
        String containing the calculation and result
    """
    try:
        result = (value * percentage) / 100
        return f"{percentage}% of {value} = {result}"
    except Exception as e:
        return f"Error in percentage calculation: {e}"

@mcp.tool()
def calculate_power(base: float, exponent: float) -> str:
    """
    Calculates base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent (power)
        
    Returns:
        String containing the calculation and result
    """
    try:
        result = base ** exponent
        return f"{base}^{exponent} = {result}"
    except Exception as e:
        return f"Error in power calculation: {e}"

@mcp.tool()
def calculate_square_root(number: float) -> str:
    """
    Calculates the square root of a number.
    
    Args:
        number: The number to find the square root of
        
    Returns:
        String containing the calculation and result
    """
    try:
        if number < 0:
            return "Error: Cannot calculate square root of negative number"
        
        result = number ** 0.5
        return f"√{number} = {result}"
    except Exception as e:
        return f"Error in square root calculation: {e}"

@mcp.tool()
def perform_complex_calculation(expression: str) -> str:
    """
    Evaluates a mathematical expression safely.
    
    Args:
        expression: Mathematical expression as a string (e.g., "2 + 3 * 4")
        
    Returns:
        String containing the expression and result
    """
    try:
        # Remove any potentially dangerous functions/imports
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression.replace('**', '^')):
            return "Error: Expression contains invalid characters"
        
        # Replace ^ with ** for Python exponentiation
        safe_expression = expression.replace('^', '**')
        
        # Evaluate the expression safely
        result = eval(safe_expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except ZeroDivisionError:
        return "Error: Division by zero in expression"
    except Exception as e:
        return f"Error evaluating expression: {e}"

if __name__ == "__main__":
    mcp.run()
