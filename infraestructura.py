from aplicacion import GestionMateriales

class MaterialesInfraestructura():

    def tipo_material(cls,input_dict: dict):
        while True:
            try:
                match input_dict("material"):
                    case "LibroFisico":
                        input_dict["num_paginas"] = int(input("Ingrese el numero de paginas en numeros enteros :"))
                        input_dict["editorial"] = input("Ingree la Editorial :")
                        print("Categorias de estado fisico \n" \
                        "nuevo,excelente,bueno,regular,deteriorado,inservible")
                        input_dict["estado_fisico"] = input("Ingrese la categoria a la que Pertenese :")
                        if input_dict["estado_fisico"] not in ("nuevo","excelente","bueno","regular","deteriorado","inservible"): raise ValueError
                
                    case "LibroElectronico":
                        input_dict["tamaño_mb"] = float(input("Ingrese tamaño MB del Material :"))
                        print("Categorias de Formato \n" \
                        "PDF,EPUB,MOBI,AZW,DOCX")
                        input_dict["formato"] = input("Ingrese formato del Material :")
                        if input_dict["formato"] not in ("PDF", "EPUB", "MOBI", "AZW", "DOCX"): raise ValueError

                    case "Revista":
                        input_dict["numero_edicion"] = int(input("Ingrese numero de edicion :"))
                        input_dict["mes_publicacion"] = input("Ingrese nombre mes de publicacion :")
                        if input_dict["mes_publicacion"] not in ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
                        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"): raise ValueError
            
                    case "Audiolibro":
                        input_dict["duracion_minutos"] = float(input("Ingrese tiempo de duracion en minutos :"))
                        input_dict["narrador"] = input("Ingrese nombre del narrador :")
                        print(("MP3, WAV, AAC, FLAC, OGG"))
                        input_dict["formato_audio"] = input("Ingrese formato del Material :")
            
                    case _:
                        print("opcion no valida")
            
            except ValueError:
                print("valor Incorrecto")
            except TypeError:
                print("tipo de dato incorrecto")
                
        
    
    def input_materiales(cls):

        while True:
            try:
                input_dict = {}
                input("Los materiales que puede registrar en el sistemas son :" \
                "LibroFisico, LibroElectronico, Revista, Audiolibro")
                input_dict["material"] = input("Ingrese tipo de material :")
                if input_dict["material"] not in ("LibroFisico","LibroElectronico","Revista","Audiolibro"): raise ValueError
                input_dict["titulo"] = input("Ingrese titulo del material :")
                input_dict["autor"] = input("Ingrese el nombre del autor :")
                input_dict["año_publicacion"] = int(input("Ingrese año de publicacion :"))
                input_dict["codigo_unico"] =  int(input("Ingrese codigo de identificacion :"))

                cls.tipo_material(input_dict)
                return input_dict
                
            except ValueError:
                print("valor Incorrecto")
            except TypeError:
                print("tipo de dato incorrecto")
    

    def registrar_material(cls,material: dict):
        GestionMateriales.crear_Materiales(dict)
        print(GestionMateriales.lista_Materiales[material["codigo_unico"]])

    def crear_prestamo(cls):

        while True:
            try:
                id = int(input("Ingrese codigo unico del material :"))
                if id not in GestionMateriales.dict_materiales: raise ValueError
                day = int(input("Ingrese el numero de dias que desea alquilar el material :"))

                return print(f"Valor a pagar ={GestionMateriales.realizar_préstamo(id,day)}")
            except ValueError:
                print("valor Incorrecto")
            except TypeError:
                print("tipo de dato incorrecto")
    


        



                
    
