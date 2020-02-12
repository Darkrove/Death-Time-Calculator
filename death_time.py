from numpy import *
import math as m
# Temp of body before death which is same for all body
Body_Temp = 98.6
To = ''
t = ''
Tt = ''
k = ''
Ts = ''
in_te=''
def k_cal():
    global To,t,Tt,k,Ts, in_te
    # Initial temperature of body when found
    To=in_te=int(input("Enter Initial Temperature(*c): "))
    # Time interval 
    t=int(input("Enter Time Interval (min): "))
    # Temp after some times 
    Tt=int(input(f"Enter Temperature After {t} Minute(*c): "))
    # Surrounding temp (ambient)
    Ts=int(input("Enter Surrounding Temperature(*c): "))
    # Calculating k by transfering known value opposite side 
    # Tt = Ts+(To-Ts)*e**(-k*t)
    k = (log((Tt-Ts)/(To-Ts))/(log(e))*1/60)
    k = round(abs(k),4)
    print(f"Value Of Proportionality Constant(k): {k}")
    Time_cal()
def Time_cal():
    global Tt,To, t
    Tt=To
    To=Body_Temp
    t = (log((Tt-Ts)/(To-Ts))/(log(e))*(-1/k))
    t = m.ceil(t)
    print(f"Death Was Happen Before {t} Minute When Body Was Found And \nInitial Temperature Was {in_te} *C.")
k_cal()
