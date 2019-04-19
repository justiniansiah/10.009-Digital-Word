1. bool, tuple, None: The following problems test your knowledge of bool, tuple and NoneType
types; no need to write a program for these but you can verify your answer by writing
programs.

(a) What are the types of a and b?
    a =(1) #int
    b=(1 ,) #tuple
    
    
(b) List from the variables below those that will evaluate to False when converted to
bool.
    a='abc' #True
    b =0+0j #False
    c=(1 ,) #True
    d=''    #False
    e='None'#True
    f= None #False
    
    
(c) What will be the values of expressions at steps (a), (b) and (c) below?
    t=(1 ,2 ,3)
    t+t # (a)   #(1 ,2 ,3, 1 ,2 ,3)
    t*2 # (b)   #(1 ,2 ,3, 1 ,2 ,3)
    t[1: -1] # (c) #(2,)