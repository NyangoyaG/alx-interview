#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0  # If n is 1, we already have 1 H character.
    
    operations = [0] * (n + 1)  # Initialize an array to store the minimum operations for each position.
    
    for i in range(2, n + 1):
        operations[i] = float('inf')  # Set an initial large value as a placeholder.
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)
    
    return operations[n]

# Example usage:
n = 9
print(minOperations(n))  # Output: 6

