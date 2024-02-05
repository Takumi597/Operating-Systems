import random
def proc_generation(Process_num,Max_process_exec_time,Max_await_time,Repeat_num,randomizer_for_await_time,randomizer_for_exec_time):
    #ustawienie ziarna dla losowania wartości z zakresów i wpisanie ich do pliku
    random.seed(1111)
    Process=open("CPU/Process.txt","w")
    for i in range(0,Repeat_num):
        for j in range(0,Process_num):
            #odpowiednio od lewej: czas potrzebny do wykonania,czas nadejścia
            proc=str(random.randint(randomizer_for_exec_time,Max_process_exec_time)) + " | " + str(random.randint(randomizer_for_await_time,Max_await_time)) + "\n"
            Process.write(proc)
