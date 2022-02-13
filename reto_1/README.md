Yacurl se creó con la finalidad de estudir la comunicacion de dos procesos / aplicaciones en Internet para implementar un servicio distribuido como mecanismo para entender y dominar los estándares de la Web (HTTP, HTML y URLs). 

Utilizaremos Sockets como mecanismo de comunicacion para el cliente Yacurl y un Web Service cualquiera.

Pasos para utilizar el cliente Yacurl:
    1. Inicializar una pipenv shell 

    2. Puede ejecutar Yacurl de 3 formas en una terminal:
        A. "$ python main.py yacurl" 
        B. "$ python main.py yacurl -h host"
        C. "$ python main.py yacurl -h host -p port"

    3. Opción A: El cliente Yacurl iniciara y solicitará un Host cualquiera a quien se realizara una petición, utilizar siempre el formato "www.eldominiodeseado.com" y presionar Enter para confirmar Host.
    Seguidamente Yacurl solicitara el puerto por el cual debera crear la conexion, escribir el puerto por el que desee conectarse (80 o 443), si no se especifica un puerto Yacurl tomará por defecto el puerto 80. Presionar Enter para confirmar.

    4. Opcion B: despues de -h debera especificar el host al que desea conectarse y presionar enter. 
    Seguido Yacurl pregutara el puerto deseado, si no se especifica tomará por defecto el puerto 80.

    5. Opción C: despues de -h debera especificar el host al que desea conectarse y despues de -p debera especificar el puerto igualmente y presionar enter para empezar la ejecución de Yacurl.

    

Funcionamiento del cliente Yacurl:

    1. Yacurl iniciara la conexion con el host y puerto especificados anteriormente y realizara una solicitud GET / HTTP/1.1 y solicitara los archivos html de dicho host.

    2. Cuando Yacurl reciba la respuesta del host (http response), entonces parseara la respuesta guardando el html en el archivo generado "parsing.html".
    
    3. Por ultimo en consola se observara el trafico generado con el protocolo TCP en el puerto especificado y se mostrarán todos los protocoolos decodificados de el paquete http.request y http.response.
    
    4. Yacurl cerrará la conexion con el host y el cliente finalizara su ejecucion.