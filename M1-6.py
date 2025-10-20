#Mesele 1
a=int(input("a ededini daxil edin: "))
b=int(input("b ededini daxil edin: "))
c=int(input("c ededini daxil edin: "))
if ((a>0 or b>0 or c>0 )and (a<0 or b<0 or c<0)):
    print("YES")
else:
    print("NO")


#Mesele 2
N=int(input("N ededini daxil edin: "))
a=N//100
b=(N//10)%10
c=N%10
if a!=b and a!=c and c != b:
    print("YES")
else:
    print("NO")


#Mesele 3
a=int(input("a ededini daxil edin: "))
b=int(input("b ededini daxil edin: "))
c=abs(a-b)-1
print("Aralarindaki edlerin sayi: " , c )


#Mesele 4
a=int(input("a ededini daxil edin: "))
b=int(input("b ededini daxil edin: "))
c=int(input("c ededini daxil edin: "))
d=int(input("d ededini daxil edin: "))
if (a > b) and (a > c) and (a > d):
    print("a ededi en boyukdur ")
elif (b > a) and (b > c) and (b > d):
    print("b ededi en boyukdur")
elif (c > a) and (c > b) and (c > d):
    print("c ededi en boyukdur")
else:
    print("d ededi en boyukdur")


#Mesele 5
a=float(input("a terefini daxil edin: "))
b=float(input("b terefini  daxil edin: "))
c=float(input("c terefini daxil edin: "))
v=a * b * c
s=2 * (a*b + b*c + a*c)
print("Düzbucaqlı paralelepipedin hecmi: ",v)
print("Düzbucaqlı paralelepipedin sahese: ",s)
a=int(input("ededi daxil edin: "))
if (a%2==0):
    print("eded cutur")
else:
    print("eded tekdir")
    
