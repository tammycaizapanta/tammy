def disco(de,a):
    print("mover disco de torre",de,"a torre",a)

def torreHanoi(torre,A, C, B):
    if torre >= 1:
        torreHanoi(torre-1,A,B,C)
        disco(A,C)
        torreHanoi(torre-1,B,C,A)

torreHanoi(3,"A","B","C")