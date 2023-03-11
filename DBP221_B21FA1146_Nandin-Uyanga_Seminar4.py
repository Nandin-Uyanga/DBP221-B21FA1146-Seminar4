#1

import numpy as np
array=np.arange(50,101)
print("50-100")
print(array)

#2

import numpy as np
array=np.zeros(10)
print("10 zeros:")
print(array)
array=np.ones(10)
print("10 ones:")
print(array)
array=np.ones(10)*6
print("10 sixes:")
print(array)

#3

import numpy as np
m= np.arange(20,33).reshape((3, 4))
print(m)

#4

import numpy as np
x = np.eye(3)
print(x)

#5

import numpy as np
x = np.diag([1, 2, 3, 4, 5])
print(x)

#6

import numpy as np
x = np.array([[0,1],[2,3]])
print("2x2:")
print(x)
print("Бүх элементүүдийн нийлбэр:")
print(np.sum(x))
print("Баганын нийлбэр:")
print(np.sum(x, axis=0))
print("Мөрийн нийлбэр:")
print(np.sum(x, axis=1))

#7
salary1= [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
salary2 = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
salary3 = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
salary4 = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
salary5 = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
salary6 = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
salary7 = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
salary8 = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
salary9 = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
salary10 = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]

Salary = np.array([[sal1],[sal2],[sal3],[sal4], [sal5],[sal6],[sal7], [sal8], [sal9], [sal10]])

print("Баганын нийт цалин", np.sum(Salary , axis = 0))

print("Мөрийн нийт цалин", np.sum(Salary ,axis = -1))

AndreaPirlo_G = [80,77,82,82,73,82,58,78,6,35]
SergioBusquets_G = [82,57,82,79,76,72,60,72,79,80]
IkerCasillas_G = [79,78,75,81,76,79,62,76,77,69]
PhilippLahm_G = [80,65,77,66,69,77,55,67,77,40]
SergioAguerod_G = [82,82,82,79,82,78,54,76,71,41]
FranckRibery_G = [70,69,67,77,70,77,57,74,79,44]
ToniKroos_G = [78,64,80,78,45,80,60,70,62,82]
CarlesPuyol_G = [35,35,80,74,82,78,66,81,81,27]
ZlatanIbrahimovic_G = [40,40,40,81,78,81,39,0,10,51]
Antoine Griezmann_G = [75,51,51,79,77,76,49,69,54,62]

Games = np.array([[AndreaPirlo_G], [SergioBusquets_G], [IkerCasillas_G], [PhilippLahm_G], [SergioAguerod_G], [FranckRibery_G], [ToniKroos_G], [CarlesPuyol_G], [ZlatanIbrahimovic_G], [Antoine Griezmann_G]])

print("Баганын нийт Тоглолт", np.sum( Games, axis = 0))

print("Мөрийн нийт Тоглолт", np.sum( Games, axis = -1))

AndreaPirlo_FG = [20,34,45,37,46,34,53,44,46,52]
SergioBusquets_FG = [38,50,42,45,46,30,31,49,41,47]
IkerCasillas_FG = [25,44,24,40,31,42,18,19,39,43]
PhilippLahm_FG = [18,32,26,37,20,35,34,46,24,19]
SergioAguerod_FG = [26,28,24,19,37,32,30,43,31,42]
FranckRibery_FG = [36,25,28,48,23,22,29,24,32,41]
ToniKroos_FG = [42,28,39,43,26,31,50,45,38,36]
CarlesPuyol_FG = [44,46,34,32,37,49,18,25,35,40]
ZlatanIbrahimovic_FG = [22,18,34,44,32,26,19,45,25,23]
Antoine Griezmann_FG = [30,44,50,35,26,41,18,28,40,43]

FieldGoals  = np.array([[AndreaPirlo_FG], [SergioBusquets_FG], [IkerCasillas_FG], [PhilippLahm_FG], [SergioAguerod_FG], [FranckRibery_FG], [ToniKroos_FG], [CarlesPuyol_FG], [ZlatanIbrahimovic_FG], [Antoine Griezmann_FG]])

print("Баганын нийт Гоал ", np.sum( FieldGoals, axis = 0))

print("Мөрийн нийт Гоал", np.sum( FieldGoals, axis = -1))






