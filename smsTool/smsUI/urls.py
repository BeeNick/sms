from django.urls import path, include
from smsUI.views import home, personalHome, register, personalHome_shortcut, editPersonalSkills

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('personalHome_s/', personalHome_shortcut.as_view(), name='personalHome'),
    path('personalHome/<slug:slug>/', personalHome.as_view(), name='personalHome_notWorking'),
    path('register/', register, name='register'),
    path('editPersonalSkills/', editPersonalSkills, name='editPersonalSkills')
]
