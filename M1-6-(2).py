# 1.	1-dən 10-a qədər olan ədədlərin kvadratlarını çap edən proqram

for i in range(1, 11):
    print(i**2)

# 2.	1-dən n-yə qədər olan cüt ədədləri çap et. n konsoldan daxil edilir.

n=int(input(("Ededi daxil edin: ")))
for i in range(1,n+1):
    if (i%2==0):
        print("Cut ededler: ",i)

# 3.	Mənfi ədəd daxil edilənə qədər ədədləri toplayan proqram yaz.

total = 0

while True:
    n = int(input("Eded daxil et: "))
    if n < 0:
        break
    total += n

print("Ededlerin cemi:", total)

# 4.	1-dən 10-a qədər ədədləri yaz, amma 4 və 7-ni keç.

for i in range(1,11):
    if (i!=4 and i!=7):
        print(i)

# 5.	İki ədədin cəmini, fərqini, hasilini, bölünməsini tapan funksiya yaz.

def hesabla(a, b):
    print("Cemi:", a + b)
    print("Ferqi:", a - b)
    print("Hesili:", a * b)
    print("Qismeti:", a / b)

a1 = int(input("1-ci ededi daxil edin: "))
a2 = int(input("2-ci ededi daxil edin: "))

hesabla(a1, a2)

# 6.	Verilən ədədin cüt olub-olmadığını yoxlayan funksiya yaz.
def cuty(a):
    if a % 2 == 0:
        print(a, "cutdur")
    else:
        print(a, "tekdir")

n = int(input("Eded daxil edin: "))
cuty(n)



