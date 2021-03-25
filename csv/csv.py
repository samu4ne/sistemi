#imparare ad usare la libreria csv
import csv


def main():
    with open("/home/samuele/Scrivania/scuola/4/tpsit/pyton/csv/test.csv", newline="") as filecsv:
        lettore = csv.reader(filecsv,delimiter=",")
        for temp in lettore:
            print(temp)

if __name__=="__main__":
    main()