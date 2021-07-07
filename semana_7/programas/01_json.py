# -*- coding: utf-8 -*-
"""
json
"""

#%%
"""
Archivo JSON
"""

{
  "nombre":"Jonh Doe",
  "profesion":"Programador",
  "edad":25,
  "lenguajes":["PHP","Javascript","Python"],
  "disponibilidadParaViajar":"true",
  "rangoProfesional": {
      "aniosDeExperiencia": 7,
      "nivel": "Senior"
  }
}


#%%
"""
Dependencias de una aplicación
"""

"""
Especificar las dependencias de Node.js con un archivo package.json

Incluya un archivo package.json en la raíz del proyecto de código
fuente para especificar los paquetes de dependencias 
(use la palabra clave dependencies) y para proporcionar un comando de inicio 
(use la palabra clave scripts). El uso de la palabra clave scripts puede 
sustituir la opción NodeCommand de legado en el espacio de nombres 
aws:elasticbeanstalk:container:nodejs. 

"""

# ejemplo 1

{
    "name": "my-app",
    "version": "0.0.1",
    "private": true,
    "dependencies": {
      "ejs": "latest",
      "aws-sdk": "latest",
      "express": "latest",
      "body-parser": "latest"
    },
    "scripts": {
      "start": "node app.js"
    }
  }

#%%
# ejemplo 2
#package.json
{
  "name": "spa",
  "version": "0.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "test": "ng test",
    "lint": "ng lint",
    "e2e": "ng e2e"
  },
  "private": true,
  "dependencies": {
    "@angular/animations": "^6.0.0",
    "@angular/common": "^6.0.0",
    "@angular/compiler": "^6.0.0",
    "@angular/core": "^6.0.0",
    "@angular/forms": "^6.0.0",
    "@angular/http": "^6.0.0",
    "@angular/platform-browser": "^6.0.0",
    "@angular/platform-browser-dynamic": "^6.0.0",
    "@angular/router": "^6.0.0",
    "bootstrap": "^4.1.1",
    "core-js": "^2.5.4",
    "jquery": "^3.3.1",
    "popper.js": "^1.14.3",
    "rxjs": "^6.0.0",
    "zone.js": "^0.8.26"
  },
  "devDependencies": {
    "@angular/compiler-cli": "^6.0.0",
    "@angular-devkit/build-angular": "~0.6.1",
    "typescript": "~2.7.2",
    "@angular/cli": "~6.0.1",
    "@angular/language-service": "^6.0.0",
    "@types/jasmine": "~2.8.6",
    "@types/jasminewd2": "~2.0.3",
    "@types/node": "~8.9.4",
    "codelyzer": "~4.2.1",
    "jasmine-core": "~2.99.1",
    "jasmine-spec-reporter": "~4.2.1",
    "karma": "~1.7.1",
    "karma-chrome-launcher": "~2.2.0",
    "karma-coverage-istanbul-reporter": "~1.4.2",
    "karma-jasmine": "~1.1.1",
    "karma-jasmine-html-reporter": "^0.2.2",
    "protractor": "~5.3.0",
    "ts-node": "~5.0.1",
    "tslint": "~5.9.1"
  }
}


#%%


#crear.json
{
    "key":"value",
    "key2":"value"
}

#%%

# 1
{
  "array": [
    1,
    2,
    3
  ],
  "boolean": true,
  "color": "gold",
  "null": null,
  "number": 123,
  "object": {
    "a": "b",
    "c": "d"
  },
  "string": "Hello World"
}

#arhivo.json
{
  "nombre":"Jonh Doe",
  "profesion":"Programador",
  "edad":25,
  "lenguajes":["PHP","Javascript","Python"],
  "disponibilidadParaViajar":true,
  "rangoProfesional": {
      "aniosDeExperiencia": 7,
      "nivel": "Senior"
  }
}




#%%
"""
Serialilzar
"""

import json

x = {
  "nombre": "Carlos",
  "edad": 30,
  "casado": True,
  "divorciado": False,
  "hijos": ("Ann","Billy"),
  "mascotas": None,
  "carros": [
    {"modelo": "BMW 230", "mpg": 27.5},
    {"modelo": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#%%
#ejemplo 2

al_gabriel = { "1":"Gabriel","asignatura":"Técnicas","laVaPerdiendo":True, 
              "notasActuales": [1.0, 3.5]}
json_hilera = json.dumps(al_gabriel) 

#%%
"""
Equivalente JSON
"""
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#%%
"""
Deserializar
"""
x =  '{ "nombre":"John", "edad":30, "ciudad":"New York", "boleano":true}'
import json
objeto = json.loads(x)

print(objeto)
print(objeto["edad"])

#%%

"""
crear archivo JSON
"""

# importa la libreria
import json

# Crea un diccionario, las llaves son los nombres de las variables
a = {"nombre":"Gabriel", "asignatura":"Técnicas",
     "vaPerdiendo":True,"notas": [1, 3.5]}

# abre un archivo y va guardando el diccionario como json
with open('alumnoGabriel.json', 'w') as f:
    # se utiliza el método dump para almacenar el diccionario
    # dentro del archivo
    json.dump(a, f)
    
#%%
"""
Lectura de un archivo con formato serializado
"""
f = open("ejemplo.json","r")
data = json.loads(f.read())

print(data)