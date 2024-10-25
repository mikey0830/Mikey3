def recaman_sequence(n):
    sequence = [0]  
    seen = {0}  
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
if __name__ == "__main__":
    sequence = recaman_sequence(32)  
    print(sequence)