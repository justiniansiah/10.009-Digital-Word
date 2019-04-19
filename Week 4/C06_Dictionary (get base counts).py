def get_base_counts(DNA):
    dna = list(DNA)
    a = c = g = t = 0
    for i in range(len(dna)):
        if dna[i] == "A":
            a+=1
        elif dna[i] == "C":
            c+=1
        elif dna[i] == "G":
            g+=1
        elif dna[i] == "T":
            t+=1
        else:
            return 'The input DNA string is invalid'
    dna_dict = {'A': a, 'C': c, 'G': g, 'T': t}
    if a == 0:
        del dna_dict["A"]
    if c == 0:
        del dna_dict["C"]
    if g == 0:
        del dna_dict["G"]
    if t == 0:
        del dna_dict["T"]
    
    return dna_dict
    
print get_base_counts('AACCGT') #{'A': 2,'C': 2, 'G': 1, 'T': 1}
print get_base_counts('AAB') #"The input DNA string is invalid"
print get_base_counts('AaCaGT')#"The input DNA string is invalid"
print get_base_counts('A') #{'A': 1}