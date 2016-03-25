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

  value1=len(Set_feedback.objects.filter(value=1))
  value2=len(Set_feedback.objects.filter(value=2))
  value3=len(Set_feedback.objects.filter(value=3))
  value4=len(Set_feedback.objects.filter(value=4))
  value5=len(Set_feedback.objects.filter(value=5))
  value6=len(Set_feedback.objects.filter(value=6))
  value7=len(Set_feedback.objects.filter(value=7))
  value8=len(Set_feedback.objects.filter(value=8))
  value9=len(Set_feedback.objects.filter(value=9))
  value10=len(Set_feedback.objects.filter(value=10))
  value11=len(Set_feedback.objects.filter(value=11))
  value12=len(Set_feedback.objects.filter(value=12))

  
  results=[]
  results.append({
  		'this is boring':value1,
  		'need to know more...':value2,
      'i feel sleepy':value3,
      'please slow down':value4,
      'this is interesting':value5,
      'im saturated':value6,
      'im lovin it':value7,
      'i need a chai break':value8,
      'lost the track':value9,
      'this is informative':value10,
      'best thing in the world':value11,
      'why am i here???':value12,
  	})
  
  return JsonResponse((list(results)),safe=False)









