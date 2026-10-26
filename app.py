from flask import Flask, render_template, request


app = Flask(__name__)




# P�gina de inicio
@app.route("/")
def inicio():
    titulo = "Mundo del Terror"
    mensaje = "Bienvenido al lugar donde comienzan tus peores pesadillas."


    return render_template(
        "index.html",
        titulo=titulo,
        mensaje=mensaje
    )




# P�gina de pel�culas
@app.route("/peliculas")
def peliculas():

    lista_peliculas = [
        {
            "nombre": "El conjuro",
            "anio": 2013,
            "resumen": "Una familia experimenta sucesos paranormales en su casa.",
            "director": "James Wan",
            "portada": "https://tumbaabierta.com/wp-content/uploads/2013/04/tumbaabierta_the_CONJURING_cartel_internacional-696x1031.jpg"
        },
        {
            "nombre": "It",
            "anio": 2017,
            "resumen": "Un grupo de amigos se enfrenta a una entidad aterradora.",
            "director": "Andy Muschietti",
            "portada": "https://lamorgueblog.wordpress.com/wp-content/uploads/2017/09/it-eso-poster.jpg?w=816"
        },
        {
            "nombre": "Halloween",
            "anio": 1978,
            "resumen": "Un asesino enmascarado regresa durante Halloween.",
            "director": "John Carpenter",
            "portada": "https://www.originalfilmart.com/cdn/shop/products/Halloween_6_Curse_of_Michael_Myers_1995_original_film_art_5000x.jpg?v=1562543391"
        },
        {
            "nombre": "El exorcista",
            "anio": 1973,
            "resumen": "Una niña presenta comportamientos inexplicables.",
            "director": "William Friedkin",
            "portada": "https://static.wikia.nocookie.net/cine/images/1/1a/The_exorcist.jpg/revision/latest?cb=20121027192450"
        },
        {
            "nombre": "Pesadilla en la calle Elm",
            "anio": 1984,
            "resumen": "Un grupo de jóvenes es perseguido en sus sueños.",
            "director": "Wes Craven",
            "portada": "https://es.web.img3.acsta.net/c_310_420/medias/nmedia/18/78/84/45/20235469.jpg"
        },
        {
            "nombre": "La noche de los muertos vivientes",
            "anio": 1968,
            "resumen": "Un grupo intenta sobrevivir a una invasión de muertos vivientes.",
            "director": "George A. Romero",
            "portada": "https://static.wikia.nocookie.net/doblaje/images/3/35/Night_of_the_Living_Dead_%281968%29.png/revision/latest?cb=20180713083516&path-prefix=es"
        }
    ]

    busqueda = request.args.get("busqueda", "").strip()
    peliculas_filtradas = lista_peliculas

    if busqueda:
        consulta = busqueda.casefold()
        peliculas_filtradas = [
            pelicula for pelicula in lista_peliculas
            if consulta in pelicula["nombre"].casefold()
            or consulta in str(pelicula["anio"])
            or consulta in pelicula["director"].casefold()
        ]

    return render_template(
            "peliculas.html",
            peliculas=peliculas_filtradas,
            busqueda=busqueda
        )




# P�gina sobre nosotros
@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")




if __name__ == "__main__":
    app.run(debug=True)
