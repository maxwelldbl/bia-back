from django.urls import path
from seguridad.views import choices_views as views


urlpatterns = [
    # Choices
    path('paises/', views.PaisesChoices.as_view(), name='paises'),
    path('indicativo-paises/', views.IndicativoPaisesChoices.as_view(), name='indicativo-paises'),
    path('departamentos/', views.DepartamentosChoices.as_view(), name='departamentos'),
    path('municipios/', views.MunicipiosChoices.as_view(), name='municipios'),
    path('estado-civil/', views.EstadoCivilChoices.as_view(), name='sexo'),
    path('sexo/', views.SexoChoices.as_view(), name='sexo'),
    path('subsistemas/', views.SubsistemasChoices.as_view(), name='subsistemas'),
    path('cod-permiso/', views.CodPermisoChoices.as_view(), name='cod-permiso'),
    path('opciones-usuario/', views.OpcionesUsuarioChoices.as_view(), name='opciones-usuario'),
    path('tipo-direccion/', views.TipoDireccionChoices.as_view(), name='tipo-direccion'),
    path('tipo-documento/', views.TipoDocumentoChoices.as_view(), name='tipo-documento'),
    path('tipo-persona/', views.TipoPersonaChoices.as_view(), name='tipo-persona'),
    path('tipo-usuario/', views.TipoUsuarioChoices.as_view(), name='tipo-usuario'),
    path('direcciones/', views.DireccionesChoices.as_view(), name='direcciones')
]