from django.urls import path, include
from smsUI.views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('personalHome_s/', personalHome_shortcut.as_view(), name='personalHome'),
    path('personalHome/<slug:slug>/', personalHome.as_view(), name='personalHome_notWorking'),
    path('register/', register, name='register'),
    path('editPersonalSkills/', editPersonalSkills, name='editPersonalSkills'),
    path('newSkillElement/', addSkill, name='newSkillElement'),
    path('newSkillsSet/', addSkillsSet, name='newSkillsSet'),
    path('editUserProfile/', editUserProfile, name='editUserProfile'),
    path('settings/', settings, name='settings'),
    path('editSeniority/', editSeniority.as_view(), name='editSeniority'),
    path('editSeniority/editSeniorityRank/<int:seniority_id><str:operation>', editSeniorityRank, name='editSeniorityRank'),
    path('editSeniority/deleteSeniority/<int:seniority_id>', deleteSeniority, name='deleteSeniority'),
    path('newSeniority/', addSeniority, name='newSeniority')
]
