from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from set_feedback import views
from set_feedback.views import get_queryset

urlpatterns = [
    url(r'^set_feedback/$', views.Set_feedbackList.as_view()),
    url(r'^get_feedback/$', get_queryset),
    # url(r'^register/(?P<pk>[0-9]+)/$', views.RegisterDetail.as_view()),
    
	
]

urlpatterns = format_suffix_patterns(urlpatterns)

