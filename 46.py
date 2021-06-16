
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