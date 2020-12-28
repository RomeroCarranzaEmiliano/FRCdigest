# Bienvenido a la documentación de FRCdigest

[visita nuestro repositorio en github](https://github.com/RomeroCarranzaEmiliano/FRCdigest).

## /api

En este módulo se encuentran todos los archivos que hacen a la api de la aplicación. El propósito de esta es provisorio.
No se deben crear _issues_ referidos a este módulo, ya que se prevee para la versión 1.0 la creación de una api en un
repositorio separado.

## /bot

En este modulo se encuentran todos los archivos que hacen al bot de discord para la aplicación.

    /bot
        /command
        .env
        __init__.py
        __main__.py
        config.db
        config.py
        config.yml
        setup_config_database.py

### /bot/command/

Este módulo contiene todos los archivos necesarios para ser utilizado en el procesamiento de comandos.

    /command
        __main__.py
        command_dictionary.py
        commander.py

#### /bot/command/\_\_main__.py



#### /bot/command/command_dictionary.py

Contiene una función por cada comando soportado, esta función se encarga de realizar las acciones asociadas al 
comando(lo que se supone que debe realizar). También contiene un diccionario con el _tag_ de cada comando y la
respectiva función de este.

#### /bot/command/commander.py

Contiene un objeto _Commander_ el cual debe recibir un comando como parametro para ser inicializado.

    class Commander():
    def __init__(self, command):
        self.command = command
        self.parameters = []
        self.to_do = ''
        self.command_dictionary = command_dictionary.dictionary
        self.response = ''
    
    import commander as cmdr
    commander = cmdr.Commander(command)

Este objeto es responsable de:

* detectar cuál comando se está llamando
* obtener los parámetros junto a este
* verificar los parámetros
* formatear los parámetros como un vector
* ejecutar el comando. 


#
    commander.detect()
    

Este método se encarga de detectar cuál comando ha sido llamado. Verifica que el comando recibido, ya guardado en 
self.command, no esté vacío. Luego, mediante el vector de _supported_commands_ y el vector _tag_, paralelos entre sí,
trata de encontrar una ocurrencia en _supported_commands_ que verifique el comando. Finalmente se guarda en self.to_do el
respectivo valor del vector _tag_

### /bot/.env

### /bot/\__main__.py

### /bot/config.db

### /bot/config.py

### /bot/config.yml

### /bot/setup_config_database.py


## /database/

En este directorio se encuentra la base de datos _sqlite_, archivos .csv y scripts de python para manejar la base de
datos y los archivos .csv
