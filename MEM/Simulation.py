from Refs_prep import ref_preparation
import json,copy
import matplotlib.pyplot as plt
from RefsGeneration import RefsGeneration
from Mem_conf import mc
#wczytanie konfiguracji w formie gotowego słownika z pliku Mem_conf
memory_config=mc()
from FIFO import FIFO
from LRU import LRU
path=("MEM/Ref.txt")
print(memory_config)
#funkcja służąca do generowania wykresów
def setplot(faults1, algorithm1, amountRefs1, frames1, faults2, algorithm2, amountRefs2, frames2):
    plt.title("Comparison of Algorithms")


    Frames1 = [i for i in frames1[-1]]
    Faults1 = [j for j in faults1[-1]]


    Frames2 = [i for i in frames2[-1]]
    Faults2 = [j for j in faults2[-1]]

    bar_width = 0.35


    bar_shift = [x + bar_width for x in Frames1]


    plt.bar(Frames1, Faults1, color='green', width=bar_width, label=algorithm1)
    plt.bar(bar_shift, Faults2, color='blue', width=bar_width, label=algorithm2)

    plt.xlabel("frames")
    plt.ylabel(f"faults for specific amount of refs")
    plt.xticks(Frames1)
    plt.legend()
    plt.show()

def simulation(configuration):
    path="MEM/Ref.txt"
    RefsGeneration(configuration["AmountOFrefs"],configuration["AmountOFpages"],configuration["AmountOFseries"],configuration["Randomizer"])
    RefsTable=ref_preparation(path)
    return RefsTable
if __name__ == "__main__":
    Result_FIFO=[]
    Result_LRU=[]
    Ref_storage=simulation(memory_config)
    FIFO_storage=[i for i in Ref_storage] #kopie tablicy
    LRU_storage=copy.deepcopy(Ref_storage)
    #testowanie obu algorytmów dla różnych bramek
    for j in range(0,len(memory_config["AmountOFframes"])):
        List_FIFO=FIFO(FIFO_storage,j)
        List_LRU=LRU(LRU_storage,j)
        Result_FIFO.append([memory_config["AmountOFframes"][j],List_FIFO[0],List_FIFO[1]])
        print(List_FIFO)
        Result_LRU.append([memory_config["AmountOFframes"][j],List_LRU[0],List_LRU[1]])
    ##################################################################
    #LRU section
    LRU_pagehit=[]
    LRU_faults=[]
    LRU_frames =[]
    #wczytanie pliku json do słownika
    with open("MEM/stats_LRU.json" , "r") as LRU_file:
        LRU_data = json.load(LRU_file)
    #wczytanie faultsów z Result_LRU do jsona
    for i in range(len(Result_LRU)):
        LRU_faults.append(Result_LRU[i][1])
    LRU_data["faults"].append(LRU_faults)
    #wczytanie frameów z Result_LRU do LRU_frames
    for j in range(len(Result_LRU)):
        LRU_frames.append(Result_LRU[j][0])
    #wczytanie page hitów z Result_LRU do LRU_pagehit
    for g in range(len(Result_LRU)):
        LRU_pagehit.append(Result_LRU[g][2])
    #wprowadzenie do słownika LRU_data nowych wartości
    LRU_data["frames"].append(LRU_frames)
    LRU_data["refsAmount"].append(memory_config["AmountOFrefs"])
    LRU_data["pagehit"].append(LRU_pagehit)
    #zapisanie słownika do pliku json
    with open("MEM/stats_LRU.json", "w") as LRU_file:
        json.dump(LRU_data ,  LRU_file , indent=2)
    ##################################################################
    #FIFO section
    FIFO_faults = []
    FIFO_frames = []
    FIFO_pagehit=[]
    #wczytanie pliku json do słownika
    with open("MEM/stats_FIFO.json", "r") as FIFO_file:
        FIFO_data = json.load(FIFO_file)
    #wczytanie faultsów z Result_FIFO do jsona
    for i in range(len(Result_FIFO)):
        FIFO_faults.append(Result_FIFO[i][1])
    FIFO_data["faults"].append(FIFO_faults)
    #wczytanie frameów z Result_FIFO do FIFO_frames
    for j in range(len(Result_FIFO)):
        FIFO_frames.append(Result_FIFO[j][0])
    #wczytanie page hitów z Result_FIFO do FIFO_pagehit
    for g in range(len(Result_FIFO)):
        FIFO_pagehit.append(Result_FIFO[g][2])
    #wprowadzenie do słownika FIFO_data nowych wartości
    FIFO_data["frames"].append(FIFO_frames)
    FIFO_data["refsAmount"].append(memory_config["AmountOFrefs"])
    FIFO_data["pagehit"].append(FIFO_pagehit)
    #zapisanie słownika do pliku json
    with open("MEM/stats_FIFO.json", "w") as FIFO_file:
        json.dump(FIFO_data, FIFO_file, indent=2)
    ##################################################################
    #funkcja do generowania wykresów na podstawie danych pobranych z plików json
    with open("MEM/stats_LRU.json" , "r") as LRUfile:
        LRUdata = json.load(LRUfile)
    with open("MEM/stats_FIFO.json" , "r") as FIFOfile:
        FIFOdata = json.load(FIFOfile)
    setplot(LRUdata["faults"], LRUdata["algorithm"], LRUdata["refsAmount"], LRUdata["frames"],
            FIFOdata["faults"], FIFOdata["algorithm"], FIFOdata["refsAmount"], FIFOdata["frames"])
    #zero
    


    