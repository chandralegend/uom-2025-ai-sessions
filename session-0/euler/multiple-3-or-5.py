def solve(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    # Example usage:
    print(solve(10))  # Output: 23
    print(solve(1000))  # Output: 233168