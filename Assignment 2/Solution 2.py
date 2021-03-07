import pandas as pd
import matplotlib.pyplot as plt
data = pd. read_csv('proyek2.txt', sep = '\s+')

# NOTE : Binding Energi Eksperimen
data.insert(loc=3, column='BindingEnergi(MeV)', value=(data['BindingEnergi(kEv)']/1000)) # NOTE : Konversi dari kEv menjadi MeV
data.insert(loc=4, column='BindingEnergi(MeV)/A', value=(data['BindingEnergi(MeV)']/data['A'])) #NOTE : BE/A
fig, ax = plt.subplots()
_ = ax.scatter(data[ 'A'], data[ 'BindingEnergi(MeV)/A'], color _ = 'blue')
_ = ax.set_xlabel('A')
_ =ax.set_ylabel( 'BE/A')
_ = ax.set_title('Grafik Binding Energi Eksperimen/A vs A')
#plt.savefig('BEeksperimen.png', dpi=600, bbox_inches='tight')

# NOTE : Binding Energi Teori
data.insert(loc=1, column='N', value=( data['A']-data['Z'])) # NOTE: N = neutron
subset = data[['A', 'Z', 'N']]
tuples = [tuple(x) for x in subset.values]
av = 15.8 #MeV
ab = 18.3 #MeV ; NOTE : ab disini sama dengan as
ac = 0.714 #MeV
asym = 23.2 #MeV
BE_teori = listo)
for A,Z,N in tuples :
    if z% 2 == 0 and N % 2 == 0 : # NOTE : genap-genap
        BE_SEM = av*A - ab*A**(2/3) - Z*(Z-1)*ac/A**(1/3) - asym*(N-Z)**2/A + 33.5
    elif Z % 2 == 1 and N % 2 == 1 :# NOTE : ganjil-ganjil
        BE_SEM = av*A - ab*A**(2/3) - Z*(Z-1)*ac/A**(1/3) - asym*(N-Z)**2/A - 33.5
    elif z% 2 == 0 and N % 2 == 1: # NOTE : genap-ganjil
        BE_SEM = av*A - ab*A**(2/3) - Z*(Z-1)*ac/A**(1/3) - asym*(N-Z)**2/A
    elif Z % 2 == 1 and N % 2 == 0 ; # NOTE : ganjil-genap
        BE_SEM = av*A - ab*A**(2/3) - Z*(Z-1)*ac/A**(1/3) - asym*(N-Z )**2/A
    BE_teori.append(BE_SEM)
BE_values = pd. Series(BE_teori)
data.insert(loc=6, column='BE_SEM', value=BE_values ) # NOTE : Memasukkan data BE SEM kedalam tabel data
data.insert(loc=7, column='BE_SEM/A', value=(data['BE_SEM']/data['A'])) # NOTE : BE_SEM/A
fig, ax = plt.subplots()
_1 = ax.scatter(data['A'], data[ 'BE_SEM/A'], color = 'red', label='BE teori')
_2 = ax.scatter(data['A'], data[ 'BindingEnergi(MeV)/A'], color = 'blue', label='BE eksperimen')
_ = plt.legend( handles=[_1, 2])
_ = ax.set_xlabel('A')
_ = ax.set_ylabel( 'BE/A')
_ = ax.set_title('Grafik Binding Energi')
#plt.savefig('BEgabunganVID.png', dpi=600, bbox_inches='tight')

#NOTE : Menampilkan "Magic Number" (BE EKSPERIMEN - BE TEORI (SEM))
data.insert(loc=8, column='Magic_Number', value=(data['BindingEnergi (MeV)'] - data[ 'BE_SEM'])) # NOTE : Menampilkan Magic Number (BE EKSPERIMEN - BE TEORI (SEM))
fig, ax = plt.subplots()
_ = ax.scatter(data['Z'], data[ 'Magic_Number'), color = 'red')
_ = ax.set_xlabel('Z')
_ = ax.set_ylabel('BE')
_ = ax.set_title('Grafik Magic Number')
#plt.savefig( 'Magic Numz.png', dpi=600, bbox_inches='tight')

fig, ax = plt.subplots()
_ = ax.scatter(data['N'], data[ 'Magic_Number'], color = 'blue')
_ = ax.set_xlabel('N)
_ = ax.set_ylabel( 'BE')
_ = ax.set_title( 'Grafik Magic Number')
#plt.savefig( 'Magic Numn.png', dpi=600, bbox_inches='tight')


