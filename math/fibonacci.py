
def fibonacci_generator(N):
    sequence = [0, 1]
    for i in range(N - 2):
        sequence.append(sequence[i] + sequence[i + 1])
    
    print(sequence)

fibonacci_generator() # Enter a number here
