def anomalie(anomalieAnno):
    primoAnno = int(input("Inserisci 1 anno:\n"))
    secondoAnno = int(input("Inserisci 2 anno:\n"))
    maxMin = []

    for k in range(anno1, anno2 + 1):
        maxMin.append(float(anomalieAnno[str(k)]))
    
    print(f"minima anomalia: {min(maxMin)}, massima anomalia {max(maxMin)}")

if __name__ == "__main__":
    anomalieAnno = {}
    Succ = 2
    cnt = 1
    somma = 0
    media = 0
    anno = open("annual.csv", "r").readlines()
    
    for line in anno[1:]:

        if Succ >= len(anno):
            Succ = 0

        line = line[:-1].split(",")
        line2 = anno[Succ].split(",")

        if line[1] == line2[1]:
            somma = somma + float(line[2])
            cnt=cnt+1
        else:
            somma = somma + float(line[2])
            media = somma / cnt
            anomalie[line[1]] = media
            cnt=cnt+1
            somma = 0
        
        Succ =Succ+1
    
    anomalie(anomalieAnno)





