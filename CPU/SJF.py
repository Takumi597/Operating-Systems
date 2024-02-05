#funkcja symulująca algorytm SJF wywłaszczającego
def SJF(proceslist,TmTexec):
    TimerForProcesses = 0
    IfEnded = 2
    AwaitTime = 1
    queue = []
    #pętla wykonująca instukcje dopóki kolejka lub wszystkie wartości na polu 2 proceslist, który pokazuje status procesu, nie będą True (proces wykonany lub w kolejce)
    while not all(item[2] for item in proceslist) or  queue:
        #iteracja po proceslist
        for proc in proceslist:
            #jeżeli czas nadejscia będzie równy głównemu licznikowi (TimerForProcesses) to proces zostanie dodany do kolejki i jego status zmieni się na True
            if proc[AwaitTime] == TimerForProcesses:
                print("Process added to CPU queue....")
                queue.append(proc)
                proc[IfEnded] = True
        if queue:
            #każdorazowe sprawdzanie czy w kolejce nie ma procesu o krótszym czasie potrzebnym do wykonania, czyli dynamiczne sortowanie kolejki według czasu potrzebnego do wykonania
            for q in range(len(queue)):
                for  qq in range(q,len(queue)-1):
                    if queue[qq][0] > queue[qq+1][0]:
                        queue[qq],queue[qq+1]=queue[qq+1],queue[qq]
            #jeżeli czas potrzebny do wykonania będzie równy 0 to proces zostanie usunięty z kolejki, dodany do listy procesów zakończonych
            if queue[0][0] == 0:
                print("process ended , time to execute:" + str(queue[0][3]))
                TmTexec.append(queue[0][3])
                del queue[0]
            #w przeciwnym wypadku od jego czasu potrzebnego do wykonania zostanie odjęte 1
            elif queue[0]:
                print("Exec Process")
                queue[0][0]-=1
        for  subproces in queue[1:]: # dodanie tmTexec do każdego poza tym co sie wykonuje
            subproces[3] +=1
        #inkrementacja głównego licznika
        TimerForProcesses+=1
    print(TimerForProcesses)
    print(TmTexec)  
    return TimerForProcesses 


