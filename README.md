# t_credito

## 1. Cloning the repository
```
git clone https://github.com/fabianMM04/t_credito.git
```
## 2. go to the project and build with docker-compose
```
cd t_credito
docker-compose build
```
## 3. testing the api
```
docker-compose run api python manage.py test franquicia
```
## 4. Run project with docker-compose
```
docker-compose up
```
## 4. API franquicia
```
* GET: http://127.0.0.1:8000/api/v1/franquicia
response: {
    "franquicias": [
        {
            "id": 2,
            "nombre": "VISA",
            "cantidad_numero": 16,
            "numero_inicial": 4
        },
        {
            "id": 3,
            "nombre": "Mastercard",
            "cantidad_numero": 16,
            "numero_inicial": 5
        },
        {
            "id": 4,
            "nombre": "Amex",
            "cantidad_numero": 15,
            "numero_inicial": 3
        },
        {
            "id": 5,
            "nombre": "Diners Club",
            "cantidad_numero": 14,
            "numero_inicial": 3
        },
        {
            "id": 7,
            "nombre": "prueba",
            "cantidad_numero": 17,
            "numero_inicial": 1
        }
    ]
}
* POST: http://127.0.0.1:8000/api/v1/franquicia 
  Header: Content-Type: application/json
  Body: {

          "nombre": "prueba",
          "cantidad_numero": 17,
          "numero_inicial": 1
}
Response: {
    "message": "Agregado exitosamente"
}
* GET: http://127.0.0.1:8000/api/v1/franquicia/{id} ; http://127.0.0.1:8000/api/v1/franquicia/2
  Response: {
    "franquicia": {
        "id": 2,
        "nombre": "VISA",
        "cantidad_numero": 16,
        "numero_inicial": 4
    }
}
* PUT: http://127.0.0.1:8000/api/v1/franquicia/{id} ; http://127.0.0.1:8000/api/v1/franquicia/7
  Header: Content-Type: application/json
  Body: {
    "nombre": "prueba update",
    "cantidad_numero": 13,
    "numero_inicial": 9
  }
  Response:  {
    "message": "Actualizado exitosamente"
}
* DELETE: http://127.0.0.1:8000/api/v1/franquicia/{id} ; http://127.0.0.1:8000/api/v1/franquicia/8
  Response: {"message": "Eliminado exitosamente"}
```
## 5. API verificar
```
* 
* POST: http://127.0.0.1:8000/api/v1/verificar
  Header: Content-Type: application/json
  Body: {
    "numero": "331 231 312 312 123"
   }
   Response: {
    "nombre": "Amex"
    }
