def max(i, e):
    if i>e:
        return i
    else:
        return e
def min(i, e):
    if i<s:
        return i
    else:
        return e
print("Vvedite 4 chisla")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
max1=max(max(a,b),max(c,d))
max2=min(min(a,b),min(c,d))
print("max = ",max1)
print("min = ",max2)
summ=max1+max2
print("summa = ",summ)