def recaman_sequence(n):
   
    sequence = [0]
    seen = {0}  # Set to keep track of numbers already in sequence

    for k in range(1, n):
        previous = sequence[-1]
        next_num = previous - k
        
        if next_num > 0 and next_num not in seen:
            sequence.append(next_num)
            seen.add(next_num)
        else:
            next_num = previous + k
            sequence.append(next_num)
            seen.add(next_num)
    
    return sequence
n = int(input("Enter the length of the Recaman sequence: "))
sequence = recaman_sequence(n)