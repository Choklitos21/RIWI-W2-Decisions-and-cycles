1. Diferencias entre un **bucle controlado por contador** y un **bucle controlado por condición**.
~~~
La principal diferencia entre un bucle controlado por contador y un bucle controlado por 
condición reside en el mecanismo de terminación: un bucle por contador, típicamente un bucle for, 
está diseñado para repetirse un número fijo y predeterminado de veces, utilizando una variable numérica 
que se incrementa o decrementa hasta alcanzar un valor límite; en cambio, un bucle por condición, 
como un bucle while, se repite un número indeterminado de veces, y su ejecución continúa mientras 
una condición lógica sea verdadera, deteniéndose solo cuando esa condición cambia a falsa debido a algún 
cambio interno o externo (como una entrada del usuario o un cambio en los datos).
~~~
2. Ejemplos cotidianos que representen el uso de cada tipo de bucle.
~~~
Bucle controlado por contador: Un ejemplo puede ser la venta de boletos de un concierto, mientras haya X cantidad
de boletos disponibles, que las ventas estes disponibles, y una vez ese valor sea 0, que ya no se puedan comprar
mas boletos
Bucle controlado por condicion: Un ejemplo seria un semaforo, mientras el color del semaforo sea VERDE (True) los 
carros pueden transitar y cuando se vuelva ROJO (False) no se permite el paso
~~~
3. Cuándo es más apropiado usar `while` en lugar de `for`.
~~~
Es más apropiado usar el bucle 'while' en lugar del bucle 'for' cuando el número de repeticiones es desconocido o 
indeterminado y la finalización del ciclo depende de que una condición se vuelva falsa
~~~
4. Qué es un **bucle infinito**, cómo prevenirlo y cómo detectarlo durante la ejecución.
~~~
* Un bucle infinito es una secuencia de instrucciones dentro de un programa que se repite sin cesar porque su 
condición de terminación nunca se cumple.
* Dentro del bucle, siempre debe haber una instrucción que modifique la variable o estado utilizado en la 
condición de parada, revisa cuidadosamente si la condición de prueba realmente puede volverse falsa, tambien
es una buena práctica incluir un contador secundario que fuerce la salida después de un número máximo 
de iteraciones razonable
* Verificar la Falta de Salida (Output), usar un Depurador (Debugger), observar el Uso de la CPU para ver que 
nada este gastando muchos recursos
~~~
5. Qué función cumplen las sentencias `break` y `continue` dentro de un ciclo.
~~~
Break cumple la función de terminar inmediatamente el bucle en el que se encuentra, sin importar si 
la condición de ciclo se ha cumplido, siendo útil para detener un ciclo cuando se alcanza un resultado deseado 
o se encuentra un error, mientras que continue cumple la función de saltar la ejecución del código 
restante y avanzar directamente a la siguiente repetición del bucle
~~~
6. Explica el error lógico más común al usar `while` y cómo evitarlo.
~~~
El error lógico más común al usar while es crear por error un bucle infinito, lo que ocurre porque la variable o 
de control de la condición del ciclo nunca se modifica (o se modifica incorrectamente) dentro del del bucle, 
impidiendo que la condición se vuelva falsa.
Para evitar este problema, hay que asegurarse de que en cada iteración exista una instrucción exacta 
que acerque la variable de control al límite de la condición (por ejemplo, incrementando un contador o cambiando un 
estado a False), haciendo asi que el bucle pueda finalizar
~~~

