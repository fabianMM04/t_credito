from os import stat
from django.db.models import query
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


from django.http.response import JsonResponse

from .models import Franquicia
from .serializers import FranquiciaSerializer

@csrf_exempt
def verificar_tc(request):
    if request.method == 'POST':

        json_object = JSONParser().parse(request)
        numero_tarjeta = str(json_object['numero'])
        numero_tarjeta = numero_tarjeta.replace(" ", "")
        if numero_tarjeta.isnumeric():
            cantidad_numero = len(numero_tarjeta)
            numero_inicial = numero_tarjeta[0]
            franquicia = Franquicia.objects.get(cantidad_numero=cantidad_numero, numero_inicial=numero_inicial)
            return JsonResponse({"nombre": franquicia.nombre}, status=status.HTTP_200_OK)
        return JsonResponse({"message": "Numero de la tarjeta invalido"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def franquiciaAPI(request,pk=0):
    if request.method == 'GET':
        franquicias = Franquicia.objects.all()
        franquicias_serializer = FranquiciaSerializer(franquicias,many=True)
        return JsonResponse({"franquicia": franquicias_serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        franquicia_data = JSONParser().parse(request)
        franquicias_serializer = FranquiciaSerializer(data=franquicia_data)
        if franquicias_serializer.is_valid():
            franquicias_serializer.save()
            return JsonResponse({"message": "Agregado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"message":"Fallo en agregar franquicia"}, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        franquicia_data = JSONParser().parse(request)
        franquicia = Franquicia.objects.get(pk=pk)

        franquicias_serializer = FranquiciaSerializer(franquicia,data=franquicia_data, partial=True)
        if franquicias_serializer.is_valid():
            franquicias_serializer.save()
            return JsonResponse({"message":"Actualizado exitosamente"}, status=status.HTTP_200_OK)
        return JsonResponse({"message": "Fallo en actualizar"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        franquicia = Franquicia.objects.get(pk=pk)
        franquicia.delete()
        return JsonResponse({"message": "Eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def franquicia_list_create(request):
    if request.method == 'GET':
        franquicias = Franquicia.objects.all()
        franquicias_serializer = FranquiciaSerializer(franquicias,many=True)
        return JsonResponse({"franquicias": franquicias_serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        franquicia_data = JSONParser().parse(request)
        franquicias_serializer = FranquiciaSerializer(data=franquicia_data)
        if franquicias_serializer.is_valid():
            franquicias_serializer.save()
            return JsonResponse({"message": "Agregado exitosamente"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"message":"Fallo en agregar franquicia"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def franquicia_detail(request, pk=0):
    if request.method == "GET":
        franquicia = Franquicia.objects.get(pk=pk)
        franquicias_serializer = FranquiciaSerializer(franquicia)
        return JsonResponse({"franquicia": franquicias_serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        franquicia_data = JSONParser().parse(request)
        franquicia = Franquicia.objects.get(pk=pk)

        franquicias_serializer = FranquiciaSerializer(franquicia,data=franquicia_data, partial=True)
        if franquicias_serializer.is_valid():
            franquicias_serializer.save()
            return JsonResponse({"message":"Actualizado exitosamente"}, status=status.HTTP_200_OK)
        return JsonResponse({"message": "Fallo en actualizar"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        franquicia = Franquicia.objects.get(pk=pk)
        franquicia.delete()
        return JsonResponse({"message": "Eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)
