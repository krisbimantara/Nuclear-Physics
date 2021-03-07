# Mencari nilai koefisien aki dengan aljabar linier (Matrix)
# [N] = [V][L][V]^-1[No]

# Referensi
#Moral, L., & Pacheco, A. F. (2003). Algebraic approach to the radioactive decay equations. 
#American Journal of Physics, 71(7), 684–686. https://doi.org/10.1119/1.1571834

import numpy as np
from sympy import *

No = 1000
t = Symbol('t')

# Waktu Paruh V, Cr, dan Mn
halfLifeV = 0.23
halfLifeCr = 5.9*60
halfLifeMn = 2.58*60*60

# Konstanta peluruhan (lamda)
l1 = np.log(2)/halfLifeV
l2 = np.log(2)/halfLifeCr
l3 = np.log(2)/halfLifeMn
l4 = 0

# Matrix A
dN = np.array([[-l1, 0, 0, 0],
             [l1, -l2, 0, 0],
             [0, l2, -l3, 0],
             [0, 0, l3, -l4]])

# Matrix N0
N0 = np.array([[No],[0],[0],[0]])

# Mencari eigenvalues dan eigenvectors dari matrix A 
dN_eigenvalues, dN_eigenvector = np.linalg.eig(dN) 
  

# Membuat matriks diagonal eigenvalues
dN_eigenvalues_Diag = np.diag(dN_eigenvalues)
dN_eigenvalues_2 = Matrix(dN_eigenvalues_Diag)

# Mmebuat matix diagonal exp(-lamda*t)
L = exp(t*dN_eigenvalues_2);

#[N] = eigenvector [dN] * [L] * eigenvector [dN]^-1 * [N0]
N = dN_eigenvector*L*np.linalg.inv(dN_eigenvector)*N0;

# Menampilkan matrix N yang berisi koefisien aki
N

# Nilai - nilai koefisien a
a11 = str(N.row(0)[0])[0:6]
a21 = str(N.row(1)[0]).replace(' ','')[0:17]
a22 = str(N.row(1)[0]).replace(' ','')[43:59]
a31 = str(N.row(2)[0]).replace(' ','')[0:17]
a32 = str(N.row(2)[0]).replace(' ','')[42:59]
a33 = str(N.row(2)[0]).replace(' ','')[87:102]
a41 = str(N.row(3)[0]).replace(' ','')[6:26]
a42 = str(N.row(3)[0]).replace(' ','')[52:68]
a43 = str(N.row(3)[0]).replace(' ','')[95:111]
a44 = str(N.row(3)[0]).replace(' ','')[0:6]
print('Nilai koefisien a11 = {}'.format(a11))
print('Nilai koefisien a21 = {}'.format(a21))
print('Nilai koefisien a22 = {}'.format(a22))
print('Nilai koefisien a31 = {}'.format(a31))
print('Nilai koefisien a32 = {}'.format(a32))
print('Nilai koefisien a33 = {}'.format(a33))
print('Nilai koefisien a41 = {}'.format(a41))
print('Nilai koefisien a42 = {}'.format(a42))
print('Nilai koefisien a43 = {}'.format(a43))
print('Nilai koefisien a44 = {}'.format(a44))

# Plot N1,N2,N3,N4 sebagai fungsi waktu
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
_ = ax.plot(time, N1, label='V-56')
_ = ax.plot(time, N2, label='Cr-56')
_ = ax.plot(time, N3, label='Mn-56')
_ = ax.plot(time, N4, label='Fe-56')
_ = ax.set_xlabel('t (s)')
_ = ax.set_ylabel('N(t)')
_ = ax.set_title('Evolusi jumlah unsur radioaktif N(t) sebagai fungsi waktu')
_ = ax.set_xscale('log')
_ = ax.legend(loc='upper right')
_ = ax.grid()
#plt.savefig('Nt.png', dpi=600, bbox_inches='tight')

# Mencari nilai Aktivitas unsur
# A = N * lamda

A1 = N1*l1
A2 = N2*l2
A3 = N3*l3
A4 = N4*l4

#Plot Aktivitas sebagai fungsi waktu
fig, ax = plt.subplots()
_ = ax.plot(time, A1, label='V-56')
_ = ax.plot(time, A2, label='Cr-56')
_ = ax.plot(time, A3, label='Mn-56')
_ = ax.set_xlabel('t (s)')
_ = ax.set_ylabel('A(t)')
_ = ax.set_title('Aktivitas V-56, Cr-56, Mn-56 sebagai fungsi waktu')
_ = ax.set_xscale('log')
_ = ax.set_yscale('log')
_ = ax.set_ylim(10**(-3),10**4)
_ = ax.legend(loc='upper right')
_ = ax.grid()
#plt.savefig('At.png', dpi=600, bbox_inches='tight')

# Aktivitas maksimum dan waktunya
for x,y1 in zip(time,A1):
    if y1 == max(A1):
        print('Aktivitas maksimum unsur 1 ≈ {} Bq dan terjadi pada saat t = {} s'.format(round(y1),round(x,1)))
        break

for x,y2 in zip(time,A2):
    if y2 == max(A2):
        print('Aktivitas maksimum unsur 2 ≈ {} Bq dan terjadi pada saat t = {} s'.format(round(y2),round(x,1)))
        break

for x,y3 in zip(time,A3):
    if y3 == max(A3):
        print('Aktivitas maksimum unsur 3 ≈ {} Bq dan terjadi pada saat t = {} s'.format(round(y3,2),round(x,1)))
        break
