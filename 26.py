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
