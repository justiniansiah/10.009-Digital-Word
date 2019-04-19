def factors(n):
    list = []
    for i in range(1,n+1):
        list.append(i)
        
    out = []    
    for i in list:
        if n%i == 0:
            out.append(i)
            
    return out
    
print factors(6) #[1, 2, 3, 6]
print factors(12) #[1, 2, 3, 4, 6, 12]
print factors(7) #[1, 7]
print factors(15) #[1, 3, 5, 15]
print factors(21) #[1, 3, 7, 21]
print factors(1) #[1]
print factors(9) #[1, 3, 9]