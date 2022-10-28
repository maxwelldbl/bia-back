from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from seguridad.choices.paises_choices import paises_CHOICES
from seguridad.choices.departamentos_choices import departamentos_CHOICES
from seguridad.choices.municipios_choices import municipios_CHOICES
from seguridad.choices.cod_permiso_choices import cod_permiso_CHOICES
from seguridad.choices.tipo_persona_choices import tipo_persona_CHOICES
from seguridad.choices.sexo_choices import sexo_CHOICES
from seguridad.choices.tipo_direccion_choices import tipo_direccion_CHOICES
from seguridad.choices.subsistemas_choices import subsistemas_CHOICES
from seguridad.choices.tipo_usuario_choices import tipo_usuario_CHOICES
from seguridad.choices.opciones_usuario_choices import opciones_usuario_CHOICES

from django.conf import settings
from random import choice, choices
from string import ascii_letters, digits

# Modelos proveedores para Persona


class Sexo(models.Model):
    cod_sexo = models.CharField(max_length=1, db_column='T004CodSexo')
    nombre = models.CharField(max_length=20, db_column='T004nombre')

    def __str__(self):  
        return str(self.nombre)
    
    class Meta:
        db_table = 'T004Sexo'
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexo'
 
 
class Paises(models.Model):
    nombre = models.CharField(max_length=50, db_column='T003nombre')
    cod_pais = models.CharField(primary_key=True, max_length=2, db_column='T003CodPais')
    
    def __str__(self):
        return str(self.cod_pais)
    
    class Meta:
        db_table = "T003Paises"
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'


class Departamento(models.Model):
    nombre = models.CharField(max_length=30, db_column='T002nombre')
    pais = models.CharField(max_length=2, choices=paises_CHOICES, db_column='T002Cod_Pais')
    cod_departamento = models.CharField(primary_key=True, max_length=2, db_column='T002CodDepartamento')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'T002DepartamentosPais'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Municipio(models.Model):
    nombre = models.CharField(max_length=30, db_column='T001nombre')
    cod_departamento = models.CharField(max_length=2, choices=departamentos_CHOICES, db_column='T001Cod_Departamentos')
    cod_municipio = models.CharField(primary_key=True, max_length=5, db_column='T001CodMunicipio')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'T001MunicipiosDepartamento'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class TipoDocumento(models.Model):
    cod_tipo_documento = models.CharField(max_length=2, primary_key=True, unique=True, db_column='T006CodTipoDocumentoID')
    nombre = models.CharField(max_length=40, db_column='T006nombre')
    precargado = models.BooleanField(default=False, db_column='T006registroPrecargado')
    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        db_table = 'T006TiposDocumentoID'
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'


class EstadoCivil(models.Model):
    cod_estado_civil = models.CharField(max_length=1, primary_key=True, unique=True, db_column='T005CodEstadoCivil')
    nombre = models.CharField(max_length=20, db_column='T005nombre')
    precargado = models.BooleanField(default=False, db_column='T006registroPrecargado')

    
    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        db_table = 'T005EstadoCivil'
        verbose_name = 'Estado civil'
        verbose_name_plural = 'Estados civiles'


class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True, editable=False, db_column='T010IdPersona')
    tipo_persona = models.CharField(max_length=1, choices=tipo_persona_CHOICES, db_column='T010tipoPersona')
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, db_column='T010Cod_TipoDocumento')
    numero_documento = models.CharField(max_length=20, db_column='T010nroDocumentoID')
    digito_verificacion = models.CharField(max_length=1, null=True, blank=True, db_column='T010digitoVerificacion')
    primer_nombre = models.CharField(max_length=30, null=True, blank=True, db_column='T010primerNombre')
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True, db_column='T010segundoNombre')
    primer_apellido = models.CharField(max_length=30, null=True, blank=True, db_column='T010primerApellido')
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True, db_column='T010segundoApellido')
    nombre_comercial = models.CharField(max_length=200, null=True, blank=True, db_column='T010nombreComercial')
    razon_social = models.CharField(max_length=200, null=True, blank=True, db_column='T010razonSocial')
    pais_residencia = models.CharField(max_length=2, null=True, blank=True, choices=paises_CHOICES, db_column='T010Cod_PaisResidenciaExterior')
    municipio_residencia = models.CharField(max_length=5,choices=municipios_CHOICES, null=True, blank=True, db_column='T010Cod_MunicipioResidenciaNal')
    direccion_residencia = models.CharField(max_length=255, null=True, blank=True, db_column='T010dirResidencia')
    direccion_residencia_ref = models.CharField(max_length=255, null=True, blank=True, db_column='T010dirResidenciaReferencia')
    ubicacion_georeferenciada = models.CharField(max_length=50, db_column='T010dirRecidenciaGeoref')
    direccion_laboral = models.CharField(max_length=255, null=True, blank=True, db_column='T010dirLaboralNal')
    direccion_notificaciones = models.CharField(max_length=255, null=True, blank=True, db_column='T010dirNotificacionNal')
    pais_nacimiento = models.CharField(max_length=2, null=True, blank=True, choices=paises_CHOICES, db_column='T010Cod_PaisNacimiento')
    fecha_nacimiento = models.DateField(blank=True,null=True, db_column='T010FechaNacimiento')
    sexo = models.CharField(max_length=1, null=True, blank=True, choices=sexo_CHOICES, db_column='T010Cod_Sexo')
    estado_civil = models.ForeignKey(EstadoCivil, related_name="estado_civil", on_delete=models.SET_NULL, null=True, blank=True, db_column='T010Cod_EstadoCivil')
    representante_legal = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, db_column='T010Id_PersonaRepLegal')
    email = models.EmailField(max_length=255, unique=True, db_column='T010emailNotificación')
    email_empresarial = models.EmailField(max_length=255, null=True, blank=True, db_column='T010emailEmpresarial')
    telefono_fijo_residencial = models.CharField(max_length=15, null=True, blank=True, db_column='T010telFijoResidencial')
    telefono_celular = models.CharField(max_length=15, db_column='T010telCelularPersona')
    telefono_empresa = models.CharField(max_length=15, null=True, blank=True, db_column='T010telEmpresa')
    cod_municipio_laboral_nal = models.CharField(max_length=5, choices=municipios_CHOICES, null=True, blank=True, db_column='T010Cod_MunicipioLaboralNal')
    cod_municipio_notificacion_nal = models.CharField(max_length=5, choices=municipios_CHOICES, null=True, blank=True, db_column='T010Cod_MunicipioNotificacionNal')
    telefono_celular_empresa = models.CharField(max_length=15, blank=True, null=True, db_column='T010telCelularEmpresa')
    telefono_empresa_2 = models.CharField(max_length=15, null=True, blank=True, db_column='T010telEmpresa2')
    cod_pais_nacionalidad_empresa = models.CharField(max_length=2, null=True, blank=True, choices=paises_CHOICES, db_column='T010Cod_PaisNacionalidadDeEmpresa')
    acepta_notificacion_sms = models.BooleanField(default=True, db_column='T010aceptaNotificacionSMS')
    acepta_notificacion_email = models.BooleanField(default=True, db_column='T010aceptaNotificacionEmail')
    acepta_tratamiento_datos = models.BooleanField(default=True, db_column='T010aceptaTratamientoDeDatos')
    
    def __str__(self):
        return str(self.primer_nombre) + ' ' + str(self.primer_apellido)
    
    class Meta:
        db_table = 'T010Personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        unique_together = ['tipo_documento', 'numero_documento']

# Tablas producidas a partir de Persona


class HistoricoDireccion(models.Model):
    id_historico_direccion = models.AutoField(primary_key=True, editable=False, db_column='T015IdHistoDireccion')
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, db_column = 'T015Id_Persona')    
    direccion = models.CharField(max_length=255, db_column='T015direccion')
    cod_municipio = models.CharField(max_length=5, choices=municipios_CHOICES, null=True, blank=True, db_column='T015Cod_MunicipioEnCol')
    cod_pais_exterior = models.CharField(max_length=2, choices=paises_CHOICES, null=True,  db_column='T015Cod_PaisEnElExterior')
    tipo_direccion = models.CharField(max_length=3, choices=tipo_direccion_CHOICES, db_column='T015tipoDeDireccion')
    fecha_cambio = models.DateTimeField(auto_now_add=True, db_column='T015fechaCambio')
        
    def __str__(self):
        return str(self.id_historico_direccion)

    class Meta:
        db_table = 'T015HistoricoDirecciones'
        verbose_name = 'Histórico de dirección'
        verbose_name_plural = 'Histórico de direcciones'


class ApoderadoPersona(models.Model):
    consecutivo_del_proceso = models.AutoField(primary_key=True, editable=False, db_column = 'T013ConsecDelProceso') #Pendiente por foreingKey de tabla procesos
    id_proceso = models.CharField(max_length=50, db_column = 'T013IdProceso') #Pendiente por foreingKey de tabla procesos
    persona_poderdante = models.ForeignKey(Personas, on_delete=models.CASCADE, db_column='T013IdPersonaPoderdante')
    persona_apoderada = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='persona_apoderada', db_column = 'T013IdPersonaApoderada')
    fecha_inicio = models.DateTimeField(db_column='T013fechaInicio')
    fecha_cierre = models.DateTimeField(db_column='T013fechaCierre', null=True, blank=True)
    
    def __str__(self):
        return str(self.id_proceso)

    class Meta:
        db_table = 'T013Apoderados_Persona'    
        verbose_name = 'Apoderado'
        verbose_name_plural = 'Apoderados'


class HistoricoEmails(models.Model):
    id_histo_email = models.AutoField(primary_key=True, db_column='T016IdHistoEmail')
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, db_column='T016Id_Persona')
    email_notificacion = models.EmailField(max_length=100, db_column='T016emailDeNotificacion')
    fecha_cambio = models.DateTimeField(auto_now=True, db_column='T016fechaCambio')

    def __str__(self):
        return str(self.email_notificacion)

    class Meta:
        db_table = 'T016HistoricoEmails'      
        verbose_name = 'Historico de email'
        verbose_name_plural = 'Históricos de email'


class SucursalesEmpresas(models.Model):
    id_persona_empresa = models.ForeignKey(Personas,on_delete=models.CASCADE,  db_column='T012IdPersonaEmpresa')
    numero_sucursal = models.AutoField(primary_key=True, editable=False, db_column='T012NroSucursal')
    sucursal = models.CharField(max_length=255, db_column='T012sucursal')
    municipio = models.CharField(max_length=5, choices=municipios_CHOICES, null=True, blank=True, db_column='T012Cod_MunicipioSucursalNal')
    direccion = models.CharField(max_length=255, db_column='T012dirSucursal')
    direccion_sucursal_georeferenciada = models.CharField(max_length=50, db_column='T012dirSucursalGeoref')
    pais_sucursal_exterior = models.CharField(max_length=2, choices=paises_CHOICES, db_column='T012cod_PaisSucursalExterior')
    direccion_notificacion = models.CharField(max_length=50, db_column='T012dirNotificacionNal')
    municipio_notificacion = models.CharField(max_length=5, choices=municipios_CHOICES, db_column='T012Cod_MunicipioNotificacionNal') 
    email_sucursal = models.EmailField(max_length=255, db_column='T012emailSucursal')
    telefono_sucursal = models.CharField(max_length=10, db_column='T012telContactoSucursal')
    es_principal = models.BooleanField(default=False, db_column='T012esPrincipal')
    
    def __str__(self):
        return str(self.sucursal)
    
    class Meta:
        db_table = 'T012SucursalesEmpresa'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'


class ClasesTercero(models.Model):
    id_clase_tercero = models.AutoField(primary_key=True, editable=False, db_column='T007IdClaseTercero')
    nombre = models.CharField(max_length=30, db_column='T007nombre')
    
    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'T007ClasesTercero'
        verbose_name = 'Clase tercero'
        verbose_name_plural = 'Clase terceros'


class ClasesTerceroPersona(models.Model):
    id_clase_tercero_persona = models.AutoField(primary_key=True, editable=False, db_column='T011IdClaseTerceroPersona')
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, db_column='T011IdClaseTercero')
    id_clase_tercero = models.ForeignKey(ClasesTercero, on_delete=models.CASCADE, db_column='T011IdPersona')
    
    def __str__(self):
        return str(self.id_persona) + ' ' + str(self.id_clase_tercero)
    
    class Meta:
        db_table = 'T011ClasesTercero_Persona'
        constraints = [models.UniqueConstraint(fields=['id_persona', 'id_clase_tercero'], name='clases-tercero-persona')]
        verbose_name = 'Clase tercero persona'
        verbose_name_plural = 'Clase tercero personas'


# Tablas para proveer Usuarios

class OperacionesSobreUsuario(models.Model):
    cod_operacion = models.AutoField(primary_key=True, editable=False, db_column='T008CodOperacion')
    nombre = models.CharField(max_length=20, db_column='T008nombre')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'T008OperacionesSobreUsusario'
        verbose_name = 'Operacion sobre usuario'
        verbose_name_plural = 'Operaciones sobre usuario'


class Permisos(models.Model):
    nombre_permiso = models.CharField(max_length=20, db_column='Tznombre')
    cod_permiso = models.CharField(max_length=2, primary_key=True, choices=cod_permiso_CHOICES, db_column='TzCodPermiso')

    def __str__(self):
        return str(self.nombre_permiso)

    class Meta:
        db_table = "TzPermisos"
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        
    
class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True, editable=False, db_column='TzIdRol')
    nombre_rol = models.CharField(max_length=100, db_column='Tznombre')
    descripcion_rol = models.CharField(max_length=255, db_column='Tzdescripcion')
    Rol_sistema = models.BooleanField(default=False, db_column='TXrolDelSistema')
    
    def __str__(self):
        return str(self.nombre_rol)
    
    class Meta:
        db_table= 'TzRoles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
        
class Modulos(models.Model): 
    id_modulo = models.AutoField(primary_key=True, editable=False, db_column='TzIdModulo')
    nombre_modulo = models.CharField(max_length=70, db_column='Tznombre')
    subsistema = models.CharField(max_length=4, choices=subsistemas_CHOICES, db_column='Tzsubsistema')# Juan camilo textchoices 
    descripcion = models.CharField(max_length=255, db_column='Tzdescripcion')
     
    def __str__(self):
        return str(self.nombre_modulo)
    
    class Meta:
        db_table= 'TzModulos'
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'       
    

class PermisosModulo(models.Model):
    id_permisos_modulo= models.AutoField(primary_key=True,db_column='TzIdPermisos_Modulo' )
    id_modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='TzIdModulo')
    cod_permiso = models.ForeignKey(Permisos, on_delete=models.CASCADE, db_column='TzCodPermiso')
  
    def __str__(self):
        return str(self.id_modulo) + ' ' + str(self.cod_permiso)
    
    class Meta:
        db_table= 'TzPermisos_Modulo'
        constraints = [models.UniqueConstraint(fields=['id_modulo', 'cod_permiso'], name='permisos-modulo')]
        verbose_name = 'Permiso de módulo'
        verbose_name_plural = 'Permisos de módulo'


class PermisosModuloRol(models.Model):
    id_permiso_modulo_rol = models.AutoField(primary_key=True, db_column='IdPermisoModuloRol')
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='TzIdRol')
    id_permiso_modulo = models.ForeignKey(PermisosModulo, on_delete=models.CASCADE, db_column='TzIdPermiso_Modulo')
    
    def __str__(self):
        return str(self.id_rol) + ' ' + str(self.id_permiso_modulo) + ' ' + str(self.id_permiso_modulo_rol)
    
    class Meta:
        db_table= 'TzPermisos_Modulo_Rol'
        constraints = [models.UniqueConstraint(fields=['id_rol', 'id_permiso_modulo'], name='permiso_modulo_rol')]
        verbose_name = 'Permiso de modulo de rol'
        verbose_name_plural = 'Permisos de modulo de roles'
        

class User(AbstractBaseUser, PermissionsMixin):   
    id_usuario = models.AutoField(primary_key=True, editable=False, db_column='TzIdUsuario')
    nombre_de_usuario = models.CharField(max_length=30, db_column='TznombreUsuario')
    persona = models.OneToOneField(Personas, on_delete=models.CASCADE, db_column='TzId_Persona')
    is_active = models.BooleanField(max_length=1, default=False, db_column='Tzactivo')
    is_staff = models.BooleanField(default=False, db_column='Tzstaff')#Añadido por Juan
    is_superuser = models.BooleanField(default=False, db_column='TzsuperUser')  #Añadido por Juan
    is_blocked = models.BooleanField(max_length=1, default=False, db_column='Tzbloqueado')
    creado_por_portal = models.BooleanField(default=False, db_column='TzcreadoPorPortal')
    id_usuario_creador = models.ForeignKey('self', on_delete=models.SET_NULL,null=True, db_column="TzId_UsuarioCreador")
    created_at = models.DateTimeField(auto_now_add=True, db_column='TzfechaCreacion')
    activated_at = models.DateTimeField(null=True, db_column='TzfechaActivacionInicial')
    is_creado_por_portal= models.BooleanField(default=True, db_column='TZcreadoPorPortal')
    tipo_usuario = models.CharField(max_length=1,null=True, choices=tipo_usuario_CHOICES, db_column='TztipoUsuario')
    profile_img = models.ImageField(null=True, blank=True, default='/placeholder.png', db_column='tzrutaFoto') #Juan Camilo Text Choices
    email = models.EmailField(unique=True, db_column='TzemailUsuario') #Añadido por Juan
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{'refresh': str(refresh), 'access': str(refresh.access_token)}
    
    class Meta:
        db_table = 'TzUsuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

# Tablas generadas a partir de User

class Login(models.Model):
    id_login = models.AutoField(primary_key=True, editable=False, db_column='TzIdLogin')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='TzId_Usuario')
    dirip = models.CharField(max_length=40, db_column='TzdirIP')
    dispositivo_conexion = models.CharField(max_length=30, db_column='TzdispositivoConexion')
    fecha_login = models.DateTimeField(auto_now=True, db_column='TzfechaLogin')
    fecha_hora_cierre_sesion = models.DateTimeField(blank=True, null=True, db_column='TzfechaHoraCierreSesion')
    
    def __str__(self):
        return str(self.id_usuario)
    
    class Meta:
        db_table = 'TzLogin'
        verbose_name = 'Login'
        verbose_name_plural = 'Login'   

    
class LoginErroneo(models.Model):
    id_login_error = models.AutoField(primary_key=True, editable=False, db_column='TzIdLoginError')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='TzId_Usuario')
    dirip = models.CharField(max_length=40, db_column='TzdirIP')
    dispositivo_conexion = models.CharField(max_length=30, db_column='TzdispositivoConexion')
    fecha_login_error = models.DateTimeField(auto_now=True, db_column='TzfechaLoginError')
    contador = models.IntegerField(db_column='Tzcontador')
    
    def __str__(self):
        return str(self.id_usuario)
    
    class Meta:
        db_table = 'TzLoginErroneo'
        verbose_name = 'Login Erroneo'
        verbose_name_plural = 'Login Erroneo'
        

class UsuariosRol(models.Model):
    id_usuarios_rol = models.AutoField(primary_key=True, editable=False, db_column='TzIdUsuarios_Rol')
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='TzId_Rol')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='TzId_Usuario')

    def __str__(self):
        return str(self.id_rol) + ' ' + str(self.id_usuario)

    class Meta:
        db_table = 'TzUsuarios_Rol'
        constraints = [models.UniqueConstraint(fields=['id_rol', 'id_usuario'], name='permiso_modulo')]
        verbose_name = 'Rol de usuario'
        verbose_name_plural = 'Roles de usuario'


class Auditorias(models.Model):
    id_auditoria = models.AutoField(db_column='TzIdAuditoria', primary_key=True, editable=False)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='TzId_Usuario') ##No tiene definido tipo de relacion
    id_modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE, db_column='TzId_Modulo')
    id_cod_permiso_accion = models.ForeignKey(Permisos, on_delete=models.CASCADE, db_column='TzCod_PermisoAccion')
    fecha_accion = models.DateField(db_column='TzfechaAccion')
    subsistema = models.CharField(max_length=4, choices=subsistemas_CHOICES, db_column='Tzsubsistema') #Juan camilo text choices
    dirip = models.CharField(max_length=255, db_column='Tzdirip')
    descripcion = models.TextField(db_column='Tzdescripcion')
    valores_actualizados = models.CharField(max_length=255, null=True, blank=True, db_column='TzvaloresActualizados')

    def __str__(self):
        return str(self.descripcion) 
  
    class Meta: 
        db_table ='TzAuditorias'
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
        
     
class HistoricoActivacion(models.Model):
    id_historico = models.AutoField(primary_key=True, editable=False, db_column='T014IdHistorico')
    id_usuario_afectado = models.ForeignKey(User, on_delete=models.CASCADE, db_column='T014Id_UsuarioAfectado')
    cod_operacion = models.CharField(max_length=1, choices=opciones_usuario_CHOICES, db_column='T014Cod_Operacion')
    fecha_operacion = models.DateTimeField(auto_now=True, db_column='T014fechaOperacion')
    justificacion = models.TextField(db_column='T014justificacion')
    usuario_operador = models.ForeignKey(User, related_name='usuarioOperador', on_delete=models.SET_NULL, null=True, blank=True, db_column='T014Id_UsuarioOperador')  #Añadido por Juan

    def __str__(self):
        return str(self.cod_operacion)

    class Meta:
        db_table = 'T014HistoricoActivacion'  
        verbose_name = 'Histórico de activación'
        verbose_name_plural = 'Histórico de activaciones'

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)    
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        db_table = 'Shortener'  
        verbose_name = 'Acortador'
        verbose_name_plural = 'Acortadores'
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        # Try to get the value from the settings module
        SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

        AVAIABLE_CHARS = ascii_letters + digits
        
        random_code = "".join(
            [choice(AVAIABLE_CHARS) for _ in range(SIZE)]
        )

        model_class = self.__class__
        
        exist = model_class.objects.filter(short_url=random_code).exists()
        
        while exist:
            random_code = "".join(
                [choice(AVAIABLE_CHARS) for _ in range(SIZE)]
            )
            
            exist = model_class.objects.filter(short_url=random_code).exists()
            
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = random_code

        super().save(*args, **kwargs)        