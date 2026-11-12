# Gestión del conocimiento · Fitmesh

Repositorio privado de la **etapa 2** de la estrategia de Gestión del Conocimiento del proyecto *Sistema Escalable de Asignación de Rutinas Multidisciplinarias* (Ingeniería de Software II). La estrategia completa está en Confluence, espacio GDP, página *Gestión del Conocimiento*.

## Estructura

| Carpeta | Contenido |
| --- | --- |
| `decisiones/` | Registros D-nnn: qué se decidió, alternativas y motivo |
| `errores/` | Registros E-nnn: síntoma, causa raíz, solución y prevención |
| `lecciones/` | Registros L-nnn: qué pasó, qué aprendimos y qué recomendamos |
| `reuniones/` | Registros R-nnn: resumen, acuerdos y próximos pasos |
| `guias/` | Guías técnicas reutilizables |
| `plantillas/` | Una plantilla por tipo de registro |
| `scripts/` | Validación de los registros |

## Cómo se agrega un registro

1. Una persona pasa la transcripción, el ticket o el pull request a un asistente de IA con la instrucción de la sección 9 de la estrategia.
2. El asistente devuelve borradores con la plantilla que corresponde. Se suben en una rama `registro/<id>` y se abre un pull request.
3. Una persona **distinta del autor** revisa: corrige nombres y términos, comprueba que no haya datos inventados y asigna la confidencialidad.
4. El chequeo automático (`scripts/validar_registros.py`) verifica los campos obligatorios y que no haya registros de nivel `rojo`.
5. Con la aprobación del revisor se fusiona. Desde ese momento el registro es vigente.

## Reglas

- Nada se borra: lo que deja de valer pasa a `obsoleto` y se enlaza al registro que lo reemplaza.
- Un registro de confidencialidad `rojo` (credenciales, datos personales, acuerdos confidenciales) **no se sube nunca** a este repositorio.
- Todo se escribe en español (D-006).
- Si no hay un registro sobre un tema, la consulta debe responder «no consta».
- El agente de IA solo puede crear ramas y pull requests; nunca aprueba ni fusiona.
