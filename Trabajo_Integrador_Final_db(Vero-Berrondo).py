import os
import a_B_m_db
import reportes_estadisticas_db

peliculas =[]
def cinema():
 print("#"*50)
 print("#")
 print("#  CINEMA+ # "*3)
 print("#")
 print("#"*50)
while True:
  cinema()
  print("#"*50) 
  print("          MENU INICIO      ")
  print("#"*50)
  print("#"*50)
  print     (f"""
        #  1- A.B.M De Peliculas.
        #  2- Calificacion de Titulos.
        #  3- Reportes y Estadisticas.
        #  0- Salir.
           """)
  print("#"*50)
  opcion=int(input("Ingresa una opcion: "))
  os.system("cls")
  if opcion==1:
   opcion_abm=True
   while opcion_abm==True:
      cinema()
      print("#"*50)
      print("#")       
      print("  MENU DE ALTA, BAJA Y MODIFICACION DE PELICULAS   ")
      print("#")       
      print("#"*50)     
      print(f"""
        # 1-Alta de Nueva Pelicula.
        # 2-Modificacion de Pelicula Existente.
        # 3-Baja de Pelicula.
        # 0-Volver al Menu Principal.
            """) 
      print("#"*50)
      opcion_abm=int(input("# Ingresa una Opcion: "))
      os.system("cls")
      if opcion_abm==1:
        
        a_B_m_db.alta_de_nueva_pelicula()
        continue 
      elif opcion_abm==2:
       cont1=True  
       while cont1==True:  
          print("#"*50)
          print(f"Modificacion de Pelicula Existente")
          print("#"*50)
          print(f"""
           # 1-Buscar por Id.
           # 2-Buscar por Titulo.
           # 0-Volver.
                      """)
          print("#"*50)
          opc=int(input("Ingresa una opcion: "))
          
          if opc==1: 
             cinema()
             print("#"*50) 
             print("Buscar por ID")
             print("#"*50)
             
             a_B_m_db.modificar_pelicula_por_id()
             input("Presione una tecla para continuar:")
             os.system("cls")
             continue
            
          elif opc==2:
            cinema()
            print("#"*50)
            print("Buscar por Titulo")
            print("#"*50)
            
            a_B_m_db.modificar_pelicula_por_titulo()
            input("Presione una tecla para continuar:")
            os.system("cls")
            continue
          elif opc==0:
           cont1=False 
           break
            
      elif opcion_abm==3:
        cinema()
        print("#"*50)
        print(f"""
             # Baja de Pelicula """)
        print("#"*50)
        
        a_B_m_db.eliminar_pelicula_por_titulo()
        input("Presione una tecla para continuar")
        os.system("cls")
        continue
      elif opcion_abm==0 :
        print("Estas Saliendo de Alta, baja y Modificacion de Peliculas...") 
        opcion_abm=False  
        break
  elif opcion==2:
            cinema()
            print("#"*50)
            print("#")
            print(" CALIFICACION DE TITULOS  ")
            print("#")
            print("#"*50)
            print("")
            
            reportes_estadisticas_db.calificar_peliculas_al_azar()
            os.system("cls")
           
                 
           
              
  elif opcion==3:
    cont3=True
    while cont3==True:    
        cinema()
        print("#"*50)
        print("#")       
        print(" REPORTES Y ESTADISTICAS ")
        print("#")       
        print("#"*50)
        print(f"""
        # 1-Lstados de Peliculas: Titulo,Genero,Sinopsis y Calificacion.
        # 2-Peliculas de Mayor Puntaje
        # 3-Peliculas Disponibles en la Plataforma.
        # 0-Volver
              
        """)
        print("#"*50)
        opcion_reportes=int(input("Ingresa una opcion: ")) 
        os.system("cls")
        if opcion_reportes==1:
          cinema()
          reportes_estadisticas_db.listado_de_peliculas_alfabetico(peliculas)
          continue
        elif opcion_reportes==2:
          cinema()
          reportes_estadisticas_db.mostrar_mejor_calificadas()
          continue 
        elif opcion_reportes==3:
          cinema()
          reportes_estadisticas_db.peliculas_en_streaming(peliculas)
          continue
        else:
         opcion_reportes==0
         print("Saliendo de Reportes y Estadisticas")
         cont3=False 
         break
  
          
  elif opcion==0:
    print(f""" Estas Saliendo de # Cinema+ #...
         Gracias por tus Aportes""")  
    break
  else: 
      print("# Elige una opcion del Menu #")

            



