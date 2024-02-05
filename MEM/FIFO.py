#import konfiguracji z pliku Mem_conf.py
from Mem_conf import mc
memory_config=mc()
#funkcja symulująca algorytm zastępowania stron FIFO
def FIFO(Ref_list,frame_val):
    #odpowiednio od góry inicjalizacja zmiennych dla stron trafionych, pojemności listy, błędów, głównego licznika oraz kolejki wypełnionej wartościami -1 oraz wielkości takiej jak aktualna bramka
    page_hit=0
    queue_capacity=memory_config["AmountOFframes"][frame_val]
    faults=0
    refs_count=0
    queue=[-1]*queue_capacity
    #pętla wykonująca się dopóki nie przeanalizuje wszystkich wartości
    while refs_count < memory_config["AmountOFrefs"]*memory_config["AmountOFseries"]:
        print(queue)
        print(Ref_list[refs_count])
        #jeżeli aktualny element znajduje się w kolejce, to pomijamy resztę instrukcji i inkrementujemy strony trafione
        if Ref_list[refs_count] in queue:
            print("no fault")
            page_hit+=1
            pass
        #w przeciwnym wypadku, jeżeli element nie jest w kolejce oraz długość kolejki jest mniejsza od długości zdefiniowanej przez bramkę, to dodajemy do błędów +1 i wprowadzamy na 1 miejscu kolejki aktualną wartość
        elif Ref_list[refs_count] not in queue and len(queue) < queue_capacity:
                print("fault")
                faults+=1
                queue.insert(0,Ref_list[refs_count])
        #w przeciwnym wypadku, jako ostatnią wartość wstawiamy aktualną wartość, następnie za pomocą instrukcji pop usuwamy ją z kolejki dodając do zmiennej newest, 
        #potem newest wprowadzamy na sam początek kolejki, zachowując tym samym w kolejce sekwencję od najmłodszego od lewej do najstarszego po prawej stronie elementu kolejki
        else:
            queue[-1]=Ref_list[refs_count]
            newest=queue.pop(-1)
            print(newest,end="niewiem")
            queue.insert(0,newest)
            faults+=1
            print("fault")
        #inkrementacja głównego licznika
        refs_count+=1
    return [faults,page_hit]