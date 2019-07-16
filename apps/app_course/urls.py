from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'add', views.add),
    url(r'^destroy/(?P<course_id>[0-9]+)', views.delete),
    url(r'^delete/(?P<course_id>[0-9]+)', views.destroy),
]