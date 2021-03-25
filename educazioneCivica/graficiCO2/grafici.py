import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

anni= []
anomalie = []

anni1=[]
emissioniTot=[]

emissioniGas=[]
emissioniLiquidFuel=[]
emissioniSolidFuel=[]
emissioniCement=[]
emisisoniGasFLaring=[]

data_file = open("/home/samuele/Scrivania/scuola/4/sistemi/educazioneCivica/Temperature_Anomaly.csv")
data_file1 = open("/home/samuele/Scrivania/scuola/4/sistemi/educazioneCivica/CO2_emissions.csv")

data_reader = csv.reader(data_file, delimiter=',')
data_reader1= csv.reader(data_file1, delimiter= ',')

for k in range(5):
    next(data_reader)

next(data_reader1)

for row in data_reader:
    anni.append(int(row[0]))
    anomalie.append(float(row[1]))

for row in data_reader1:
    anni1.append(int(row[0]))
    emissioniTot.append(int(row[1]))
    emissioniGas.append(int(row[2]))
    emissioniLiquidFuel.append(int(row[3]))
    emissioniSolidFuel.append(int(row[4]))
    emissioniCement.append(int(row[5]))
    emisisoniGasFLaring.append(int(row[6]))

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
fig.suptitle('temperature Anomale')

#grafico per anomalie temperatura
ax1.plot(anni, anomalie, 'o-g')
ax1.set_xlabel('anno')
ax1.set_ylabel('Anomalie C°')

#grafico per emissioni emesse
ax2.plot(anni1, emissioniTot, 'o-r')
ax2.set_xlabel('anno')
ax2.set_ylabel('emissioni')

#grafico per i diversi tipi di emissioni
ax3.plot(anni1, emissioniCement, 'o-r')
ax3.plot(anni1, emissioniGas, 'o-y')
ax3.plot(anni1, emissioniLiquidFuel, 'o-b')
ax3.plot(anni1, emissioniSolidFuel, 'o-m')
ax3.plot(anni1, emisisoniGasFLaring, 'o-g')

ax3.set_xlabel('anno')
ax3.set_ylabel('emissioni')



plt.show()