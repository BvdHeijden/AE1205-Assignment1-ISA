from math import exp

#Initial values
g0=9.80665
R=287.0
T0=288.15
p0=101325.0
rho0=p0/(R*T0)

#Configure input options
options=[["meters",1],["feet",0.3048],["Flight Level",30.48]]

ISA_Data=[]
#Data format: [    name,       H_start, H_end,   a    ]
ISA_Data.append(["Troposphere" ,0     ,11000 ,-0.0065 ])
ISA_Data.append(["Tropopause"  ,11000 ,20000 ,0       ])
ISA_Data.append(["Stratosphere",20000 ,32000 ,0.001   ])
ISA_Data.append(["Stratosphere",32000 ,47000 ,0.0028  ])
ISA_Data.append(["Stratopause" ,47000 ,51000 ,0       ])
ISA_Data.append(["Mesosphere"  ,51000 ,71000 ,-0.0028 ])
ISA_Data.append(["Mesosphere"  ,71000 ,86000 ,-0.002  ])

#choose which altitude mode
print("*** ISA Calculator ***\n\n1. Calculate ISA for altitude in meters\n2. Calculate ISA for altitude in feet\n3. Calculate ISA for altitude in FL")
inputChoice=options[int(input("\nEnter your Choice: "))-1]

#request altitude from user
Useralt=float(input("Enter Altitude: "))
alt=Useralt*inputChoice[1]

T=T0
p=p0
rho=rho0

#Calculate ISA values at requested altitude
for layer in ISA_Data:
    h0=layer[1]
    h1=layer[2]
    a=layer[3]
    
    if alt>h0:
        name=layer[0]
        T_old=T
        T=T+a*(min(alt,h1)-h0)
        
        if a!=0:
            p=p*((T/T_old)**(-g0/(a*R)))
        else:
            p=p*(exp(-g0*(min(alt,h1)-h0)/(R*T)))
        
        rho=p/(R*T)

print("\nThis altitude is in the",name)
print("Temperature:",round(T,2),"K (",round(T-273.15,2),"C)")
print("Pressure   :",round(p,0),"Pa (",round(100*p/p0,0),"% SL)")
print("Density    :",round(rho,4),"km/m3 (",round(100*rho/rho0,0),"% SL)")
