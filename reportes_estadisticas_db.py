import sqlite3
import random
import os
def cargar_peliculas_db():
    conn = sqlite3.connect('peliculas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT* FROM peliculas")
    rows=cursor.fetchall()
    conn.close()
    columnas=[desc[0]for desc in cursor.description]
    peliculas=[dict(zip(columnas,row))for row in rows]
    return peliculas


peliculas = cargar_peliculas_db()
calificacion=[]
def listado_de_peliculas_alfabetico(peliculas):
          print("#"*50)
          print("")
          print("Listado de Peliculas: Titulo, Genero, Sinopsis y Calificacion.")
          print("") 
          print("#"*50)
          peliculas=  cargar_peliculas_db()
          peliculas_ordenadas=sorted(peliculas,key=lambda x:x['titulo'])#ordenar peliculas por titulo en orden alfabetico
          for peliculas in peliculas_ordenadas:#mostrar peliculas ordenadas
           titulo=peliculas['titulo']
           genero=peliculas['genero']
           sinopsis=peliculas['sinopsis']
           calificacion=peliculas['calificacion']
           
           print("-"*50)
           print(f"Titulo: {titulo}")
           print("")
           print(f"Genero:{genero}")
           print("")
           print(f"Sinopsis:{sinopsis}")
           print("")
           print(f"Calificacion:{calificacion}")
           print("-"*50)
           input("Presiona una tecla para continuar:")
           print("-"*50)
           os.system("cls")

def mostrar_mejor_calificadas():
         print("#"*50)
         print("")
         print("Peliculas de Mayor Puntaje")
         print("") 
         print("#"*50)
        
       
         with sqlite3.connect('peliculas.db') as conn:
           cursor = conn.cursor()
         cursor.execute('SELECT * FROM peliculas WHERE calificacion IS NOT NULL ORDER BY calificacion DESC LIMIT 10')
         nombres_columnas = [descripcion[0] for descripcion in cursor.description]
         rows = cursor.fetchall()
         peliculas_mejor_calificadas = [dict(zip(nombres_columnas, fila)) for fila in rows]
         print("#" * 50)
         print("Top 10 Películas Mejor Calificadas")
         print("#" * 50)
         for idx, pelicula in enumerate(peliculas_mejor_calificadas, 1):
            print("#" * 50)
            print(f"{idx}. Título: {pelicula['titulo']}")
            print("")
            print(f"Calificación: {pelicula['calificacion']}")
            print("#" * 50)
            input("presiona una tecla para continuar:")
            os.system("cls")

def peliculas_en_streaming(peliculas):
         print("#"*50)
         print("")
         print("Peliculas Disponibles en la Plataforma") 
         print("")
         print("#"*50)
         peliculas=cargar_peliculas_db()
         peliculas_disponibles=sorted(peliculas,key=lambda x:x['disponible'])
         for pelicula in peliculas_disponibles:
           titulo=pelicula['titulo']
           disponible=pelicula['disponible']
           if disponible==1:
                disponible=True
           else:
                disponible=False
           
           print("")
           print(f"Titulo: {titulo} ")
           print("")
           print(f"Disponible: {disponible}")
           print("-"*50)
           input("Presiona una tecla para continuar:")
           os.system("cls")


def calificar_peliculas_al_azar():
              with sqlite3.connect('peliculas.db')as conn:
               cursor = conn.cursor()
              cursor.execute("SELECT* FROM peliculas")
              columnas=[desc[0]for desc in cursor.description]
              rows=cursor.fetchall()
              peliculas=[dict(zip(columnas,fila))for fila in rows]
              random.shuffle(peliculas)
              peliculas_al_azar=peliculas[:10]
              for pelicula in peliculas_al_azar:
                print("#" * 50)
                print(f"Título: {pelicula['titulo']},Calificación: {pelicula['calificacion']if pelicula['calificacion'] is not None else 'No calificada'}")
                
                try:
                  nueva_calificacion = int(input(f"Ingrese la calificación para '{pelicula['titulo']}': "))
                  print("#" * 50)
                  input("Presiona una tecla para continuar:")
                  os.system("cls")

                except ValueError:
                 print("Ingrese un número entero como calificación.")
                continue
              pelicula['calificacion']=nueva_calificacion
              for pelicula in peliculas_al_azar:
               cursor.execute("UPDATE peliculas SET calificacion=? WHERE id=?", (nueva_calificacion, pelicula['id']))
               conn.commit()
              conn.close()
              return
          