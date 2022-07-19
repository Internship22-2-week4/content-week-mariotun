from wsgiref.simple_server import demo_app
from django.urls import path
from django.db import router


#Django rest framework
from rest_framework.routers import DefaultRouter

#views
#from . import views
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories',CategoryViewSet)

urlpatterns = router.urls

urlpatterns += [
    
    #path('',views.index, name='index'),
    #path('author/<int:author_id>',views.author, name='author'),
    #path('category/<int:category_id>',views.category, name='category')
]