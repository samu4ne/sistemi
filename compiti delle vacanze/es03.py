#es03: generare serie di fibonacci ricorsiva

def serie_fibonacci(n, k, a, b):
    if(k<n):
        k= k+1
        c=a+b
        a=b
        b=c
        print(c)
        serie_fibonacci(n, k, a, b)





print("inserire il numero di elementi della serie di fibonacci")
n=input()
a=1
b=1
print(a)
print(b)
serie_fibonacci(n, 2, a, b)