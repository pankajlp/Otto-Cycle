
import math
import matplotlib.pyplot as plt


# Function for kinematics of engine

'''The parameters are the bore length,stroke length, connecting rod length,
the compression ratio and the start and the end crank angle'''
def engine_kinematics(bore, stroke, con_rod, cr, start_crank, end_crank):

	a = stroke/2                    #crank pin radius
	R = con_rod/a                  

	Vs = (math.pi/4)*pow(bore,2)*stroke  #Swept Volume
	Vc = Vs/(cr-1) # Clearance Volume

	# Conversion to Radians using math library fuction
	startc = math.radians(start_crank) 
	endc = math.radians(end_crank)

	n = 75 # Number of divisions
	dt = (endc-startc)/(n-1) # Spacing between each division
	V = [] # Defining empty array for volume

	for i in range(0,n): #Using loop to append to the volume array
		theta = startc + i*dt
		V.append((1 + 0.5*(cr-1)*(R+1-math.cos(theta)-(pow((pow(R,2)-pow(math.sin(theta),2)),0.5))))*Vc)
		
	return V

    
    

# Inputs of the geometric parameters
    #Taking the engine parameters of Buggati Veyron
bore = 0.086
stroke = 0.086
con_rod = 0.23
p1 = 101325 #Initial Pressure
t1 = 288 #Initial Temperature
t3 = 2179
cr = 9 #Compression ratio 
gamma = 1.4

# Calculating Swept volume and Clearance volume
Vs = (math.pi/4)*pow(bore,2)*stroke
Vc = Vs/(cr-1)
v1 = Vs + Vc
v2 = Vc

# Process 1-2: Isentropic compression

# p1*v1^gamma = p2*v2^gamma; t2/t1 = (v1/v2)^(gamma-1) = cr^(gamma-1)
t2 = t1*pow(cr,(gamma-1)) #Calculating T2
p2 = p1*pow(cr,gamma)     #Calculating p2

# Calling the function to determine the Compression Volume
V_comp = engine_kinematics(bore, stroke, con_rod, cr, 180, 0) 
constant_c = p1*pow(v1,gamma)
P_comp = []


for j in V_comp: # Finding the Compression Pressure
	P_comp.append(constant_c/pow(j,gamma))

# Process 2-3: Constant volume heat addition
v3 = v2
p3 = (p2*t3)/t2

# Process 3-4: Isentropic expansion

v4 = v1
p4 = p3*pow((v3/v4),gamma)

# Calling the function for Expansion Volume
V_exp = engine_kinematics(bore, stroke, con_rod, cr, 0, 180)
constant_c = p3*pow(v3,gamma)
P_exp = []

for j in V_exp: #Determining the Expansion Pressure
	P_exp.append(constant_c/pow(j,gamma))

#Calculating the Thermal efficiency
eff = 1 - (1/pow(cr,(gamma-1)))
eff = str(eff*100)

print("Thermal Efficiency of the Otto Cycle = " + eff + " %")

# Plotting the PV Diagram
plt.figure()
plt.plot(V_comp,P_comp, label='Isentropic compression')
plt.plot([v2,v3],[p2,p3], label='Heat addition')
plt.plot(V_exp,P_exp, label='Isentropic expansion')
plt.plot([v4,v1],[p4,p1], label='Heat Rejection')
plt.xlabel('Volume')
plt.ylabel('Pressure')
plt.title('P-V Diagram of Otto Cycle')
plt.legend()
plt.show()

 


