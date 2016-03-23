from set_feedback.models import Set_feedback
from set_feedback.serializers import Set_feedbackSerializer
from rest_framework import generics
from django.http import JsonResponse
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions


class Set_feedbackList(generics.ListCreateAPIView):
 queryset = Set_feedback.objects.all()
 serializer_class = Set_feedbackSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)



def get_queryset(request):

  good=len(Set_feedback.objects.filter(value=1))
  bad=len(Set_feedback.objects.filter(value=0))

  
  results=[]
  results.append({
  		'good':good,
  		'bad':bad,
  	})
  
  return JsonResponse((list(results)),safe=False)









