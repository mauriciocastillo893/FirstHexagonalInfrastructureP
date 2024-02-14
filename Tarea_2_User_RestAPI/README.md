# Task 2: Flujo de registros de usuario, activación de cuenta y login

**In this task, I am implementing a hexagonal architecture that contains User as an entity, CRUD about it, and a variety of features.**

**More about the task:**


````
Entity: User
Name: String
Last Name: String
Cellphone: String Unique
Email: String Unique
Password: String
Activation Token
Verified At: Date

Registro de usuario  /api/v1/users

Nombre
Apellido
Telefono
Correo Electrónico
Contraseña

Encriptar contraseña

Enviar un correo electrónico al email proporcionado y en el contenido del correo vendrá un link con la ruta  de activación de usuario https://:domain/api/v1/users/:token/activate (método PUT)

Activar la cuenta
Buscar al usuario por el token de activación y actualizar la fecha de verificación

1. REGISTRO DE USUARIOS
2. ENVIO DE CORREO ELECTRONICO
3. ACTIVACIÓN DE CUENTA (BUSCAR UN USUARIO POR  EL TOKEN ASIGNADO ACTUALIZAR FECHA DE VERIFICACIÓN TOMANDO LA FECHA Y HORA ACTUAL QUE SE ESTA ACTIVANDO)

Si la cuenta esta activa y no ha sido eliminada entonces el usuario podrá iniciar sesión.

Logout:  Si el usuario no esta logeado no se podrá cerrar sesión (validación de rutas)

(Implementar JWT)
Implementar al menos 2 repositorios (Mysql Mongo Sqlite).
````

**Made by: Mauricio Castillo**