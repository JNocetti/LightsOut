# LightsOut
Lights Out es un juego electr´onico que se juega en un tablero n×n de luces que pueden estar prendidas
o apagadas. El juego comienza con una distribuci´on aleatoria de luces prendidas o apagadas en el tablero,
y el objetivo del jugador es alcanzar un estado en el que todas las luces est´an apagadas.
Presionar cualquiera de las luces tendr´a como efecto cambiarla de estado (si estaba prendida pasa a
apagada, y si estaba apagada pasa a estar prendida), la dificultad del juego est´a en que tambi´en cambian
de estado las luces adyacentes a la presionada.
Mostremos un ejemplo de una jugada. Modelaremos el tablero del juego como una matriz n × n con
entradas 1 (luz prendida) y 0 (luz apagada). Utilizaremos la notaci´on est´andar aij para la luz que se
encuentra en la fila i y la columna j. Supongamos que el juego se encuentra en el siguiente estado


0 0 1 1 1
0 1 1 1 0
1 0 0 1 1
1 1 0 0 1
0 1 1 1 0


Si presionamos la luz que se encuentra en la entrada a43 (que est´a apagada), la cambiaremos de estado
as´ı como a sus cuatro luces adyacentes, obteniendo el estado


0 0 1 1 1
0 1 1 1 0
1 0 1 1 1
1 0 1 1 1
0 1 0 1 0


Es posible probar el juego de forma online. Recomendamos probar algunas veces el juego en tableros
de distintos tama˜nos, para familiarizarse con las reglas.
Se pide:
1. ¿Es necesario que alguna de las luces sea presionada m´as de una vez para ganar el juego?
2. ¿El orden en que se presionan las luces en una soluci´on es relevante?
En base a las respuestas de las preguntas anteriores, propondremos como modelo matem´atico para
las soluciones del juego un vector v = (x1, x2, . . . , xn2 ) de tama˜no n
2
. Dado i ∈ {1, 2, . . . , n2} usamos
divisi´on entera para escribir i − 1 = n · q + r con 0 ≤ r < n. Luego definimos xi = 1 si la luz en la entrada
a(q+1)(r+1) debe ser presionada en la soluci´on y xi = 0 en caso contrario.
Se pide:
3. Justifique por qu´e el modelo matem´atico anterior es correcto para modelar las soluciones del juego.
Veamos un ejemplo en un tablero m´as chico. Tambi´en usaremos este ejemplo para proponer un sistema
lineal de ecuaciones que encuentre una soluci´on del juego. Supongamos que tenemos el tablero


0 1 0
1 1 0
0 0 1


Este estado del juego puede ganarse presionando las luces a33 y a22 (¿importa el orden en que las
presionamos?). Al presionar la luz a33 obtenemos el estado


0 1 0
1 1 1
0 1 0


donde al presionar la luz a22 obtenemos


0 0 0
0 0 0
0 0 0


que corresponde a la victoria del jugador. En t´erminos del modelo matem´atico propuesto, la soluci´on ser´a
el vector (0, 0, 0, 0, 1, 0, 0, 0, 1), donde x5 = x9 = 1 y xi = 0 para i ∈ {1, 2, 3, 4, 6, 7, 8}.
Vamos a plantear un sistema de ecuaciones que permita resolver el problema. La idea es que x1, x2, . . . , xn2
sean las inc´ognitas, y que cada ecuaci´on refleje la cantidad de cambios de estado que ocurren en la luz
correspondiente. Usaremos la misma regla de asociaci´on que antes, la ecuaci´on i del sistema trabajar´a
con la luz a(q−1)(r−1) donde i − 1 = n · q + r con 0 ≤ r < n. Lo haremos en el tablero 3 × 3 del ejemplo
anterior, por lo que n = 3 y como hay 32
luces, generaremos un sistema de 9 ecuaciones con 9 inc´ognitas.
Trabajaremos con la suma 1 + 1 = 0, esto es porque una cantidad par de cambios de estado en una
luz equivalen a no hacer ning´un cambio de estado.
Para la primera ecuaci´on, tenemos que estudiar lo que pasa con la luz a11. Debido a las reglas del
juego, la misma s´olo se ve afectada por los cambios de estado de las luces en las entradas a11, a12 y
a21, que se corresponden con las inc´ognitas x1, x2 y x4 del sistema. Obtenemos entonces que la primera
ecuaci´on del sistema es
x1 + x2 + x4 = 0
el miembro izquierdo de la igualdad representa los cambios de estado que ocurren en la entrada a11, el
miembro de la derecha es cero porque dado el tablero inicial con el que estamos trabajando, no queremos
que haya cambio de estado en la luz a11. Si continuamos con esta l´ogica para todas las luces obtenemos
el sistema de ecuaciones



x1 + x2 + x4 = 0
x1 + x2 + x3 + x5 = 1
x2 + x3 + x6 = 0
x1 + x4 + x5 + x7 = 1
x2 + x4 + x5 + x6 + x8 = 1
x3 + x5 + x6 + x9 = 0
x4 + x7 + x8 = 0
x5 + x7 + x8 + x9 = 0
x6 + x8 + x9 = 1
Se pide:
4. Justifique detalladamente la construcci´on de las otras ecuaciones del sistema en este ejemplo.
5. Verifique que la soluci´on encontrada anteriormente donde x5 = x9 = 1 y xi = 0 para i ∈
{1, 2, 3, 4, 6, 7, 8} es soluci´on del sistema de ecuaciones.
Con esto hemos visto la estrategia para construir un sistema de ecuaciones cuya soluci´on resuelve el
juego Lights Out. Ahora pasamos a la implementaci´on en Python de una soluci´on al problema.
Se pide:
6. Crear una funci´on en Python que reciba como entrada una matriz n×n de unos y ceros, que represente el estado inicial del juego Lights Out, y devuelva un vector de unos y ceros correspondiente
a la soluci´on del juego, usando el modelo matem´atico propuesto en este document.
Para la resoluci´on del sistema de ecuaciones, se tendr´a que modificar el algoritmo de escalerizaci´on
Gaussiana para tener en cuenta que estamos trabajando en el conjunto {0, 1} con la suma binaria, y sin
producto. Observe que por como queda constru´ıdo el sistema nunca ser´a necesario hacer pivoteo, por lo
que la ´unica transformaci´on elemental que se debe aplicar es Fi → Fi + Fj .
Sobre el informe:
• El tiempo para entregar el informe es hasta el s´abado 11 de noviembre inclusive. La entrega se
realizar´a por webasignatura.
• El informe deber´a estar en formato pdf, la entrega tambi´en deber´a incluir los scripts utilizados.
• El informe deber´a contener t´ıtulo, fecha, nombre y c´edula del estudiante.
• Se evaluar´a: prolijidad del informe, utilizaci´on correcta del idioma espa˜nol, redacci´on, prolijidad del
c´odigo presentado en los scripts, conclusiones
