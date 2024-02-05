#import konfiguracji z pliku Mem_conf.py
from Mem_conf import mc
memory_config=mc()
#funkcja symulująca algorytm zastępowania stron LRU
def LRU(Ref_list,frame_val):
    #odpowiednio od góry inicjalizacja zmiennych dla pojemności listy, błędów, głównego licznika, kolejki, kolejki dla LRU, stron trafionych
    queue_size=memory_config["AmountOFframes"][frame_val]
    faults=0
    refs_count=0
    queue=[]
    LRUqueue=[]
    page_hit=0
    #pętla wykonująca się dopóki nie przeanalizuje wszystkich wartości
    while refs_count < memory_config["AmountOFrefs"]*memory_config["AmountOFseries"]:
        #przypadek trafienia strony (nadchodząca ramka już jest w kolejce)
        if Ref_list[refs_count] in queue:
            print("no fault")
            page_hit+=1
            pass
        #jeżeli strona zostanie trafiona i znajduje się w kolejce LRU to usuwamy wartość z indeksu Ref_list[refs_count] po czym dodajemy nową wartość
            if Ref_list[refs_count] in LRUqueue:
                del LRUqueue[LRUqueue.index(Ref_list[refs_count])]
            LRUqueue.append(Ref_list[refs_count])
            pass
        #jeżeli nie ma w kolejce strony i długość kolejki jest mniejsza niż ta ustalona przez bramkę, to wartość dodajemy do kolejki zwykłej i LRU, oraz inkrementujemy błąd
        elif Ref_list[refs_count] not in queue:
            if len(queue) <queue_size:
                queue.append(Ref_list[refs_count])
                LRUqueue.append(Ref_list[refs_count])
                faults+=1
                print("fault")
            #w przeciwnym wypadku, gdy długość kolejki jest większa niż ta ustalona przez bramkę, to w kolejce zwykłej w miejsce wartości indeksu 1 indeksu w kolejce LRU wstawiamy nową wartość
            else:
                queue[queue.index(LRUqueue[0])]=Ref_list[refs_count]
                #usunięcie 1 wartości z kolejki LRU, dodanie nowej wartości na koniec kolejki LRU, inkrementacja błędu
                del LRUqueue[0]
                LRUqueue.append(Ref_list[refs_count])
                faults+=1
                print("fault")
        #inkrementacja głównego licznika
        refs_count+=1
    return [faults,page_hit]



