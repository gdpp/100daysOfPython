En esta sección se tratarán los siguientes temas:

¿Qué es FastAPI y por qué aprenderlo?

- Documentación y enlaces importantes
- Instalación de FastAPI.
- Nuestro primer endpoint (GET)
- Query Params
- Path Params
- Métodos HTTP y status code.
- Endpoint POST
- Endpoint PUT
- Endpoint DELETE
- Documentación automática

# ¿Qué es FastAPI?

FastAPI es un framework web basado en Python 3.7+ que usa tipado estático (type hints) para:

Validar datos automáticamente.
Generar documentación interactiva de la API (con Swagger y Redoc).
Facilitar el desarrollo y el testing de servicios backend modernos.
Internamente, está construido sobre Starlette (para la parte web) y Pydantic (para validación de datos).

# Principales ventajas

## Rápido y eficiente

Está optimizado con ASGI (Asynchronous Server Gateway Interface), lo que permite manejar peticiones concurrentes fácilmente, ideal para microservicios y aplicaciones que necesitan rendimiento.

## Tipado y validación automática

Gracias a Pydantic, puedes declarar tus modelos de datos con tipos (int, str, list, etc.) y FastAPI valida automáticamente las entradas del cliente.

## Documentación automática

Genera una interfaz interactiva de documentación (Swagger UI o ReDoc) sin escribir nada extra. Perfecto para colaborar con frontend o QA.

## Productivo y moderno

Tiene una curva de aprendizaje baja si ya sabes Python. Además, usa async/await, type hints, y patrones actuales de desarrollo backend.

## Excelente integración con herramientas modernas

Funciona muy bien con SQLAlchemy, Pydantic, Alembic, Docker, GraphQL, OAuth2/JWT, y plataformas en la nube como AWS o GCP.

## ¿Por qué aprender FastAPI?

- Es la opción moderna en Python para APIs (más rápido y moderno que Django REST Framework o Flask).
- Se usa en empresas como Netflix, Uber, Microsoft y Explosion.ai.
- Ideal si quieres crear microservicios, APIs REST, backends para React/Vue, o integraciones con IA (OpenAI, HuggingFace, etc.).
- Es perfecto para entrevistas o portafolios backend: demuestra conocimiento moderno, buenas prácticas y eficiencia.
