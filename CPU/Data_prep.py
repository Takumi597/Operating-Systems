#funkcja przygotywująca dane do analizy
def data_preparation(path):
    with open(path, "r") as proces:
        #inicjalizacja listy procesów
        processList = []
        #pobieranie z pliku txt, iterowanie po pobranych wynikach z wykluczeniem ostatniego znaku(nowa linia) i formatowanie do listy
        temp = [i[:-1] for i in proces]
        #pętla iteruje po nieprzygotowanej liście i rozdziela dane na czas wykonania i czas nadejścia
        for i in range(0, len(temp)):
            for j in temp[i]:
                if j == "|":
                    Delimiter  = temp[i].index("|")
                    #odpowiednio od lewej strony: czas potrzebny do wykonania, czas nadejścia, status procesu, czas zakończenia
                    processList.append([int(temp[i][:Delimiter]), int(temp[i][Delimiter + 1:]), False,0])
                    break
    #sortowanie listy wedle czasu nadejścia
    processList.sort(key=lambda x:x[1])
    return processList