##🔹 1. Ən kiçik ədədi tapmaq və tək ədədlərin sayını hesablamaq

n = int(input("Neçə ədəd daxil edəcəksiniz: "))
ededler = []

tek_sayi = 0 

for i in range(n):
    eded = int(input(f"{i+1}. ədədi daxil edin: "))
    ededler.append(eded)
    if eded % 2 == 1: 
        tek_sayi += 1

print("Ən kiçik ədəd:", min(ededler))
print("Tək ədədlərin sayı:", tek_sayi)

##🔹 2. Parolun güclülüyünü yoxlamaq

parol = input("Parolu daxil edin: ")

uzunluq = False
rqe = False
boyuk = False

if len(parol) >= 8:
    uzunluq = True

for simvol in parol:
    if simvol.isdigit():
        rqe = True
    if simvol.isupper():
        boyuk = True

if uzunluq and rqe and boyuk:
    print("Parol güclüdür.")
else:
    print("Parol zəifdir.")

##🔹 3. Ədədlərin cəmini və ən böyük/ən kiçik ədədləri hesablamaq (korrektə ehtiyacı var)

eded=int(input("edler daxil edin: "))
edeler=[]
for i in range (eded):
   a= sum(max(edeler))
   b= sum(min(eded))
   print(a,b)
