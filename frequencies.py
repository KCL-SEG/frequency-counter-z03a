"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        frequencies[str(item)] = 0
        
    for it in items:
        frequencies[str(it)] += 1
            
    return frequencies


