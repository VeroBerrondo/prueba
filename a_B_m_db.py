import sqlite3
def cargar_peliculas_db():
    with sqlite3.connect('peliculas.db')as conn:
     cursor = conn.cursor()
     cursor.execute ('CREATE TABLE IF NOT EXISTS peliculas(id INTEGER,titulo TEXT,genero TEXT,duracion INTEGER,sinopsis TEXT,pais_de_origen TEXT,idioma TEXT,calificacion INTEGER,disponible INTEGER,clasificacion TEXT)')
     conn.commit()
    cursor.execute('SELECT*FROM peliculas')
    nombres_columnas=[descripcion[0]for descripcion in cursor.description]
    rows=cursor.fetchall()
    peliculas_resultado=[dict(zip(nombres_columnas,fila))for fila in rows]
    
    return conn, cursor, peliculas_resultado
genero=["Accion","Animacion","Comedia","Drama","Ciencia ficcion","Terror","Suspenso","Romantica"]
clasificacion=["ATP","PG","PG-13","R","NC-17"]
calificacion=[]
peliculas=[]
peliculas = cargar_peliculas_db()
def alta_de_nueva_pelicula():
      conn,cursor,peliculas=cargar_peliculas_db()
      continuar=1
      while continuar==1:
        
            print("#"*50)
            print(f"# Alta de Nueva Pelicula #")
            print("#"*50)
            nuevo_id=int(input("Ingrese el Id: ")) 
            if any(pelicula['id']==nuevo_id for pelicula in peliculas):
               print("El ID ya existe, por favor ingrese un ID unico.")
               continue
            nuevo_titulo=input("Ingrese el Titulo: ").capitalize()
            if any(pelicula['titulo']==nuevo_titulo for pelicula in peliculas):
               print("El titulo ya existe.")
               continue
            while True:
              nuevo_genero=input("Ingrese el Genero: ").capitalize()
              if nuevo_genero in genero:
               break
              else:
               print("ingresa un genero valido")
              nueva_duracion=""
            while True:  
              try:
                nueva_duracion=int(input("Ingrese la Duracion en minutos: "))
                break
              except ValueError:
               print("Ingrese un numero entero")
            nueva_sinopsis=""
            while not nueva_sinopsis:
               nueva_sinopsis=input("Ingrese la Sinopsis: ")
            nuevo_pais_de_origen="" 
            while not nuevo_pais_de_origen:
               nuevo_pais_de_origen=input("Ingrese el Pais de Origen: ")
            nuevo_idioma=""
            while not nuevo_idioma:
               nuevo_idioma=input("Ingrese el Idioma Original: ")
            nuevo_disponible=""
            while True:
               nuevo_disponible=input("Esta disponible para el streaming S/N: ").strip().lower()
               if nuevo_disponible in ["s","n"]:
                break
            
            while True:
               nueva_clasificacion=input("Ingresa la Clasificacion: ").upper()
               if nueva_clasificacion in clasificacion:
                 break
               else:
                print("Ingresa una clasificacion valida")
           
            pelicula={'id':nuevo_id,
                      'titulo':nuevo_titulo,
                      'genero':nuevo_genero,
                      'duracion':nueva_duracion,
                      'sinopsis':nueva_sinopsis,
                      'pais_de_origen':nuevo_pais_de_origen,
                      'idioma':nuevo_idioma,
                      'calificacion':None,
                      'disponible':1 if nuevo_disponible=="s" else 0,
                      'clasificacion':nueva_clasificacion}
            print("Nueva Pelicula agregada con exito")
            peliculas.append(pelicula)
            
            cursor.execute("INSERT INTO peliculas(id,titulo,genero,duracion,sinopsis,pais_de_origen,idioma,calificacion,disponible,clasificacion)VALUES(?,?,?,?,?,?,?,?,?,?)", 
               (pelicula['id'],
                pelicula['titulo'],
                pelicula['genero'],
                pelicula['duracion'],
                pelicula['sinopsis'],
                pelicula['pais_de_origen'],
                pelicula['idioma'],
                pelicula['calificacion'],
                pelicula['disponible'],
                pelicula['clasificacion']))
            conn.commit()
            continuar=int(input("Si desea agregar otro titulo ingrese 1 si desea salir ingrese 0 : "))
            if continuar==0:
               continuar=False
               break
            conn.close()
            

def modificar_pelicula_por_id():
            conn,cursor,peliculas=cargar_peliculas_db()
            id_buscar=int(input("Ingrese el ID de la Pelicula que desea modificar:"))
            for pelicula in  peliculas:
             if   id_buscar==pelicula['id']:
                  nuevo_id=int(input(f"<<{pelicula['id']}>> Ingresa nuevo ID (Ingresa 0 para no modificar): "))
                  nuevo_titulo=input(f"<<{pelicula['titulo']}>> Ingresa nuevo Titulo (Ingresa 0 para no modificar): ")
                  nuevo_genero=input(f"<<{pelicula['genero']}>> Ingresa nuevo Genero (Ingresa 0 para no modificar): ").capitalize()
                  nueva_duracion=int(input(f"<<{pelicula['duracion']}>> Ingresa nueva Duracion (Ingresa 0 para no modificar: )"))
                  nueva_sinopsis=input(f"<<{pelicula['sinopsis']}>> Ingresa nueva Sinopsis (Ingresa 0 para no modificar): ")
                  nuevo_pais_de_origen=input(f"<<{pelicula['pais_de_origen']}>> Ingresa nuevo Pais de Origen (Ingresa 0 para no modificar:) ")
                  nuevo_idioma=input(f"<<{pelicula['idioma']}>> Ingresa nuevo Idioma(Ingresa 0 para no modificar:) ")
                  nuevo_disponible=input(f"<<{pelicula['disponible']}>> Esta Disponible para el streaming S/N: ").lower()
                  nueva_clasificacion=input(f"<<{pelicula['clasificacion']}>> Ingresa nueva Clasificacion (Ingresa 0 para no modificar): ")
                  if nuevo_disponible=="s":
                     pelicula["disponible"]=nuevo_disponible =1
                  if nuevo_disponible=="n":
                     pelicula["disponible"]=nuevo_disponible= 0
                  if nueva_sinopsis!="0":
                     pelicula["sinopsis"]=nueva_sinopsis
                  if nueva_duracion !=0:
                     pelicula["duracion"]= nueva_duracion
                  if nuevo_pais_de_origen!="0":
                     pelicula["pais de origen"]=nuevo_pais_de_origen
                  if nuevo_idioma!="0":
                     pelicula["idioma"]=nuevo_idioma
                  if nuevo_titulo!= "0":
                     pelicula["titulo"]=nuevo_titulo
                  if nuevo_genero != "0":  
                       pelicula["genero"]=nuevo_genero
                  
                  if nueva_clasificacion!="0":
                        pelicula["clasificacion"] =nueva_clasificacion 
                      
                  if nuevo_id!=0:
                     pelicula["id"]=nuevo_id
                  print("Pelicula modificada con exito.")
                  cursor.execute("UPDATE peliculas SET id=?, titulo=?, genero=?, duracion=?, sinopsis=?, pais_de_origen=?, idioma=?, calificacion=?, disponible=?, clasificacion=? WHERE id=?",
                   (pelicula['id'], 
                    pelicula['titulo'], 
                    pelicula['genero'], 
                    pelicula['duracion'], 
                    pelicula['sinopsis'],
                    pelicula['pais_de_origen'], 
                    pelicula['idioma'], 
                    pelicula['calificacion'], 
                    pelicula['disponible'], 
                    pelicula['clasificacion'],
                    id_buscar))
                  conn.commit()
            
            conn.close()
            return
        
                
              
def modificar_pelicula_por_titulo():
            conn,cursor,peliculas=cargar_peliculas_db()
            titulo_A_buscar=input("Ingrese el Titulo de la Pelicula que desea modificar:")
            for pelicula in peliculas:
                if titulo_A_buscar.capitalize()==pelicula['titulo']:
                   nuevo_id=int(input(f"<<{pelicula['id']}>> Ingresa nuevo ID (Ingresa 0 para no modificar):"))
                   nuevo_titulo=input(f"<<{pelicula['titulo']}>> Ingresa nuevo Titulo (Ingresa 0 para no modificar): ")
                   nuevo_genero=input(f"<<{pelicula['genero']}>> Ingresa nuevo Genero (Ingresa 0 para no modificar): ").capitalize()
                   nueva_duracion=int(input(f"<<{pelicula['duracion']}>> Ingresa nueva Duracion (Ingresa 0 para no modificar: )"))
                   nueva_sinopsis=input(f"<<{pelicula['sinopsis']}>> Ingresa nueva Sinopsis (Ingresa 0 para no modificar): ")
                   nuevo_pais_de_origen=input(f"<<{pelicula['pais_de_origen']}>> Ingresa nuevo Pais de Origen (Ingresa 0 para no modificar:) ")
                   nuevo_idioma=input(f"<<{pelicula['idioma']}>> Ingresa nuevo Idioma(Ingresa 0 para no modificar:) ")
                   nuevo_disponible=input(f"<<{pelicula['disponible']}>> Esta Disponible para el streaming S/N: ").lower()
                   nueva_clasificacion=input(f"<<{pelicula['clasificacion']}>> Ingresa nueva Clasificacion (Ingresa 0 para no modificar): ").upper()
                   if nuevo_disponible=="s":
                     pelicula["disponible"]=nuevo_disponible =1
                   if nuevo_disponible=="n":
                     pelicula["disponible"]=nuevo_disponible= 0
                   if nueva_sinopsis!="0":
                     pelicula["sinopsis"]=nueva_sinopsis
                   if nueva_duracion !=0:
                     pelicula["duracion"]= nueva_duracion
                   if nuevo_pais_de_origen!="0":
                     pelicula["pais de origen"]=nuevo_pais_de_origen
                   if nuevo_idioma!="0":
                     pelicula["idioma"]=nuevo_idioma
                   if nuevo_titulo!= "0":
                     pelicula["titulo"]=nuevo_titulo
                   if nuevo_genero != "0":  
                       pelicula["genero"]=nuevo_genero
                  
                   if nueva_clasificacion!="0":
                        pelicula["clasificacion"] =nueva_clasificacion 
                      
                   if nuevo_id!=0:
                     pelicula["id"]=nuevo_id
                   print("Pelicula modificada con exito.")
                   cursor.execute("UPDATE peliculas SET id=?, titulo=?, genero=?, duracion=?, sinopsis=?, pais_de_origen=?, idioma=?, calificacion=?, disponible=?, clasificacion=? WHERE titulo=?",
                   (pelicula['id'], 
                    pelicula['titulo'], 
                    pelicula['genero'], 
                    pelicula['duracion'], 
                    pelicula['sinopsis'],
                    pelicula['pais_de_origen'], 
                    pelicula['idioma'], 
                    pelicula['calificacion'], 
                    pelicula['disponible'], 
                    pelicula['clasificacion'],
                    titulo_A_buscar.capitalize()))
                   conn.commit()
            
            conn.close() 
            return
            
              

def eliminar_pelicula_por_titulo():
            conn,cursor,peliculas=cargar_peliculas_db()
            
            titulo_a_eliminar = input("Ingrese el título de la película que desea eliminar:")
            pelicula_encontrada= False
            for pelicula in peliculas:
              if titulo_a_eliminar.capitalize() == pelicula['titulo'].capitalize():
                 pelicula_encontrada=True
                 break
            if pelicula_encontrada:
                 peliculas.remove(pelicula)# Removemos la película de la lista
                 print(f"Película: '{titulo_a_eliminar}' eliminada con exito.")
                 
                 cursor.execute("DELETE FROM peliculas WHERE titulo=?", (titulo_a_eliminar,))
                 conn.commit()
    
            else:
                 print(f"No se encontro La Pelicula: '{titulo_a_eliminar}")  
            
            conn.close()
            return
             
            
            
            