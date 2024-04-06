# **1. Gestión de proyectos:**

## **Funcional:**

- **Crear, editar y eliminar proyectos:**
    - Permitir la creación de proyectos.
    - Posibilitar la edición de la información del proyecto, como nombre, descripción, fechas, etc.
    - Ofrecer la opción de eliminar proyectos ya finalizados o que no sean necesarios.
- **Establecer fechas de inicio y fin para los proyectos:**
    - Definir fechas flexibles que se puedan modificar según el avance del proyecto.
- **Definir el alcance del proyecto:**
	- Establecer hitos y objetivos intermedios dentro del proyecto.
    - Delimitar las tareas y actividades que se incluirán en el proyecto.
    - Especificar los recursos necesarios (a través de los objetivos) para completar el proyecto.
- **Asignación de recursos al proyecto:**
    - Asignar usuarios específicos a las diferentes tareas del proyecto.
    - Permitir la selección de equipos o grupos de trabajo para tareas colaborativas.
- **Establecer hitos y objetivos del proyecto:**
    - Definir puntos de control para medir el avance del proyecto.
- **Seguimiento del progreso del proyecto:**
    - Visualizar el avance general del proyecto en tiempo real.
    - Obtener información detallada sobre el estado de cada tarea individual.
- **Generar informes sobre el estado del proyecto:**
    - Informes para mostrar la información más relevante.

## **No funcional:**

- **La aplicación debe ser fácil de usar y navegar:**
    - Ofrecer una interfaz intuitiva y amigable para el usuario.
- **La aplicación debe ser segura y proteger la información confidencial del proyecto:**
    - Restringir el acceso a la información del proyecto solo a los usuarios autorizados.
    - Implementar medidas de seguridad para proteger la información contra accesos no autorizados.
- **La aplicación debe ser escalable para poder manejar proyectos de diferentes tamaños:**
    - Permitir la gestión de proyectos pequeños y grandes con la misma eficiencia.
    - Adaptarse a las necesidades cambiantes del proyecto a medida que avanza.
- **Ofrecer una experiencia de usuario óptima en cada dispositivo**.

## **Datos:**

- **Nombre del proyecto:**
    - Debe ser único e identificable.
    - Puede incluir una breve descripción del proyecto.
- **Descripción del proyecto:**
    - Detallar los objetivos, el alcance y las características del proyecto.
- **Fecha de inicio del proyecto:**
    - Indicar la fecha en que se dará inicio al proyecto.
    - Puede ser una fecha específica.
- **Fecha de fin del proyecto:**
    - Indicar la fecha en que se espera finalizar el proyecto.
    - Puede ser una fecha estimada o una fecha límite contractual.
- **Alcance del proyecto:**
    - Definir claramente las tareas y actividades que se incluirán en el proyecto.
    - Excluir las tareas que no están dentro del alcance del proyecto.
- **Recursos asignados al proyecto:**
    - Identificar los usuarios, equipos o grupos de trabajo que participarán en el proyecto.
    - Especificar las habilidades y roles de cada recurso.
- **Hitos y objetivos del proyecto:**
    - Definir puntos de control específicos para medir el avance del proyecto.
- **Progreso del proyecto:**
    - Indicar el porcentaje de avance del proyecto en tiempo real.
- **Información de los integrantes:**
    - Nombre, correo electrónico, rol dentro del proyecto, etc.
- **Permisos y roles:**
    - Definir diferentes niveles de acceso a la información del proyecto.
    - Asignar roles específicos a los usuarios (administrador, editor, colaborador, etc.).

# **2. Creación y asignación de tareas:**

## **Funcional:**

- **Crear, editar y eliminar tareas:**
    - Permitir la creación de tareas con diferentes niveles de detalle.
    - Posibilitar la edición de la información de la tarea, como nombre, descripción, fechas, etc.
    - Ofrecer la opción de eliminar tareas ya completadas o que no sean necesarias.
- **Asignar tareas a usuarios o equipos:**
    - Permitir la selección de usuarios específicos para cada tarea.
    - Posibilitar la asignación de tareas a equipos o grupos de trabajo.
- **Establecer prioridades para las tareas:**
    - Definir el nivel de importancia de cada tarea.
    - Permitir la modificación de las prioridades según las necesidades del proyecto.
- **Establecer fechas de inicio y fin para las tareas:**
    - Definir fechas flexibles que se puedan modificar según el avance de la tarea.
    - Establecer hitos y objetivos intermedios dentro de la tarea.
- **Agregar comentarios y notas a las tareas:**
    - Permitir la comunicación entre los usuarios sobre las tareas.
    - Facilitar el intercambio de información y ideas.
-  **Agregar, editar, eliminar etiquetas para las tareas:**
	- Permitir la creación de etiquetas con colores a las tareas.
	- Posibilitar la edición de la información de las etiquetas, como nombre, color, mediante la edición de tareas.
	- Ofrecer la opción de eliminar etiquetas que no sean necesarias.

## **No funcional:**

- **Las tareas deben poder ser ordenadas y filtradas según diferentes criterios:**
    - Permitir la ordenación por nombre, fecha, prioridad, estado, etc.
    - Ofrecer la posibilidad de filtrar las tareas por usuario, equipo, proyecto, etc.
- **Las tareas deben tener un sistema de notificaciones para avisar a los usuarios sobre cambios o actualizaciones:**
    - Notificar a los usuarios cuando se les asigne una nueva tarea.
    - Enviar notificaciones cuando se modifique la información de una tarea.
    - Alertar a los usuarios sobre la fecha límite de una tarea.

## Datos:

- **Nombre de la tarea:**
    - Debe ser único e identificable.
    - Puede incluir una breve descripción de la tarea.
- **Descripción de la tarea:**
    - Detallar las instrucciones, requisitos y objetivos de la tarea.
    - Incluir información sobre los recursos necesarios y las fechas clave.
- **Fecha de inicio de la tarea:**
    - Indicar la fecha en que se dará inicio a la tarea.
    - Puede ser una fecha específica.
- **Fecha de fin de la tarea:**
    - Indicar la fecha en que se espera finalizar la tarea.
    - Puede ser una fecha estimada o una fecha límite contractual.
- **Prioridad de la tarea:**
    - Indicar el nivel de importancia de la tarea.
    - Puede ser baja, media o alta.
- **Estado de la tarea:**
    - Indicar el estado actual de la tarea (pendiente, en curso, completada, etc.).
- **Usuario asignado a la tarea:**
    - Identificar el usuario responsable de la tarea.
- **Equipo asignado a la tarea:**
    - Identificar el equipo o grupo de trabajo responsable de la tarea.
- **Comentarios y notas sobre la tarea:**
    - Registrar la comunicación entre los usuarios sobre la tarea.
- Etiquetas:
	- Visualizar la etiqueta con un color.
	- Indicar el nombre de la etiqueta.

# **3. Seguimiento del progreso:**

## **Funcional:**

- **Visualizar el avance general del proyecto en tiempo real:**
    - Mostrar un gráfico o indicador que represente el progreso del proyecto.
    - Detallar el porcentaje de tareas completadas y en curso.
- **Obtener información detallada sobre el estado de cada tarea individual:**
    - Mostrar el nombre, la descripción, la fecha de inicio, la fecha de fin, la prioridad y el estado de cada tarea.
    - Permitir la visualización del estado de las tareas por proyecto, usuario, equipo...
	- Ofrecer la posibilidad de filtrar las tareas por diferentes criterios (estado, prioridad, fecha, etc.).
## No funcional:

- **Adaptarse a las necesidades cambiantes del proyecto a medida que avanza.**
- **Rendimiento:**
	- El apartado debe ser rápido y eficiente.
	- Los tiempos de respuesta deben ser mínimos.
- **Usabilidad:**
	- Debe ser fácil de usar y navegar.
	- Ofrecer una interfaz intuitiva y amigable para el usuario.
# **4. Generación de informes:**

## **Funcional:**

- **Generar informes sobre el estado del proyecto:**
    - Mostrar el avance general del proyecto, las tareas completadas y en curso, los hitos alcanzados, etc.
    - Permitir la comparación del progreso del proyecto con la planificación inicial.
- **Generar informes sobre la actividad de los usuarios:**
    - Mostrar el tiempo que cada usuario ha dedicado al proyecto.
    - Detallar las tareas que cada usuario ha completado.

## **No funcional:**
- **Los informes deben ser exportables a diferentes formatos:**
    - Ofrecer la posibilidad de exportar los informes a PDF, Excel, CSV, etc.

## **Datos**
- **Tipo de informe:**
    - Informe de progreso del proyecto, informe de actividad del usuario, etc.
- **Datos que se incluirán en el informe:**
    - Tareas completadas, tareas en curso, hitos alcanzados, tiempo dedicado por usuario, etc.
- **Formato del informe:**   
    - PDF, Excel, CSV, etc.

# **5. Notificaciones y recordatorios:**

## **Funcional:**

- **Notificar a los usuarios sobre cambios o actualizaciones en las tareas:**
    - Informar a los usuarios cuando se les asigne una nueva tarea.
    -  Informar a los usuarios cuando se le asigne al equipo una nueva tarea.
    - Enviar notificaciones cuando se modifique la información de una tarea.
    - Enviar notificaciones cuando se modifique la información de un proyecto.
- **Enviar recordatorios a los usuarios sobre las tareas pendientes:**
    - Notificar a los usuarios sobre las tareas que están próximas a vencer.

## **No funcional:**

- **Las notificaciones y recordatorios deben ser configurables:**
    - Permitir a los usuarios elegir qué tipo de notificaciones y recordatorios desean recibir.
    - Ofrecer la posibilidad de personalizar la frecuencia y el método de las notificaciones.

## **Datos**
- **Tipo de notificación:**
    - Correo electrónico, notificación push, etc.
- **Frecuencia de la notificación:**
    - Inmediata, diaria, semanal, etc.
- **Método de la notificación:**
    - Correo electrónico, notificación push, mensaje dentro de la aplicación, etc.


#  6. Gestión de usuarios:
## **Funcional:**

- **Crear, editar y eliminar usuarios:**
    - Permitir la creación de usuarios con diferentes niveles de acceso, desde usuarios básicos con acceso limitado hasta administradores con acceso total al sistema.
    - Posibilitar la edición de la información del usuario, como nombre, correo electrónico, rol, foto de perfil, preferencias de idioma, etc.
    - Ofrecer la opción de eliminar usuarios inactivos o que no sean necesarios, siguiendo un proceso que garantice la seguridad y la protección de datos.
- **Asignar roles y permisos a los usuarios:**
    - Definir diferentes roles con distintos niveles de acceso a la información y funcionalidades del sistema, por ejemplo, roles para empleados, editores, colaboradores y administradores.
    - Permitir la asignación de roles específicos a cada usuario según sus responsabilidades y necesidades dentro del sistema.
    - Ofrecer la posibilidad de modificar los roles y permisos de los usuarios de forma flexible para adaptarlos a los cambios en la organización o las necesidades del proyecto.
- **Restablecer contraseñas:**
    - Permitir a los usuarios restablecer sus contraseñas en caso de olvido mediante un proceso seguro que implique la verificación de la identidad del usuario.
    - Implementar un proceso de restablecimiento de contraseñas que sea fácil de usar y que no comprometa la seguridad del sistema.

## No funcional:

- **Autenticación multifactor:** Obligatoria para todos los usuarios con 2FA activado.
- **Encriptación de datos:** Encriptación de contraseñas y datos sensibles en reposo y en tránsito.
- **Usabilidad:**
	- **Interfaz intuitiva:** Adaptable a diferentes dispositivos.
	- **Sistema de ayuda y tutoriales:** Contextuales e interactivos..
- **Disponibilidad:**
	- **Mantenimiento preventivo:** Actualizaciones regulares, parches de seguridad y plan de recuperación ante desastres.
- **Compatibilidad:**
	- **Navegadores web y dispositivos:** Soporte para los más utilizados.
- **Personalización:**
	- **Configuración del perfil:** Permitir a los usuarios cambiar foto, nombre, contraseña, idioma, etc.

## Datos:
- **Información básica:**
    - Nombre completo
    - Nombre usuario
    - Correo electrónico
    - Contraseña
    - Foto de perfil
    - Número de teléfono
    - Fecha de nacimiento
- **Información adicional:**
    - Ubicación
    - Equipo
    - Rol
    - Empresa

# **7. Gestión de roles:**

## Funcional:

- **Crear, editar y eliminar roles:**
    - Permitir la creación de roles con diferentes niveles de acceso, desde roles básicos con permisos limitados hasta roles con acceso completo a todas las funcionalidades del sistema.
    - Posibilitar la edición de las características y permisos de cada rol para adaptarlos a las necesidades específicas de la organización.
    - Ofrecer la opción de eliminar roles que no sean necesarios, siguiendo un proceso que garantice la seguridad y la integridad del sistema.
- **Asignar permisos a los roles:**
    - Definir qué funcionalidades y datos puede acceder cada rol, incluyendo permisos de lectura, escritura, edición, eliminación, creación y gestión de otros usuarios, roles, equipos y empresas.
    - Permitir la configuración granular de permisos para cada acción dentro del sistema, por ejemplo, permisos para ver, editar, crear, eliminar tareas, proyectos, archivos, etc.

## No funcional:

- **Permisos granulares:** Definición de permisos específicos para cada acción dentro del sistema.
- **Usabilidad:**
	- **Interfaz intuitiva:** Para la creación, edición y eliminación de roles.
	- **Asignación flexible de permisos:** Permitir la configuración granular de permisos para cada rol.
- **Integración con la gestión de usuarios:** Permitir la asignación de roles a usuarios.

## Datos:

- **Nombre del rol:**
    - Descriptivo y único
    - Ejemplo: "Administrador", "Editor", "Colaborador"
- **Permisos:**
    - Lectura, escritura, edición, eliminación, creación, gestión de usuarios, roles, equipos y empresas (por acción)
    - Representado con un número natural dependiendo de cada permiso.

# **8. Gestión de equipos:**

## Funcional:

- **Crear, editar y eliminar equipos:**
    - Permitir la creación de equipos de trabajo para departamentos.
    - Posibilitar la edición de la información del equipo, como nombre, descripción, foto de perfil, miembros, líder del equipo, etc.
    - Ofrecer la opción de eliminar equipos que no sean necesarios, siguiendo un proceso que garantice la seguridad y la integridad del sistema.
- **Añadir y eliminar miembros a los equipos:**
    - Permitir la gestión flexible de los miembros de cada equipo, incluyendo la posibilidad de añadir nuevos miembros, eliminar miembros inactivos o cambiar la pertenencia de un usuario a otro equipo.
    - Controlar el acceso de los usuarios a los proyectos, información y funcionalidades del equipo según su rol y equipo.

## No funcional:

- **Permisos por equipo:** Adaptar el acceso a la información y funcionalidades del sistema a las necesidades de cada equipo.
- **Control de acceso:** Restringir el acceso a la información del equipo a los miembros autorizados.
- **Usabilidad:**
	- **Interfaz intuitiva:** Para la creación, edición y eliminación de equipos.
	- **Gestión flexible de miembros:** Añadir, eliminar y cambiar la membresía de usuarios.
	- **Asignación de roles a miembros:** Permitir la configuración de permisos específicos para cada miembro dentro del equipo.
- **Integración con la gestión de usuarios:** Permitir la asignación de usuarios a equipos.
- **Integración con la gestión de proyectos:** Permitir la asignación de equipos a proyectos.
 
## Datos:

- **Nombre del equipo:**
    - Descriptivo y único
- **Descripción del equipo:**
    - Breve descripción del objetivo y las funciones del equipo
- **Miembros del equipo:**
    - Lista de usuarios que forman parte del equipo
- **Líder del equipo:**
    - Usuario responsable del equipo

# **9. Gestión de empresas:**

## Funcional:

- **Crear, editar y eliminar empresas:**
    - Permitir la creación de diferentes perfiles empresas o entidades dentro del sistema.
    - Posibilitar la edición de la información de la empresa, como nombre, correo electrónico, foto de perfil, descripción, etc.
    - Ofrecer la opción de eliminar perfil de empresa inactivo o que no sea necesario, siguiendo un proceso que garantice la seguridad y la protección de datos.

## No funcional:

**Gestión de empresas:**

- **Control de acceso:** Restringir el acceso a la información de la empresa a los usuarios autorizados.
- **Usabilidad:**
	- **Interfaz intuitiva:** Para la creación, edición y eliminación de empresas.
	- **Gestión flexible de usuarios:** Añadir, eliminar y cambiar la membresía de usuarios en la empresa.
	- **Asignación de roles a usuarios:** Permitir la configuración de permisos específicos para cada usuario dentro de la empresa.
- **Integración con la gestión de usuarios:** Permitir la asignación de usuarios a empresas.
- **Integración con la gestión de proyectos:** Permitir la asignación de empresas a proyectos.

## Datos:

- **Nombre de la empresa:**
    - Descriptivo y único
- **Descripción de la empresa:**
    - Información sobre la actividad, el tamaño y la ubicación de la empresa
- **Usuarios de la empresa:**
    - Lista de usuarios que forman parte de la empresa.
- **Ubicación**.
- **Correo electrónico**.
- **Teléfono**.