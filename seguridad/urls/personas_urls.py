from django.urls import path
from seguridad.views import personas_views as views


urlpatterns = [
    
    # Estado Civil 
    path('estado-civil/get-list/', views.GetEstadoCivil.as_view(), name="estado-civil-get"),
    path('estado-civil/get-by-id/<str:pk>/', views.GetEstadoCivilById.as_view(), name='estado-civil-id-get'),
    path('estado-civil/delete/<str:pk>/', views.DeleteEstadoCivil.as_view(), name='estado-civil-delete'),
    path('estado-civil/create/', views.RegisterEstadoCivil.as_view(), name='estado-civil-register'),
    path('estado-civil/update/<str:pk>', views.UpdateEstadoCivil.as_view(), name='estado-civil-update'),

    # Tipo Documento 
    path('tipos-documento/get-list/', views.GetTipoDocumento.as_view(), name="tipo-documento-get"),
    path('tipos-documento/get-by-id/<str:pk>/', views.GetTipoDocumentoById.as_view(), name='tipo-documento-id-get'),
    path('tipos-documento/delete/<str:pk>/', views.DeleteTipoDocumento.as_view(), name='tipo-documento-delete'),
    path('tipos-documento/create/', views.RegisterTipoDocumento.as_view(), name='tipo-documento-register'),
    path('tipos-documento/update/<str:pk>', views.UpdateTipoDocumento.as_view(), name='estado-civil-update'),

    
    # Personas 
    path('get-list/', views.GetPersonas.as_view(), name="personas-get"),
    path('get-by-email/<str:pk>/', views.getPersonaByEmail, name='persona-email-get'),
    path('get-personas-by-document/<str:tipodocumento>/<str:numerodocumento>/', views.GetPersonasByTipoDocumentoAndNumeroDocumento.as_view(), name='persona-by-document-and-tipo-documento-get'),
    path('get-personas-naturales-by-document/<str:tipodocumento>/<str:numerodocumento>/', views.GetPersonaNaturalByTipoDocumentoAndNumeroDocumento.as_view(), name='persona-natural-by-document-and-tipo-documento-get'),
    path('get-personas-juridicas-by-document/<str:tipodocumento>/<str:numerodocumento>/', views.GetPersonaJuridicaByTipoDocumentoAndNumeroDocumento.as_view(), name='persona-juridica-by-document-and-tipo-documento-get'),
    path('get-personas-naturales/', views.GetPersonaNatural.as_view(), name='persona-natural-get'),
    path('get-personas-juridicas/', views.GetPersonaJuridica.as_view(), name='persona-juridica-get'),
    path('persona-natural/usuario-interno/self/update/', views.UpdatePersonaNaturalInternoBySelf.as_view(), name='persona-natural-update-by-self'),
    path('persona-natural/usuario-externo/self/update/', views.UpdatePersonaNaturalExternoBySelf.as_view(), name='persona-natural-update-by-self'),
    path('persona-natural/user-with-permissions/update/<str:pk>/', views.UpdatePersonaNaturalByUserWithPermissions.as_view(), name='persona-natural-update-by-user-with-permissions'),
    path('persona-juridica/usuario-interno/self/update/', views.UpdatePersonaJuridicaInternoBySelf.as_view(), name='persona-natural-update-by-self'),
    path('persona-juridica/usuario-externo/self/update/', views.UpdatePersonaJuridicaExternoBySelf.as_view(), name='persona-natural-update-by-self'),
    path('persona-juridica/user-with-permissions/update/<str:pk>/', views.UpdatePersonaJuridicaByUserWithPermissions.as_view(), name='persona-natural-update-by-user-with-permissions'),
    path('persona-natural/create/', views.RegisterPersonaNatural.as_view(), name='persona-natural-register'),
    path('persona-juridica/create/', views.RegisterPersonaJuridica.as_view(), name='persona-juridica-register'),
    path('delete/<str:pk>/', views.deletePersona.as_view(), name='persona-delete'),
    
    # Apoderados Personas
    path('apoderados-personas/get-list/', views.getApoderadosPersona.as_view(), name="apoderados-personas-get"),
    path('apoderados-personas/get-by-id/<str:pk>/', views.getApoderadoPersonaById.as_view(), name='apoderado-persona-id-get'),
    path('apoderados-personas/delete/<str:pk>/', views.deleteApoderadoPersona.as_view(), name='apoderado-persona-delete'),
    path('apoderados-personas/update/<str:pk>/', views.updateApoderadoPersona.as_view(), name='apoderado-persona-update'),
    path('apoderados-personas/create/', views.registerApoderadoPersona.as_view(), name='apoderado-persona-register'),
    
    # Sucursales Empresas
    path('sucursales-empresas/get-list/', views.getSucursalesEmpresas.as_view(), name="sucursales-empresas-get"),
    path('sucursales-empresas/get-by-id/<str:pk>/', views.getSucursalEmpresaById.as_view(), name='sucursal-empresa-id-get'),
    path('sucursales-empresas/delete/<str:pk>/', views.deleteSucursalEmpresa.as_view(), name='sucursal-empresa-delete'),
    path('sucursales-empresas/update/<str:pk>/', views.updateSucursalEmpresa.as_view(), name='sucursal-empresa-update'),
    path('sucursales-empresas/create/', views.registerSucursalEmpresa.as_view(), name='sucursal-empresa-register'),
    
    # Historico Emails
    path('historico-emails/get-list/', views.getHistoricoEmails.as_view(), name="historico-emails-get"),
    
    # Historico Direcciones
    path('historico-direcciones/get-list/', views.GetHistoricoDirecciones.as_view(), name="historico-direcciones-get"),
      
    # Clases Tercero
    # path('clases-tercero/get-list/', views.getClasesTercero.as_view(), name="clases-tercero-get"),
    # path('clases-tercero/get-by-id/<str:pk>/', views.getClaseTerceroById.as_view(), name='clase-tercero-id-get'),
    # path('clases-tercero/delete/<str:pk>/', views.deleteClaseTercero.as_view(), name='clase-tercero-delete'),
    # path('clases-tercero/update/<str:pk>/', views.updateClaseTercero.as_view(), name='clase-tercero-update'),
    # path('clases-tercero/create/', views.registerClaseTercero.as_view(), name='clase-tercero-register'),
    
    # Clases Tercero Personas
    # path('clases-tercero-personas/get-list/', views.getClasesTerceroPersonas.as_view(), name="clases-tercero-personas-get"),
    # path('clases-tercero-personas/get-by-id/<str:pk>/', views.getClaseTerceroPersonaById.as_view(), name='clase-tercero-persona-id-get'),
    # path('clases-tercero-personas/delete/<str:pk>/', views.deleteClaseTerceroPersona.as_view(), name='clase-tercero-persona-delete'),
    # path('clases-tercero-personas/update/<str:pk>/', views.updateClaseTerceroPersona.as_view(), name='clase-tercero-persona-update'),
    # path('clases-tercero-personas/create/', views.registerClaseTerceroPersona.as_view(), name='clase-tercero-persona-register'),

]