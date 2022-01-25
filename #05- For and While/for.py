



# Print número de 0 a 9
for x in range(0, 10):
    print ("você esta no numero",x)

print("\nARRAY:\n")
Array = [1,2,3,4,5,6,7,8]
for x in Array:
    print ("Imprimindo em array",x)

ArrayIntoArray = [[1,2,3],[4,5,6]]
for x in ArrayIntoArray:
    print ("Imprimindo em array",x)
    for y in x:
       print ("Imprimindo em array dentro de array",y) 

print("\nTuppla:\n")
Tupple = (1,2,3,4,5,6,7,8,9,10,22)
for x in Tupple:
    print("Imprimindo Tupla",x)

print("\nDicionario:\n")
Dictionary = {"item":"abc","item2":"def"}
for x in Dictionary:
    print("Imprimindo dicionario",x)


Dictionary = {"item":"abc","item2":"def"}
for x in Dictionary:
    print("Imprimindo valores do dicionario ",Dictionary[x])