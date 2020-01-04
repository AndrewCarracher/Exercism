def distance(strand_a, strand_b):
    dna_strand_a = split_string(strand_a)
    dna_strand_b = split_string(strand_b)

    count_distance = 0
    incremental_counter = 0 
    

    if len(strand_a) != len(strand_b):
        raise ValueError('not of equal length')
    else:
                
        for letter_a in dna_strand_a:
            if letter_a != dna_strand_b[incremental_counter]:
                count_distance = count_distance + 1
            incremental_counter = incremental_counter + 1    

        return count_distance

def split_string(string_in):
    return [char for char in string_in]
