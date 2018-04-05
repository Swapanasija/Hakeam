from django.conf.urls import url
from myapp import views

app_name='myapp'

urlpatterns = [
    
    url(r'^donors/$',views.donorview,name='donorview'),
    url(r'^acceptors/$', views.acceptorview, name="acceptorview"),
    url(r'^doctors/$', views.doctorview, name="doctorview"),
    url(r'^help/$', views.helpview, name="helpview"),
    url(r'^help/radarview/$', views.radarview, name="radarview"),
    url(r'^doctors/result/$', views.resultview, name="resultview"),
    url(r'^help/new/$', views.CreateHelp.as_view(), name="create"),
]
