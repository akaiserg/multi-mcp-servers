#!/usr/bin/env python3
"""
Test script to demonstrate how to use the math calculator functions
"""

# Import the functions from deployment.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'mcpserver'))

from deployment import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

def test_add_numbers():
    print("=== Testing add_numbers ===")
    
    # Test with 2 numbers (only accepts 2 now)
    print(add_numbers(5, 3))
    
    # Test with different numbers
    print(add_numbers(10, 5))
    
    # Test with decimal numbers
    print(add_numbers(2.5, 3.7))
    
    # Test with negative numbers
    print(add_numbers(-5, 10))
    
    # Test with zero
    print(add_numbers(0, 15))
    
    print()

def test_subtract_numbers():
    print("=== Testing subtract_numbers ===")
    
    # Test basic subtraction (only accepts 2 now)
    print(subtract_numbers(10, 3))
    
    # Test with different numbers
    print(subtract_numbers(20, 5))
    
    # Test with decimals
    print(subtract_numbers(15.5, 3.2))
    
    # Test with negative result
    print(subtract_numbers(5, 10))
    
    print()

def test_multiply_numbers():
    print("=== Testing multiply_numbers ===")
    
    # Test with 2 numbers (only accepts 2 now)
    print(multiply_numbers(4, 5))
    
    # Test with different numbers
    print(multiply_numbers(2, 3))
    
    # Test with decimals
    print(multiply_numbers(2.5, 4))
    
    # Test with zero
    print(multiply_numbers(7, 0))
    
    print()

def test_divide_numbers():
    print("=== Testing divide_numbers ===")
    
    # Test basic division (only accepts 2 now)
    print(divide_numbers(20, 4))
    
    # Test with different numbers
    print(divide_numbers(100, 5))
    
    # Test with decimals
    print(divide_numbers(15.6, 2.4))
    
    # Test division by zero (should show error)
    print(divide_numbers(10, 0))
    
    # Test fractional result
    print(divide_numbers(7, 3))
    
    print()

if __name__ == "__main__":
    print("Math Calculator Function Tests\n")
    
    test_add_numbers()
    test_subtract_numbers() 
    test_multiply_numbers()
    test_divide_numbers()
    
    print("=== Interactive Example ===")
    print("You can call functions like this:")
    print("add_numbers(15, 25)")
    print("Result:", add_numbers(15, 25)) 