# Encriptador
Un programa con una GUI integrada y capaz de "encriptar" blocs de notas seleccionados, mediante una contraseña. También es capaz de realizar el proceso inverso.
El algoritmo de "encriptación" (que no se si debería llamarlo así) funciona de la siguiente manera. 

# El Algoritmo
1. Lee el documento y separa cada uno de sus caracteres.
2. Transforma cada caracter en su equivalente de UNICODE.
3. Con una contraseña, suma al valor anterior el valor de la contraseña.
4. Escribe un nuevo documento con los caracteres que quedaron.

Cuando desencripta el documento es básicamente lo mismo, solo que resta la contraseña en vez de sumarla.

# ¿Cómo funciona en realidad?
Básicamente un bucle lee cada uno de los valores y los asigna en un generador. 
Antiguamente utilizaba una lista pero este sistema consume demasiada RAM a medida que el documento crece. 

Luego, con ese generador creo un objeto que lo contiene, para que pueda cambiar los atributos del objeto y no generar muchas variables. Ahí tengo alojados los métodos, que consisten en generar un equivalente de UNICODE y uno de Caracteres. 
Luego de eso, en el __init__.py recopilo todas estas funciones y creo una función que encripta los archivos recibiendo el nombre y la contraseña (en cadena de texto) y otra con los mismo argumentos pero para la desencriptación.

Todo eso lo integro con una interaz gráfica creada con la librería tkinter y así tenemos el resultado final. 

# ¡Gracias por ver este repositorio!
Siéntete libre de compartirlo y de hacer tus propias versiones, estaré revisándolas.
