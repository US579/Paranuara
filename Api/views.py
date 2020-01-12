from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import People, Company
from . import serializers
import json
from django.http import JsonResponse, HttpResponse


class EmployeesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.EmployeesSerializer


class SameFriendsView(views.APIView):
    def get(self, request, pk1, pk2, format=None):
        people = People.objects.filter(index__in=(pk1, pk2))
        if people.count() != 2:
            return Response({'No same friends'},status=404)
        p1 = list(map(lambda x: int(x), people[0].friends.split(',')))
        p2 = list(map(lambda x: int(x), people[1].friends.split(',')))
        inter = list(set(p1).intersection(set(p2)))
        common = People.objects.filter(index__in=inter)
        same_friends = common.filter(eyeColor='brown', has_died=False)
        inf = {
            'people1': people[0],
            'people2': people[1],
            'same_friends': same_friends
        }
        serializer = serializers.SameFriendsSerializer(inf)
        return JsonResponse(serializer.data)


class FriutVegetableView(views.APIView):
     def get(self, request, pk1, format=None):
        people = People.objects.filter(index__in=[pk1])
        if people.count() != 1:
            return Response({'No user exist'})
        fruits = people[0].fruits.split(',')
        vegatables = people[0].vegetables.split(',')
        inf = {
            'name': people[0],
            'fruits': fruits,
            'vegatables': vegatables
        }
        serializer = serializers.FriutVegetableSerializer(inf)
        return JsonResponse(serializer.data)
