for i in range(int(input())):
    n=int(input())
    c=0
    d=0
    notes=0
    c=n%100
    d=n//100
    notes=notes+d
 
    d=c//50
    c=c%50
    notes=notes+d
    d=c//10
    c=c%10
   
    notes=notes+d
    d=c//5
    c=c%5
    
    notes=notes+d
    d=c//2
    c=c%2
    
    notes=notes+d
    d=c//1
    c=c%1
    
    notes=notes+d
    print(notes)