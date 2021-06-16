# 21
# İstifadəçidən bir string alın məsələn "Süleymanlı" bunu while ilə 10 dəfə Ekrana yazdırın.
new_string = input("Ad daxil edin:")
a=0
while a <10:
    print(new_string)
    a=a+1




# 22
# [3, 2, 4, 1]  şəklində bir list verilib. Bu listin sıralanmış variantını print etdirin.
new_list = [3,2,4,1]
new_list.sort()
print(new_list)






# 23
# Bir ədəd daxil edin və rəqəmlərinin sayını print etdirin.
new_number=int(input("Ədəd daxil edin:"))
number_times = 1
while new_number >=10:
    new_number=new_number//10
    number_times=number_times+1

print("Rəqəmlərin sayı: {}".format(number_times))







#24
#3 ədəd daxil  edin ortancılı print etsin.
a=int(input("Birinci ədədi daxil edin: "))
b=int(input("İkinci ədədi daxil edin: "))
c=int(input("Üçüncü ədədi daxil edin: "))

if a>b and a<c:
    average_number=a
elif b>a and b<c:
    average_number=b
elif c>a and c<b:
    average_number=c

print("Ortancıl ədəd: {}".format(average_number))







# 25
# Bir list var içində şəhərlər, ona yeni şəhərlər əlavə edin.
cities_list=["Baku","Ganca","Zaqatala","Qazax","Qax","Shaki"]
cities_list.append("Shamaxi")

print(cities_list)



# 26
# Sonra hər hansi şəhərin indeksini tapın və həmin indeksin təkmi cütmü olduğunu ekrana verin.
cities_list=["Baku","Ganca","Zaqatala","Qazax","Qax","Shaki"]
element_index=cities_list.index("Zaqatala")
if element_index == 0:
    element="0 tək və ya cüt deyil"
else:
    if element_index%2 == 0:
        element = "Cüt ədəddir"
    else:
        element = "Tək ədəddir"
        
print("İndex {}-dir və {}".format(element_index,element))







# 27
# Vurma cədvəlini ekrana yazdıran Python kodu yazın.
print("""
        ----- Vurma Cədvəli -----""")

for i in range(1,10):
    print("""
          ----- {} ə vurma -----""".format(i))
    for j in range(1,10):
        total=i*j
        print("{} x {} = {}".format(i,j,total))
        
        
        





# 28        
# Yaşı daxil edilən vətəndaşın sürücülük vəsiqəsinə yaşı çatıb-çatmadığını ekrana yazdıran kod yazın.
old = int(input("Yaşınızı daxil edin:"))
if old<18:
    print("Yaşınız çatmır!")
else:
    print("Yaşınız çatır")
    
    
    
    
    
    
    
    
    
# 29
# Tərəfləri daxil edilmiş üçbucağın növü müəyyənləşdirilməlidir.
# Bərabərtərəflidirsə ekrana 1, 
# Bərabəryanlıdırsa ekrana 2, 
# Müxtəliftərəflidirsə ekrana 3 yazıslın. 
# Tək sətirdə boşluqla ayrılmış şəkildə 3 tərəf daxil edilir və nəticə ekrana yazdırılır.

ededler = input("Tərəfləri daxil edin: (Boşluqla ayırın)  ")
x=ededler.split()
if x[0]==x[1]==x[2]:
    print(1)
elif x[0]==x[1] or x[0]==x[2] or x[1]==x[2]:
    print(2)
else:
    print(3)    
    
    
    
    
    
    
    
# 30
# Tək sətirdə 3 ədəd daxil edilir və ən böyük və ən kiçiyin hesablanması üçün
# köməkçi funksyalardan istifadə etməklə min( max(x, y), max(y, z), x+y+z)-i müəyyənləşdirin.
# Nətcə vergüldən sonra 2 rəqəm dəqiqliklə ekrana yazdırılsın. 

ededler = input("Tərəfləri daxil edin: (Boşluqla ayırın)  ")
a=ededler.split()
x=float(a[0])
y=float(a[1])
z=float(a[2])
new_number=min(max(x, y),max(y,z),x+y+z)
print("{:.2f}".format(new_number))
                   






# 31
# Ayın nömrəsi daxil edilir və ilin fəsli ekrana yazdırılır.
a = int(input("Ayın nömrəsini daxil edin:  "))
if a<2 or a==12:
    print("Qış ayıdır")
elif 2<a<6:
    print("Yaz ayıdır")
elif 5<a<9:
    print("Yay ayıdır")
else:
    print("Payız ayıdır")
    
    




    

# 32    
# n ədədi daxil edilir və ən böyük rəqəmini ekrana yazdırın.
a = int(input("Ədəd daxil edin: "))
a_copy=a
list=[]
while a>=10:
    list.append(a%10)
    a=a//10
list.append(a)

c = list[0]

for i in list:
    if i>c:
        c=i
print("""
      Daxil etdiyiniz ədəd: {}
      Ən böyük rəqəm: {}""".format(a_copy,c))       








# 33
# Daxil edilən n ədədinin bütün müsbət bölənlərini print etdirin.
n = int(input("Ədəd daxil edin:  "))
for i in range(1,n+1):
    if n%i==0:
       print(i)
       
       
       







# 34
# Daxil edilən n ədədin mükəmməl olub olmadığını print edin.
# Ədənin özü xaric müsbət bölənlərinin cəmi özünə bərabərdirsə belə ədədə mükəmməl ədəd deyilir.
# Məsələn, 1,2 və 3    6-nin bölənləridir cəmləri də 6-ya bərabərdir. 
n = int(input("Ədəd daxil edin:  "))
m=0
for i in range(1,n):
    if n%i==0:
       m=m+i
       
if m==n:
    print("Mükəmməl ədəddir")
else:
    print("Mükəmməl ədəd deyil")
    
    
    
    
    
    
    
    

    
# 35
# Bir list yaradın və 1dən 100-ə qədər olan ədədlərdən tək olanları bu listə yazın və sonda listi print etdirin    
list= []
a=1
while a <100:
    a=a+2
    list.append(a)
    if a==99:
        break
    
print(list)    







# 36
# 1-dən 100-ə qədər olan ədədləri 100-dən 1-ə şəklində print etdirin.
for i in range(100,0,-1):
    print(i)
    
    
 
    
 
    
 
# 37   
# Əlinizdə ölkə adlarının olduğu ölkə listi var.
# Yeni bir list yaradın və ölkə listində olan ölkələri yaratdığınız yeni listə yazın. 
# Lakin ölkənin uzunluğu 5-dən böyükdürsə olduğu kimi yazın, əks halda, yerinə * yazın.
country=["Turkey","Azerbaijan","Cuba","America","Italy","France","Chad","England"]
new_country=[]
for i in country:
    if len(i)<5:
        new_country.append("*")
    else:
        new_country.append(i)
print(new_country)










# 38
# arr = [1.4,3.7,4.8,6.3,99.9] verilmiş bu list-dən 4.8-i necə silə bilərik?
arr = [1.4,3.7,4.8,6.3,99.9]
arr.remove(4.8)
print(arr)










# 39
#s=’budama’ sözündə “a” hərflərinin sayını print etdirin. Bunu həm hazır metod ilə həm də alqoritm yazaraq edin.
s="budama"
f=0
for i in s:
    if i=="a":
        f=f+1
print(f)


n = s.count("a")
print(n)








# 40
# 0-dan 100-ə qədər cüt ədədləri toplayın amma bunu while ilə edin.
i=0
total=0
while i<100:
    i=i+2
    total=total+i
    if i==98:
        break

print(total)







# 41
# Daxilən edilən viza (30%), fərdi fəaliyyət(20%) və final(50%) balına görə tələbənin dərsi keçib-keçmədiyini print etdirin

a=int(input("1. Qimət daxil edin: "))*0.3
b=int(input("2. Qimət daxil edin: "))*0.2
c=int(input("3. Qimət daxil edin: "))*0.5

if (a+b+c)>50:
    print("Imtahandan keçdiniz  {}".format(a+b+c))
else:
    print("Kəsildiniz")
    
    
    
    
    




# 42
# Əmək haqqı və artım faizi daxil edilən işçinin yeni əmək haqqını hesablayın.
input1 =float(input("Əmək haqqını daxil edin: "))
input2 =float(input("Faiz daxil edin: "))

new_number =input1 + input1*input2/100

print("""
      Köhnə əmək haqqı: {}
      Faiz: {}
      Yeni əmək haqqı: {}
      """.format(input1,input2,new_number))        












# 43
# Hər hansı bir simvolun müəyyən bir stringin içində olub-olmadığını yoxlayın.
input1=input("String daxil edin: ")
input2=input("Axtardığınız simvol: ")

if input1.find(input2) !=0:
    print("Stringin daxilinde var")
    
else:
    print("Stringin daxilinde yoxdur")





#44
# N natural ədədi verilmişdir. Həmin ədəddə tək rəqəmlərin sayını tapın. (0 tək ədəd sayılmır)
n=input("Ədəd daxil edin:  ")
new_list=[]
for i in range(0,len(n)):
    if n[i].isnumeric()==True: 
        number = int(n[i])
        new_list.append(number)
tek_eded_say=0
tek_eded_list=[]         
for j in range(0,len(new_list)):
    if new_list[j]%2!=0:
        tek_eded_say=tek_eded_say+1
        tek_eded_list.append(new_list[j])       
print(f"""
       Daxil etdiyiniz ədəd: {n}
       Ədəddəki tək rəqəmlər: {tek_eded_list}
       Tək ədədlərin sayı: {tek_eded_say}
       """)
       
       
       
      
        
#45
# İlk 100 ədədin kvadratları cəmi ilə cəmlərinin kvadratı fərqini print etdirin.
sum_list=[]
pow_sum=[]
for i in range(0,101):
    sum_list.append(pow(i,2))
    pow_sum.append(i)
    
total = sum(sum_list)-pow(sum(pow_sum),2)
print(total)



#46
#Bir list formasında çalışanların əmək haqqları verilir. 
#Əmək haqqı 3000-dən çox olan işçilərin əmək haqqını 10%, 3000-dən az olan işçilərin əmək haqqını 20 faiz artıran python proqramı yazın.

list=[2000,4000,1500,6000]
def hesabla(e):
    for i in range(0,len(e)):
        if i >3000:
            e[i]=e[i]+e[i]*0.1
        else:
            e[i]=e[i]+e[i]*0.2
    
    print(e)
hesabla(list)



#47
# İstifadəçi bir ədəd daxil etsin bu bu ədəddən 1-ə qədər olan ədədlərin cəmini tapan rekursiv funksiya yazın.
input1=int(input("Reqem daxil edin: "))
def total(e):
    cem=0
    for i in range(1,e):
        cem=cem+i
    print("Reqemlerin cemi: {}".format(cem))
total(input1)
