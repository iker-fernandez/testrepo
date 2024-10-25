import numpy as np
import math

xi=24.59
k=8.617E-5
T=8000
ne=1E14
nH=2.139E15
nHe=2.139E14
q=xi/k/T
ans=2.07E-16*ne/2*T**(-1.5)*np.exp(q)

h=4.136E-15
c=3E10

l1=320E-8
l2=850E-8
l3=1215E-8

nu1=3E10/l1
nu2=3E10/l2
nu3=3E10/l3
R=1.0968E5

np=1E14
nH=2.139E15
nHe=2.139E14
a0=1.99654
a1=-1.18267E-5
a2=2.64243E-6
a3=-4.40524E-10
a4=3.23992E-14
a5=-1.39568E-18
a6=2.78701E-23


gbf=1-0.3456*(l2*R-0.5)/(l2*R)**(1/3) #Gaunt BF

bfH=2.815E29*gbf/(nu2)**3 #BF H

bfHe=2.951209E14/nu1**2 #BF He I

bfHe2=2.815E29*gbf/2/(nu1)**3 #BF He II

chi_bf=bfHe*nHe*(1-math.exp(-(h*nu1)/(k*T)))


'''
bfHe2=(a0+a1*l2+a2*l2**2+a3*l2**3+a4*l2**4+a5*l2**5+a6*l2**6)*10**(-18)

gff=1+0.3456*(l1*k*T/h/c+0.5)/(l1*R)**(1/3) #Gaunt FF
ffH=3.7E8*gff/(T**0.5*nu1**3) #FF H
ffHe2=3.7E8*gff*4/(T**0.5*nu1**3) #FF H

a=-10.92/k/T
b=int(a)

ffHe=4*math.exp(b)*ffH

chi_ff=ffHe*ne*nHe*(1-math.exp(-(h*nu1)/(k*T)))

print(chi_ff)

'''
gbb=0.869-(3/8) #Gaunt BB
f=2**5*gbb/(3**1.5*math.pi*8*(1-1/4)**3) #Fuerza oscilador
e=5.338E-29
m=9.1E-28
s=math.pi*e**2/m/c*f #Sigma BB


print(s,s*nH,1.6E-19*3.336E-10)
'''

print(h*c/10.2)
'''