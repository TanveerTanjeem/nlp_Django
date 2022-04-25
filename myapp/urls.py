from django.urls import include, path
from . import views

urlpatterns = [  
    path('',views.form),
    path('hello/', views.hello, name = 'hello'),  # app homepage
    path('article/<slug:username>',views.viewArticle, name = 'article'),
    path('article/',views.viewArticle),
    

]
