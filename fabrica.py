

class fabricaMateriales():
    
    def crearMaterial(cls,materiales: dict):
        tipo = materiales.pop("material")
        obj = tipo(**materiales)
        return obj


