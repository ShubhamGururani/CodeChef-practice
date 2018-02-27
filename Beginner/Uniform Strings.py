t=int(input());
for i in range(0,t):
    count=0
    x=input();
    z=0;
    while z<len(x):
        if z==len(x)-1:
            if x[z]!=x[0]:
                count=count+1
            break
                   
        if x[z]!=x[z+1]:
            count=count+1
        z=z+1
    if count <3:
        print('uniform')
    else:
        print('non-uniform')