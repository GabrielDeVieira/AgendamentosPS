"""p01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Agendamento import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('createHor/', views.createTbHorarios),
    path('updateHor/<int:id>/', views.updateTbHorarios, name="url_update4"),
    path('deletarHor/<int:id>/', views.deleteTbHorarios, name="url_delete4"),
    
    path('cadastro/', views.cadastro, name= 'cadastro'),
    
    
    path('', views.login, name= 'login'),
    path('inicio/', views.inicio,),
    path('agendamentos/', views.viTbAgendamentos,),
    path('localdetrabalho/', views.viTbLocal),
    path('createLoc/', views.createTbLocal),
    path('updateLoc/<int:id>/', views.updateTbLocal, name="url_update3"),
    path('deletarLoc/<int:id>/', views.deleteTbLocal, name="url_delete3"),
    path('createBai/', views.createTbBairros),
    path('updateBai/<int:id>/', views.updateTbBairros, name="url_update2"),
    path('deletarBai/<int:id>/', views.deleteTbBairros, name="url_delete2"),
    path('createEst/', views.createTbEstados),
    path('updateEst/<int:id>/', views.updateTbEstados, name="url_update"),
    path('deletarEst/<int:id>/', views.deleteTbEstados, name="url_delete"),
    path('createCid/', views.createTbCidades),
    path('updateCid/<int:id>/', views.updateTbCidades, name="url_update1"),
    path('deletarCid/<int:id>/', views.deleteTbCidades, name="url_delete1"),
    path('user/', views.usesof, name= 'user'),
    path('agendamentosdia/<int:id>/', views.viTbAgendamentosdia, name= 'agendamentosdia1'),
    
    path('createAgm/', views.createTbAgendamentosmes),
    path('updateAgm/<int:id>/', views.updateTbAgendamentosmes, name="url_update8"),
    path('deletarAgm/<int:id>/', views.deleteTbAgendamentosmes, name="url_delete8"),
    
    
]
    #path('registrar/', UsuarioCreate.as_view(), name='registrar'),


