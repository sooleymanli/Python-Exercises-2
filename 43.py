# 43
# Hər hansı bir simvolun müəyyən bir stringin içində olub-olmadığını yoxlayın.
input1=input("String daxil edin: ")
input2=input("Axtardığınız simvol: ")

if input1.find(input2) !=0:
    print("Stringin daxilinde var")
    
else:
    print("Stringin daxilinde yoxdur")
