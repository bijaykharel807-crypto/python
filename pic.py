def fibbo(n):
     if n==1 or n==0:
         return 1
     else:
              return n * fibbo(n-1) 
         
print (fibbo(5))