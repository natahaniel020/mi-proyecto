"""
EJERCICIO 1.1: GESTION DE MATERIALES BIBLIOGRAFICOS
----------------------------------------------------
CONTEXTO:
Una biblioteca digital necesita gestionar diferentes tipos de materiales:
libros fisicos, libros electronicos, revistas y audiolibros. Todos comparten
informacion basica pero tienen caracteristicas especificas.

REQUERIMIENTOS:
1. Crear una clase abstracta "MaterialBibliografico" con:
   - Atributos privados: titulo, autor, año_publicacion, codigo_unico
   - Metodo abstracto: calcular_valor_prestamo()
   - Metodo abstracto: obtener_tipo_material()
   - Metodos getters y setters (ENCAPSULAMIENTO)

2. Crear clases hijas que hereden de MaterialBibliografico (HERENCIA):
   - LibroFisico: atributos adicionales (num_paginas, editorial, estado_fisico)
   - LibroElectronico: atributos adicionales (tamaño_mb, formato, url_descarga)
   - Revista: atributos adicionales (numero_edicion, mes_publicacion)
   - Audiolibro: atributos adicionales (duracion_minutos, narrador, formato_audio)

3. Implementar calcular_valor_prestamo() de forma diferente en cada clase
   (POLIMORFISMO):
   - LibroFisico: $2.00 por dia
   - LibroElectronico: $1.00 por dia
   - Revista: $0.50 por dia
   - Audiolibro: $1.50 por dia

4. Usar ABSTRACCION para ocultar la complejidad del calculo interno

ENTREGABLES:
- Archivo con las clases implementadas
- Programa de prueba que cree al menos 2 objetos de cada tipo
- Demostrar el polimorfismo usando una lista de materiales
- Mostrar que no se puede instanciar la clase abstracta

"""
from abc import ABC,abstractmethod

class MaterialBibliografico(ABC):

    def __init__(self,titulo: str, autor: str, año_publicacion: int, codigo_unico: int):
        self.__titulo = titulo 
        self.__autor = autor
        self.__año_publicacion = año_publicacion 
        self.__codigo_unico = codigo_unico
    

    @abstractmethod
    def calcular_valor_prestamo(self):
        pass

    @abstractmethod
    def obtener_tipo_material(self):
        pass

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def año_publicacion(self):
        return self.__año_publicacion 
    
    @property
    def codigo_unico(self):
        return self.__codigo_unico
    
    @titulo.setter
    def titulo(self, atr):
        self.__titulo = atr
    
    @autor.setter
    def autor(self, atr):
        self.__autor = atr
    
    @año_publicacion.setter
    def año_publicacion(self, atr):
        self.__año_publicacion = atr
    
    @codigo_unico.setter
    def codigo_unico(self, atr):
        self.__codigo_unico = atr

class LibroFisico(MaterialBibliografico):

    def __init__(self, titulo, autor, año_publicacion, codigo_unico,num_paginas: int, editorial: str, estado_fisico :str):
        super().__init__(titulo, autor, año_publicacion, codigo_unico)
        if num_paginas <= 0: raise ValueError
        self._num_paginas = num_paginas
        self._editorial = editorial
        if estado_fisico not in ("nuevo","excelente","bueno","regular","deteriorado","inservible"): raise ValueError
        self._estado_fisico = estado_fisico
            
    
    def calcular_valor_prestamo(self, day:int)-> float:
        if day <= 0 :
            raise ValueError
        else:
            return 2.00 * day
    
    def obtener_tipo_material(self):
        return "Libro Fisico"

class LibroElectronico(MaterialBibliografico):

    def __init__(self, titulo, autor, año_publicacion, codigo_unico,tamaño_mb: float, formato: str):
        super().__init__(titulo, autor, año_publicacion, codigo_unico)
        if tamaño_mb <= 0: raise ValueError
        self._tamaño_mb = tamaño_mb
        if formato not in ("PDF", "EPUB", "MOBI", "AZW", "DOCX"): raise ValueError
        self.__formato = formato
        self.__url_descarga = f"https://www.libro_nathaniel.com/descargas/{self.titulo}.pdf"
        
    def calcular_valor_prestamo(self, day:int)-> float:
        if day <= 0 :
            raise ValueError
        else:
            return 1.00 * day
    
    def obtener_tipo_material(self):
        return "Libro Electronico"

class Revista(MaterialBibliografico):

    def __init__(self, titulo, autor, año_publicacion, codigo_unico,numero_edicion: int, mes_publicacion: str):
        super().__init__(titulo, autor, año_publicacion, codigo_unico)
        if numero_edicion <= 0: raise ValueError
        self.__numero_edicion = numero_edicion
        if mes_publicacion not in ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"):raise ValueError
        self._mes_publicacion = mes_publicacion

    def calcular_valor_prestamo(self, day:int)-> float:
        if day <= 0 :
            raise ValueError
        else:
            return 0.50 * day
    
    def obtener_tipo_material(self):
        return "Revista"

class Audiolibro(MaterialBibliografico):

    def __init__(self, titulo, autor, año_publicacion, codigo_unico,duracion_minutos: float, narrador: str, formato_audio: str):
        super().__init__(titulo, autor, año_publicacion, codigo_unico)
        if duracion_minutos <= 0: raise ValueError
        self._duracion_minutos = duracion_minutos
        self._narrador = narrador
        if formato_audio not in ("MP3", "WAV", "AAC", "FLAC", "OGG"): raise ValueError
        self._formato_audio = formato_audio
    
    def calcular_valor_prestamo(self, day:int)-> float:
        if day <= 0 :
            raise ValueError
        else:
            return 1.50 * day
    
    def obtener_tipo_material(self):
        return "Audiolibro"