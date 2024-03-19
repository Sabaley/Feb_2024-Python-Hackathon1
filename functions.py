def fibonacci(n):
    
    if n <= 1:
        return [0] if n == 1 else []
    else:
        a, b = 0, 1
        fibonacci_sequence = [0, 1]
        for _ in range(2, n):
            c = a + b
            a, b = b, c
            fibonacci_sequence.append(c)
        return fibonacci_sequence


num_terms = int(input("Enter the number of terms: "))

fibonacci_sequence = fibonacci(num_terms)

print(fibonacci_sequence)
