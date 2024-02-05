import random
def RefsGeneration(amount_refs,amount_pages,amount_series,randomizer):
    #ustawienie ziarna dla losowania wartości z zakresów i wpisanie ich do pliku
    random.seed(8100931)
    Memory=open("MEM/Ref.txt" , "w")
    #generowanie wartości stron 
    for serie in range(amount_series): #ile razy wygeneruje ilość stron określoną przez amount_refs
        for ref in range(amount_refs):
            Memory.write(str(random.randint(randomizer,amount_pages))+"\n")
    Memory.close()        




