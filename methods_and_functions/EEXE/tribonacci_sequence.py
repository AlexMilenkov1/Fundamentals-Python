def print_tribonacci_sequence(n):
    sequence = [1, 1, 2]  # Initialize the sequence with the first three numbers
    print("1 1 2", end=" ")  # Print the first three numbers

    for i in range(3, n):
        tribonacci_num = sequence[i-1] + sequence[i-2] + sequence[i-3]
        sequence.append(tribonacci_num)
        print(tribonacci_num, end=" ")

    print()  # Print a new line at the end

# Example usage:
num = int(input())

print_tribonacci_sequence(num)
