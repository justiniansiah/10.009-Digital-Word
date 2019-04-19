# Lists: The following problems test your knowledge of lists in Python; no need to write a
# program for these but you can verify your answers by writing programs.

# (a) Specify the value of x[0] after the following code snippet. (Ans = 1)
    x=[1 ,2 ,3]
    x [0]=0
    y=x
    y [0]=1
    
#     
#     
# (b) Specify the value of x[0] after the following code snippet. (Ans = a)
    x=[1 ,2 ,3]
    def f(l):
        l[0]= 'a'
    f(x)
    print x[0]
    
    
# (c) What is the value of a[0][0][0][0] after executing the following code snippet?
#     Write `E' if there are any errors. (Ans = 1)
    x=[1 ,2 ,3]
    y=[x]
    a=[y,x]
    y [0][0] = (1 ,2)
    print a[0][0][0][0]

   ##   y [0][0] = (1 ,2)
    # print a
#     
#     
# (d) Specify the values of expressions (a), (b), (c) and (d) in the following code. Ans = (0,0,0,1)
    x=[1 ,2 ,3]
    y1 =[x ,0]
    y2=y1 [:]
    y2 [0][0]=0
    y2 [1]=1
    print y1 [0][0] # (a)
    print y1 [1] # (b)
    print y2 [0][0] # (c)
    print y2 [1] # (d)
#     
#     
# (e) Specify the values of expressions (a), (b), (c) and (d) in the following code. Ans = (1,0,0,1)
    import copy
    x=[1 ,2 ,3]
    y1 =[x ,0]
    y2= copy . deepcopy (y1)
    y2 [0][0]=0
    y2 [1]=1
    print y1 [0][0] # (a)
    print y1 [1] # (b)
    print y2 [0][0] # (c)
    print y2 [1] # (d)
#     
#     
# (f) What is the value of l after steps (a), (b), (c) and (d) below?
    l=[1 ,2 ,3]
    l [2:3]=4 # (a)
    print l
    l [1:3]=[0] # (b)
    print l
    l [1:1]=1 #(c)
    print l
    l [2:]=[] # (d)
    print l