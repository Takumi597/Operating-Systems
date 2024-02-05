#funkcja wczytująca konfigurację z pliku Config_MEM.txt do słownika
def mc(memory_config={}):
    with open("MEM/Config_MEM.txt", "r") as mem_config:
        #pętla iterująca po wszystkich liniach, i to jedna linijka
        for i in mem_config:
            #oddzielenie wartości od klucza, klucz przed delimiterem
            delimiter=i.index(":")
            if i[:delimiter]!="AmountOFframes":
                memory_config[i[:delimiter]]=int(i[delimiter+1:-1])
            #w przypadku Amount of frames mamy więcej niż jedną wartość, więc oddzielamy wartości od siebie splitem i zapisujemy do listy, przy okazji każdą wartość zamieniamyna liczbę
            else:
                memory_config[i[:delimiter]]=[int(x) for x in i[delimiter+1:-1].split(",")]
    return memory_config