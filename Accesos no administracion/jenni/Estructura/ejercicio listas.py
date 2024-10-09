abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","y","Z"]
for i in range(len(abecedario),1,-1):
     if i % 3 == 0:
        abecedario.pop(i-1)
print(abecedario)
