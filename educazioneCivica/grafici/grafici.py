import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temperatura_media = []
giorni_giacca = []
giorni_scuola=[]
giorni_videogiochi= []
data_file = open("/home/samuele/Scrivania/scuola/4/sistemi/file.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    mesi_n.append(int(row[0]))
    temperatura_media.append(float(row[1]))
    giorni_giacca.append(float(row[2]))
    giorni_scuola.append(float(row[3]))
    giorni_videogiochi.append(float(row[4]))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('dati medi per mesi')

ax1.plot(mesi_n, temperatura_media, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperatura media')

ax2.plot(mesi_n, giorni_giacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('giorni giacca')

ax3.plot(mesi_n, giorni_scuola, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('giorni scuola')

ax4.plot(mesi_n, giorni_videogiochi, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('giorni videogame')
plt.show()