from django.urls import path , include
from . import views 

urlpatterns = [
#path ('vu/' , views.index , name='vu')
path ('' , views.index , name='index') , 
path ('<int:id>' , views.detail, name='detail'),
path ('edit/<int:id>' , views.edit, name='edit'),
path ('delete/<int:id>' , views.delete, name='delete'),

path ('new/' , views.new, name='new')
]

