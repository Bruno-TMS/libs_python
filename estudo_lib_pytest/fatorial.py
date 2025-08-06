def fatorial(n):
    if n < 0:
        return 0
    
    seq_desc = (x for x in range(n, 0, -1))
    
    fatorial = 1
    
    for x in seq_desc:
        fatorial *= x
    
    return fatorial

if __name__ == '__main__':
    fat = fatorial(5)
    print (fat)