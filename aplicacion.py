import dominio
from fabrica import fabricaMateriales

class GestionMateriales:
    
    dict_materiales ={}
    dict_prestamo = {}

    # Recibe datos, usa la fábrica, registra el material
    @classmethod
    def crear_Materiales(cls, material: dict):
        materialObj = fabricaMateriales.crearMaterial(  material)
        cls.dict_materiales[materialObj.codigo_unico]= materialObj

    #Devuelve la colección almacenada.
    @classmethod
    def lista_Materiales(cls):
        return cls.dict_materiales
    
    #Buscar material por identificador Permite localizar uno específico.
    @classmethod
    def buscar_materiales(cls,id: int):
        assert id in cls.dict_materiales
        return cls.dict_materiales[id]
    
    @classmethod
    def realizar_préstamo(cls,id,day: int):
        if id not in cls.dict_materiales: raise ValueError
        obj = cls.dict_materiales[id]
        prestamo = obj.calcular_valor_prestamo(day)
        cls.dict_prestamo[id]= prestamo
        return prestamo



        

