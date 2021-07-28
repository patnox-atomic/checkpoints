##Patnox 27-07-2021

from rest_framework.exceptions import ValidationError, ParseError
from django.shortcuts import render
from checkpoints.models import CheckedPoints
from checkpoints.serializers import CheckedPointsSerializer
from rest_framework import viewsets
###from django.http import HttpResponse
from checkpoints.calculator import Calculate

###def index(request):
    ###return HttpResponse("Checkpoints App")

class CheckedPointsViewSet(viewsets.ModelViewSet):
    queryset = CheckedPoints.objects.all()
    serializer_class = CheckedPointsSerializer

    def perform_create(self, serializer):
        query = self.request.data.get('query')
        ##print("Got query as: " + query)
        ob = Calculate()
        answer = ob.str_get_closest(query)
        if answer != None:
             #print("Got answer as: " + str(answer))
             serializer.save(response=str(answer))
        else:
             #print("Got an error parsing points")
             raise ValidationError("Failed to check the points. Make sure you use the format [(1,2), (3,4)]")
             ##raise ParseError
