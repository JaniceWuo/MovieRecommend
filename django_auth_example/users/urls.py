from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    # url(r'showregist/$',views.showregist),
    url(r'recommend/$',views.recommend),
]