from os import stat
from django.db import reset_queries
from django.db.models import query
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


from django.http.response import JsonResponse

from .models import Franquicia
from .serializers import FranquiciaSerializer


@api_view(["POST"])
def verificar_tc(request):
    """
    Función que retorna el nombre de la franquicia.
    request: 
    - numero: contiene el numero de la tarjeta de credito.

    POST: Recibe el numero de la tarjeta de credito y 
    retorna el nombre de la franquicia o invalido si esta mal ingresado
    """
    try:      
        json_object = JSONParser().parse(request)
        numero_tarjeta = str(json_object['numero'])
        numero_tarjeta = numero_tarjeta.replace(" ", "")
        if numero_tarjeta.isnumeric():
            cantidad_numero = len(numero_tarjeta)
            numero_inicial = numero_tarjeta[0]
            try:
                franquicia = Franquicia.objects.get(cantidad_numero=cantidad_numero, numero_inicial=numero_inicial)
                return JsonResponse({"nombre": franquicia.nombre}, status=status.HTTP_200_OK)
            except:
                return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({"message": "Numero de la tarjeta invalido"}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse({"message": "No se encontro campo numero"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def franquicia_list_create(request):
    """
    Función que retorna la lista de franquicias y para crear franquicia.

    GET: retorna lista de franquicias
    POST: Crea una franquicia y retorna mensaje exitoso o fallido
    """
    if request.method == 'GET':
        try:        
            franquicias = Franquicia.objects.all()
            franquicias_serializer = FranquiciaSerializer(franquicias,many=True)
            return JsonResponse({"franquicias": franquicias_serializer.data}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            franquicia_data = JSONParser().parse(request)
            franquicias_serializer = FranquiciaSerializer(data=franquicia_data)
            if franquicias_serializer.is_valid():
                franquicias_serializer.save()
                return JsonResponse({"message": "Agregado exitosamente"}, status=status.HTTP_201_CREATED)
            return JsonResponse({"message":"Fallo en agregar franquicia"}, status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["GET", "PUT", "DELETE"])
def franquicia_detail(request, pk=0):
    """
    Función que actualiza, elimina y ve el detalle de una franquicia
    parametros: pk

    GET: Muestra el detalle de una franquicia por el id
    PUT: Actualiza los datos de una franquicia por el id
    DELETE: Elimina una franquicia por el id
    """
    try:
        franquicia = Franquicia.objects.get(pk=pk)
    except Franquicia.DoesNotExist:
        return JsonResponse({"message": "franquicia no existe"}, status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == "GET":
        try:
            franquicias_serializer = FranquiciaSerializer(franquicia)
            return JsonResponse({"franquicia": franquicias_serializer.data}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            franquicia_data = JSONParser().parse(request)

            franquicias_serializer = FranquiciaSerializer(franquicia,data=franquicia_data, partial=True)
            if franquicias_serializer.is_valid():
                franquicias_serializer.save()
                return JsonResponse({"message":"Actualizado exitosamente"}, status=status.HTTP_200_OK)
            return JsonResponse({"message": "Fallo en actualizar"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            franquicia.delete()
            return JsonResponse({"message": "Eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return JsonResponse({"message": "Fallo comuniquese con el administrador del sistema"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
