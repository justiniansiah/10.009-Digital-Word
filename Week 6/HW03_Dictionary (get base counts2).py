import string
UpperCase = string.ascii_uppercase

def get_base_counts2(DNA):
    dna = list(DNA)
    a = c = g = t = 0
    for i in range(len(dna)):
        if dna[i] in UpperCase:
            if dna[i] == "A":
                a+=1
            elif dna[i] == "C":
                c+=1
            elif dna[i] == "G":
                g+=1
            elif dna[i] == "T":
                t+=1
        else:
            return "The input DNA string is invalid"
    dna_dict = {'A': a, 'C': c, 'G': g, 'T': t}    
    return dna_dict
    
    
print get_base_counts2('AAACCGGTT') #{'A': 3,'C': 2, 'G': 2, 'T': 2}
print get_base_counts2('CcCCCGGGTDDDTT') #"The input DNA string is invalid"
print get_base_counts2('AAAGGIII')#{'A': 3,'C': 0, 'G': 2, 'T': 0}
print get_base_counts2('ADLSTTLLD') #{'A': 1,'C': 0, 'G': 0, 'T': 2}
print get_base_counts2('AAAABBABCCGGGA') #{'A': 6,'C': 2, 'G': 3, 'T': 0}
    


