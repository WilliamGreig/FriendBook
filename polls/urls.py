from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/edit/<int:id>', views.edit),
    path('polls/delete/<int:id>', views.delete),
    path('polls/edit/polls/save', views.save),

]
