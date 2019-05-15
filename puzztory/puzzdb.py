# -*- coding: utf-8 -*-

from django.http import HttpResponse

# from PuzzModel.models import Usertable


def testdb(request):
    response = ""
#     list = User.objects.all()

#     for var in list:
#         response += var.username + " "
#    #  if password_correct:
    return HttpResponse(response)
