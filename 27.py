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
        