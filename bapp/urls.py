from django.urls import path
from .views import Bloglist, Blogcreate, Blogupdate, Blogdelete, Blogdetail

app_name='bapp'
urlpatterns = [
    path('', Bloglist.as_view(), name="list"),
    path('create/', Blogcreate.as_view(), name='create'),
    path('update/<int:pk>/', Blogupdate.as_view(), name='update'),
    path('delete/<int:pk>/', Blogdelete.as_view(), name='delete'),
    path('detail/<int:pk>/', Blogdetail.as_view(), name='detail'),

]