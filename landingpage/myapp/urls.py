from django.contrib import admin
from django.urls import path, include
from .views import home, about, signin, signout, contact, dashboard, signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about' ),
    path('login/', signin, name='signin'),
    path('contact/', contact, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
]
