/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Rutas a las plantillas HTML dentro de la carpeta de templates
    './blog_django/templates/**/*.html',  // Modifica según la ruta completa si es necesario
    
    // Rutas a los archivos CSS dentro de la carpeta de static
    './blog_django/static/**/*.css',      // Asegúrate de que esta ruta sea correcta
    
    // Rutas a los archivos JS dentro de la carpeta de static
    './blog_django/static/**/*.js',       // Incluye esta ruta si estás usando scripts JS
  ],
  theme: {
    extend: {
      colors: {
        micolor: "#3ff",  // Color personalizado
      },
    },
  },
  plugins: [],
}
