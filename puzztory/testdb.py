# -*- coding: utf-8 -*-
from django.http import HttpResponse
from PuzzModel.models import Fragmenttable

def testdb(request):
    # response = ""
    list = Fragmenttable.objects.all()
    response_list = [var.fragmentid for var in list]
    response = " ".join(str(id) for id in response_list)
    # for var in list:
    #    response += (str(var.fragmentid) + " ")
    return HttpResponse("<p>" + response + "</p>")
