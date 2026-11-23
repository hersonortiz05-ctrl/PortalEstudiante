# Mapa de navegación y rutas

```mermaid
flowchart TD
 L[Login /login/] --> R{Rol}
 R -->|Administrador| D[Dashboard /]
 R -->|Estudiante| E[Dashboard /]
 D --> C[Gestión de carreras, períodos y cursos]
 D --> G[Gestión de estudiantes, matrículas, notas y avisos]
 E --> P[Perfil /perfil/ y contacto]
 E --> M[Materias /materias/]
 M --> MD[Detalle /materias/pk/]
 E --> N[Calificaciones /calificaciones/]
 E --> A[Avisos /avisos/ y detalle]
 D --> S[Logout POST /logout/]
 E --> S
```

En 1a funcionan /login/, /logout/, / y /gestion/carreras/, /gestion/periodos/, /gestion/cursos/, con crear/, <pk>/editar/ y <pk>/eliminar/. /admin/ conserva Django Admin para los modelos. Las demás rutas pertenecen a los paquetes siguientes y no deben enlazarse hasta existir.

Nombres definitivos de consulta: dashboard, perfil, perfil_editar, mis_materias, materia_detalle, mis_calificaciones, avisos_lista, aviso_detalle. El pk del detalle de materia es de Matricula, no de Curso. Gestión: <entidad>_lista/crear/editar/eliminar.
