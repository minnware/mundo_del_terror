## Prompt 1: 
holaaaa

## Prompt 2: 
Quiero crear una aplicación web con una estructura sencilla con Python y Flask. La aplicación será sobre películas de terror. Necesito las siguientes carpetas y archivos: un archivo app.py, una carpeta templates, una carpeta static, una carpeta static/css y un archivo styles.css

## Prompt 3: 
La página debe tener tres rutas principales: / para crear la página de inicio, una ruta para el archivo de películas y /nosotros para mostrar información acerca del proyecto. Cada una debe ocupar @app.route y render_template( ). Que este sea el código para el archivo app.py sin usar bases de datos o funciones más avanzadas.

## Prompt 4: 
Crea los archivos HTML necesarios para las rutas de mi aplicación Flask.
Necesito: index.html, películas.html y nosotros.html
Cada página debe incluir: un título, una barra de investigación, enlaces que permitan desplazarse entre las páginas y contenidos relacionados con las películas de terror.
Mantén el HTML sencillo y ordenado, no agregues JavaScript.

## Prompt 5:
Quiero que modifique mi aplicación Flask para poder enviar datos desde Python hacia los archivos HTML utilizando render_template() .
En la página de inicio quiero enviar: un título; un mensaje de bienvenida.
En la página de películas quiero enviar una lista de al menos 6 películas de terror.
Cada elemento de la lista debe contener estos 4 datos: nombre, año,breve resumen y el director.
Muéstrame cómo modificar app.py para enviar estos datos.
Luego muéstrame cómo recibirlos y mostrarlos en el HTML utilizando Jinja.

## Prompt 6:
Necesito mostrar en mi HTML los datos enviados desde Flask.
Utiliza Jinja para: mostrar variables utilizando {{ }},
Mantén el código simple.

## Prompt 7:
Necesito mostrar en mi HTML los datos enviados desde Flask.
Utiliza Jinja para: mostrar variables utilizando {{ }}, recorrer una lista utilizando un ciclo for y mostrar los diferentes datos de cada elemento.
Mantén el código simple.

## Prompt 8:
Quiero agregarle estilos css a mi aplicación Flask, para eso utiliza el archivo static/css/styles.css.

## Prompt 9:
Quiero agregarle estilos css a mi aplicación Flask, para eso, utiliza el archivo static/css/styles.css . utiliza una tipografía de terror, los colores que transmitan miedo pero que tengan armonía entre sí, una barra de navegación ordenada, márgenes y espacios, contenedor principal y que cada película primero aparezca su portada junto a su título y que se tenga que apretar para que salgan los datos restantes

## Prompt 10:
pero dame el codigo

## Prompt 11:
explica detallada mente como realizar el paso 3

## Prompt 12:
lista_peliculas = [
        {
            "nombre": "El Conjuro",
            "anio": 2013,
            "resumen": "Una familia experimenta sucesos paranormales en su casa.",
            "director": "James Wan",
            "portada": "/static/img/conjuro.jpg"
        },
        {
            "nombre": "It",
            "anio": 2017,
            "resumen": "Un grupo de amigos se enfrenta a una entidad aterradora.",
            "director": "Andy Muschietti",
        },
        {
            "nombre": "Halloween",
            "anio": 1978,
            "resumen": "Un asesino enmascarado regresa durante la noche de Halloween.",
            "director": "John Carpenter"
        },
        {
            "nombre": "El Exorcista",
            "anio": 1973,
            "resumen": "Una niña presenta comportamientos inexplicables y su familia busca ayuda.",
            "director": "William Friedkin"
            },
        {
            "nombre": "Pesadilla en la calle Elm",
            "anio": 1984,
            "resumen": "Un grupo de jóvenes es perseguido en sus sueños por una presencia siniestra.",
            "director": "Wes Craven"
        },
        {
            "nombre": "La noche de los muertos vivientes",
            "anio": 1968,
            "resumen": "Un grupo de personas intenta sobrevivir a una invasión de muertos vivientes.",
            "director": "George A. Romero"
        }   quiero que las imagenes las obtengas desde internet

## Prompt 13:
lista_peliculas = [
        {
            "nombre": "El Conjuro",
            "anio": 2013,
            "resumen": "Una familia experimenta sucesos paranormales en su casa.",
            "director": "James Wan",
            "portada": "/static/img/conjuro.jpg"
        },
        {
            "nombre": "It",
            "anio": 2017,
            "resumen": "Un grupo de amigos se enfrenta a una entidad aterradora.",
            "director": "Andy Muschietti",
        },
        {
            "nombre": "Halloween",
            "anio": 1978,
            "resumen": "Un asesino enmascarado regresa durante la noche de Halloween.",
            "director": "John Carpenter"
        },
        {
            "nombre": "El Exorcista",
            "anio": 1973,
            "resumen": "Una niña presenta comportamientos inexplicables y su familia busca ayuda.",
            "director": "William Friedkin"
            },
        {
            "nombre": "Pesadilla en la calle Elm",
            "anio": 1984,
            "resumen": "Un grupo de jóvenes es perseguido en sus sueños por una presencia siniestra.",
            "director": "Wes Craven"
        },
        {
            "nombre": "La noche de los muertos vivientes",
            "anio": 1968,
            "resumen": "Un grupo de personas intenta sobrevivir a una invasión de muertos vivientes.",
            "director": "George A. Romero"
         }   quiero que las imagenes de las portadas de cada pelicula las obtengas desde internet

## Prompt 14:
No funciona la barra de navegación, cómo lo arreglo?

## Prompt 15:
Haz que se pueda buscar una pelicula

## Prompt 16:
tengo una barra de navegacion en peliculas.html pero no funciona, corrigela

## Prompt 17:
La barra de peliculas no me deja buscar la pelicula que quiero

## Prompt 18:
modifica para que todos los titulos tengan buena ortografía

## Prompt 19:
Haz que el inicio sea más atractivo visualmente

## Prompt 20:
Haz que el inicio sea más atractivo visualmente