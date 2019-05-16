    
def fact(n):
    if n==1:
        return n
    else:
        return (n)*fact(n-1)

def sum(n):
    if n==1:
        return n
    else:
        return n+sum(n-1)
