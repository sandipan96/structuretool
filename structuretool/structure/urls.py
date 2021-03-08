from django.urls import path
from . import views
from .views import (
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    AlloyListCreate,
    AlloyListView
)

urlpatterns = [
    path('', views.home, name = 'structure-home'),
    path('choice/', views.choicePage, name = 'structure-choice'),
    path('choice/projectList/',ProjectListView.as_view(), name = 'projectList'),
    path('choice/projectList/<int:pk>/',ProjectDetailView.as_view(), name = 'ProjectDetails-detail'),
    path('choice/projectList/<int:pk>/update/',ProjectUpdateView.as_view(), name = 'ProjectDetails-update'),
    path('choice/projectList/<int:pk>/delete/',ProjectDeleteView.as_view(), name = 'ProjectDetails-delete'),
    path('choice/projectList/new/',ProjectCreateView.as_view(), name = 'ProjectDetails-create'),
    path('choice/projectList/structureCalc/',AlloyListCreate.as_view(), name = 'structureCalc'),
    path('choice/projectList/structureCalc/alloyEdit/',AlloyListView.as_view(), name = 'alloyEdit'),
    #path('choice/projectList/structureCalc/delete/',AlloyDeleteView.as_view(), name = 'AlloyGrade-delete'),
    path('choice/projectList/structureCalc/structSpecs/',views.structSpecs, name = 'structSpecs'),
]