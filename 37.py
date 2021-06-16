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

