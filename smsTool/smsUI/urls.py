from django.urls import path, include
from smsUI.views import home, personalHome, register

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('personalHome/', personalHome, name='personalHome'),
    path('register/', register, name='register')
]
