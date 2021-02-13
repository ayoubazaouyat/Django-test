from django.conf.urls import url 
from projapp import views
app_name= 'projapp'
urlpatterns = [
    url('signup/',views.register,name='register'),
    url('login/',views.login_page,name='login')
]
