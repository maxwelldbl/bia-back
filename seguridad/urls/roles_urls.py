from django.urls import path
from seguridad.views import roles_views as views

urlpatterns = [
    path('get-list', views.GetRol.as_view(), name='roles'),
    path('get-by-id/<int:pk>/', views.GetRolById.as_view(), name='rol-id'),
    path('create/', views.RegisterRol.as_view(), name='rol-register'),
    path('update/<int:pk>/', views.UpdateRol.as_view(), name='rol-update'),
    path('delete/<int:pk>/', views.DeleteRol.as_view(), name='rol-delete'),  
    path('delete_rol_de_usuario/<int:pk>/', views.DeleteUserRol.as_view(), name='rol-delete'),  
    path('add-user-roles/',views.UserRolViewSet.as_view({'post':'create'}),name='add-user-roles'),
    path('detail_roles_usuario/', views.GetRolesByUser.as_view(), name='roles-por-usuario-ver'),
    path('detail_usuarios_rol/', views.GetUsersByRol.as_view(), name='usuarios-por-rol-ver'),
]