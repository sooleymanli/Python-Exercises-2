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
