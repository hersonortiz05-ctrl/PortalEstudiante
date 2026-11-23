# Guía de estilos · Sprint 1a

Único archivo compartido de estilos: static/css/styles.css. No se necesitan librerías ni fuentes remotas. Verde #096b60, tinta #203b35, fondo #f5f7f4. Tipografía del sistema. Espaciado base 24 px y radio 14 px.

Clases: .container centra el contenido; .navbar usa Flexbox; .grid y .grid--two usan Grid; .card contiene información; .btn y .btn--primary son botones; .table y .table-container permiten scroll interno; .form-group organiza campos; .badge es una etiqueta; .message muestra mensajes. Variantes: message--success, message--error, message--warning y message--info. Foco visible y controles de mínimo 44 px.

Abrir /login/ y / con las cuentas demo; probar anchos 360, 768 y 1366 px. Registrar resultados reales, no marcar aprobado sin observar. El header se adapta por filas sin JS. Las tablas se desplazan dentro del contenedor, no toda la página.

Solo se enlazan rutas ya implementadas en 1a. Perfil, notas, avisos y detalle tendrán enlaces cuando existan en los paquetes siguientes. No añadir enlaces rotos como adelanto.

La presentación de CRUD en 1a usa plantillas básicas de Amaris dentro de la app. En 1b, Paola crea templates/gestion/* y Django prioriza esas plantillas, sin editar los archivos de Amaris.
