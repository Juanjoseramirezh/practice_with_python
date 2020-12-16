#1 imprimir el string "Hola mundo" 
print("Hola mundo")

#2 imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hola",name,"!") #con una coma
print("Hola " + name +"!") #con un mas, nota hay que dejar un espacio

#3 imprimir "Hola numero 42" con un numero en una variable
num = 42
print("Hola", num) #con una coma
print("Hola " + str(num)) #con un mas, para contatenar un str(NUMERO)

#4 imprimir "me encanta comer sushi y pizza" con los alimentos en variables
fav_food1 = "sushi"
fav_food2 = "pizza"
print("Me encanta comer {} y {}".format(fav_food1,fav_food2))#con un .format()
print(f"Me encanta comer {fav_food1} y {fav_food2}")