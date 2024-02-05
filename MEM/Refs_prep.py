#funkcja iterująca po odczycie i konwertująca każdą wartość na typ liczbowy, usuwając przy okazji znaki nowych linii
def ref_preparation(path):
    refs=[]
    with open(path , "r") as odczyt:
        for i in odczyt:
            refs.append(int(i[:-1]))
        odczyt.close()
    return refs
    
    