# API de Gestión de Películas

Este repositorio contiene el código para una API de gestión de películas desarrollada en Python utilizando FastAPI y MongoDB.

## Descripción del Proyecto

La API de gestión de películas permite a los usuarios realizar diversas operaciones relacionadas con las películas, como agregar nuevas películas, buscar películas por diferentes criterios, actualizar la información de las películas y eliminar películas de la base de datos. Utiliza una base de datos MongoDB para almacenar la información de las películas.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- `main.py`: Contiene el código principal de la aplicación FastAPI.
- `film.py`: Define la configuración de la clase Film.
- `client.py`: Define la conexión con la base de datos MongoDB.
- `bdConfig.py`: Contiene funciones de gestión de la base de datos.

## Funcionalidades Implementadas

### CRUD de Películas

- **Obtener Todas las Películas**
  - **Ruta:** `/films/`
  - **Método:** GET
  - **Descripción:** Retorna un objeto JSON que contiene todas las películas almacenadas en la base de datos.
  - **Respuesta Exitosa:** `{ "status": 1, "data": [ { "id": "str", "title": "str", "director": "str", "year": int, "genre": "str", "rating": number, "country": "str" }, ... ] }`
  - **Respuesta con Error:** `{ "status": -1, "message": "mensaje de error" }`

- **Obtener Película por ID**
  - **Ruta:** `/film/{id}`
  - **Método:** GET
  - **Descripción:** Retorna un objeto JSON que contiene la información de la película cuyo ID coincide con el parámetro proporcionado.
  - **Respuesta Exitosa:** `{ "status": 1, "data": { "id": "str", "title": "str", "director": "str", "year": int, "genre": "str", "rating": number, "country": "str" } }`
  - **Respuesta con Error:** `{ "status": -1, "message": "mensaje de error" }`

- **Agregar Nueva Película**
  - **Ruta:** `/film/`
  - **Método:** POST
  - **Descripción:** Permite agregar una nueva película a la base de datos.
  - **Respuesta Exitosa:** `{ "status": 1, "data": { "id": "str", "title": "str", "director": "str", "year": int, "genre": "str", "rating": number, "country": "str" } }`
  - **Respuesta con Error:** `{ "status": -1, "message": "mensaje de error" }`

- **Actualizar Película por ID**
  - **Ruta:** `/film/{id}`
  - **Método:** PUT
  - **Descripción:** Permite modificar la información de una película existente en la base de datos.
  - **Respuesta Exitosa:** `{ "status": 1, "message": "El film se ha actualizado correctamente" }`
  - **Respuesta con Error:** `{ "status": -1, "message": "mensaje de error" }`

- **Eliminar Película por ID**
  - **Ruta:** `/film/{id}`
  - **Método:** DELETE
  - **Descripción:** Permite eliminar una película de la base de datos.
  - **Respuesta Exitosa:** `{ "status": 1, "message": "El film se ha eliminado correctamente" }`
  - **Respuesta con Error:** `{ "status": -1, "message": "mensaje de error" }`

### Consultas Avanzadas

- **Buscar Películas por Género**
  - **Ruta:** `/films/?genre={genre}`
  - **Método:** GET
  - **Descripción:** Retorna una lista de películas según el género especificado.
  - **Ejemplo:** `/films/?genre=Comedy`

- **Ordenar Películas por Campo y Orden**
  - **Ruta:** `/films/?field={field}&order={order}`
  - **Método:** GET
  - **Descripción:** Retorna una lista de películas ordenadas según el campo y el orden especificados.
  - **Ejemplo:** `/films/?field=title&order=asc`

- **Limitar el Número de Películas**
  - **Ruta:** `/films/?limit={limit}`
  - **Método:** GET
  - **Descripción:** Retorna una lista de películas con un límite específico de registros.
  - **Ejemplo:** `/films/?limit=10`

Para obtener más información sobre los parámetros de consulta, consulta la [documentación de FastAPI](https://fastapi.tiangolo.com/tutorial/query-params/).
