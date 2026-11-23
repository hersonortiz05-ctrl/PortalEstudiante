# Etiquetas Django sin programar Python

- `{% extends 'base.html' %}` reutiliza la estructura de la página.
- `{% block content %}...{% endblock %}` coloca el contenido en un espacio de la base. También hay title, extra_css y extra_js.
- `{% load static roles %}` habilita rutas de estáticos y los filtros de roles que programó Antonid.
- `{% static 'css/styles.css' %}` obtiene la URL del CSS.
- `{% url 'dashboard' %}` obtiene una ruta por su nombre. No adivinar nombres nuevos.
- `{{ nombre_usuario }}` muestra un valor que el servidor entrega; Django escapa HTML peligroso.
- `{% if es_admin %}...{% else %}...{% endif %}` muestra contenido según una condición.
- `{% for campo in form %}...{% endfor %}` recorre campos. Lo mismo se usa para matrículas y mensajes.
- `{% empty %}` dentro de un for presenta el estado sin resultados.
- `{% csrf_token %}` es obligatorio dentro de formularios POST; protege la solicitud. No borrarlo ni reemplazarlo por una contraseña.
- `user|es_administrador` pregunta al filtro de Antonid si el usuario es administrador. Ocultar un botón no sustituye los permisos del servidor.
- `{{ campo.label_tag }}`, `{{ campo }}` y `{{ campo.errors }}` muestran etiqueta accesible, control y errores sin escribir Python.

No usar safe para contenido de usuarios, no escribir consultas en HTML y no tocar models.py. Se incluyen csrf_token y empty porque son etiquetas simples necesarias para seguridad y estados vacíos; no se pide a Paola escribir lógica Python.
