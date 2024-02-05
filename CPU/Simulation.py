from SJF import SJF
import copy
import numpy as np
import json
import matplotlib.pyplot as plt
from FCFS import FCFS
from ProcessGeneration import proc_generation
from Data_prep import data_preparation
#wczytanie konfiguracji z pliku txt do słownika config_cpu
config_cpu={}
with open ("CPU/Config_CPU.txt","r") as config:
    for i in config:
        delimiter=i.index(":")
        config_cpu[i[:delimiter]]=int(i[delimiter+1:-1])   
config.close()
#funkcja służąca do generowania wykresów
def Setplot(maxexctimeFCFS, maxecextimeSJF,randomizer, MaxAwaittime):
    plt.title(f"Await time from {randomizer} to {MaxAwaittime}")

    maxexctimeFCFS= maxexctimeFCFS[-1]

    maxecextimeSJF = maxecextimeSJF[-1]


    bar_width = 0.35

    #bar_shift = [x + bar_width for x in maxexctimeFCFS]
    handler = 1
    

    plt.bar(handler, maxexctimeFCFS, color='green', width=bar_width, label="FCFS")
    plt.bar((handler+1), maxecextimeSJF, color='blue', width=bar_width, label="SJF")

    plt.ylabel(f"Avarge execution time")
    plt.legend()
    plt.show()
#nieużywana funkcja do odchyleń standardowych
#arrivalTimes=[]
#def standard_deviation_plot(ARtime , execTimev1 , execTimev2, numoftests):
#    deviation1 = np.std(execTimev1, axis=0)
#    deviation2 = np.std(execTimev2, axis=0)
#    plt.errorbar(execTimev1,ARtime, yerr=deviation1, fmt="o-" , label="SJF")
#    plt.errorbar(execTimev2,ARtime , yerr=deviation2, color="red", fmt="o", label="FCFS")
#    plt.title("standard deviation")
#    plt.legend()
#    plt.show()
#funkcja odpowiedzialna za uruchomienie funkcji generowania procesów z parametrami, wczytanymi z config_cpu. Następnie zapisanie do zmiennej proces_list w wyniku działania funkcji Data_prep
def simulation(configuration):
    path="CPU/Process.txt"
    proc_generation(configuration["AmountOfprocess"],configuration["MaxExecTime"],configuration["MaxAwaitTime"],configuration["AmountOfRepeat"],configuration["RandomizationAwait"],configuration["RandomizationExec"])
    Proces_list=data_preparation(path)
    #pętla wczytująca wszystkie czasy nadejścia i zapisująca je do arrivalTimes
    #for i in Proces_list:
    #    arrivalTimes.append(i[1])
    return Proces_list
Result_FCFS=[]
Result_SJF=[]
if __name__ == "__main__":
    print( config_cpu)
    Proces_list_storage=simulation(config_cpu)
    #stworzenie osobnych list dla algorytmów
    SJF_list_process=copy.deepcopy(Proces_list_storage)
    FCFS_list_process=copy.deepcopy(Proces_list_storage)
    #przekazanie list do algorytmów
    FCFS(FCFS_list_process,Result_FCFS)
    SJF(SJF_list_process,Result_SJF)
    #########################################################
    #FCFS section
    await_time_FCFS=0
    #pętla iterująca po wszystkich procesach i sumująca wszystkie czasy nadejścia
    for i in FCFS_list_process:
        await_time_FCFS+=i[1]
    exec_time_FCFS=0
    #pętla sumująca wszystkie czasy wykonania
    for etime in Result_FCFS:
        exec_time_FCFS+=etime
    #zapisywanie do plików json
    with open ("CPU/stats_FCFS.json","r") as file_FCFS:
        data_FCFS=json.load(file_FCFS)
    data_FCFS["avg_exec_time"].append(exec_time_FCFS/len(Result_FCFS))
    data_FCFS["tables_with_exec_times"].append(Result_FCFS)
    data_FCFS["avg_await_time"].append(await_time_FCFS/len(Result_FCFS))
    with open("CPU/stats_FCFS.json", "w") as file_FCFS:
        json.dump(data_FCFS,file_FCFS,indent=2)
    #########################################################
    #SJF section
    await_time_SJF=0
    #pętla iterująca po wszystkich procesach i sumująca wszystkie czasy nadejścia
    for i in SJF_list_process:
        await_time_SJF+=i[1]
    exec_time_SJF=0
    #pętla sumująca wszystkie czasy wykonania
    for etime in Result_SJF:
        exec_time_SJF+=etime
    #zapisywanie do plików json
    with open ("CPU/stats_SJF.json","r") as file_SJF:
        data_SJF=json.load(file_SJF)
    data_SJF["avg_exec_time"].append(exec_time_SJF/len(Result_SJF))
    data_SJF["tables_with_exec_times"].append(Result_SJF)
    data_SJF["avg_await_time"].append(await_time_SJF/len(Result_SJF))
    with open("CPU/stats_SJF.json", "w") as file_SJF:
        json.dump(data_SJF,file_SJF,indent=2)
    #########################################################
    #funkcja do generowania wykresów na podstawie danych pobranych z plików json
    with open ("CPU/stats_SJF.json","r") as file_SJF:
        data_SJF=json.load(file_SJF)
    with open ("CPU/stats_FCFS.json","r") as file_FCFS:
        data_FCFS=json.load(file_FCFS)
    Setplot(data_FCFS["avg_exec_time"],data_SJF["avg_exec_time"],config_cpu["RandomizationAwait"],config_cpu["MaxAwaitTime"])
    #########################################################
    #with open ("CPU/stats_FCFS.json","r") as file_FCFS_dev:
    #    data_FCFS_dev=json.load(file_FCFS_dev)
    #with open ("CPU/stats_SJF.json","r") as file_SJF_dev:
    #    data_SJF_dev=json.load(file_SJF_dev)
    #standard_deviation_plot(arrivalTimes,data_SJF_dev["tables_with_exec_times"][-1],data_FCFS_dev["tables_with_exec_times"][-1],0)


    
    