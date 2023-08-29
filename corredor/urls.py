from corredor import views
from django.urls import path


urlpatterns = [

    path('', views.listar_corredores, name='home'),
    path('eliminar/<int:pk>', views.eliminar_corredor, name='eliminar'),
    path('crear/', views.crear_corredor, name='crear'),
    path('actualizar/<int:pk>', views.actualizar_corredor, name='actualizar'),
    path('mostrar/<int:pk>', views.detalle_corredor, name='mostrar'),

]
