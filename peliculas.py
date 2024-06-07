import sqlite3
import json
with open('peliculas.json','r')as archivo:
 peliculas_json=json.load(archivo)
print (peliculas_json)
conn= sqlite3.connect('peliculas.db')
cursor=conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS peliculas(
               id INTEGER PRIMARY KEY,
               titulo TEXT,
               genero TEXT CHECK(genero IN("Accion","Animacion","Comedia","Drama","Ciencia ficcion","Terror","Suspenso","Romantica")),
               duracion INTEGER,
               sinopsis TEXT,
               pais_de_origen TEXT,
               idioma TEXT,
               calificacion INTEGER --Usar INTEGER para almacenar cada calificacion,
               disponible BOOLEAN,
               clasificacion TEXT CHECK(clasificacion IN("ATP","PG","PG-13","R","NC-17")))''')
conn.commit()

for pelicula in peliculas_json:
   for calificacion in pelicula.get('calificacion',[]):
    print()
cursor.execute('''
                 INSERT INTO 
                 peliculas(id,titulo,genero,duracion,sinopsis,pais_de_origen,idioma,calificacion,disponible,clasificacion)
                 VALUES(?,?,?,?,?,?,?,?,?,?)
                 ''',
                 (pelicula['id'],
                  pelicula['titulo'],
                  pelicula['genero']if pelicula['genero']in ("Accion","Animacion","Comedia","Drama","Ciencia ficcion","Terror","Suspenso","Romantica")
                  else None,
                  pelicula['duracion'],
                  pelicula['sinopsis'],
                  pelicula['pais_de_origen'],
                  pelicula['idioma'],
                  calificacion,
                  pelicula['disponible'],
                  pelicula['clasificacion']
                  if pelicula['clasificacion']in 
                  ("ATP","PG","PG-13","R","NC-17")
                  else None))
conn.commit()
conn.close()
