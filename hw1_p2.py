

#數值輸入
f = float(input("Input the force: "))
m1 = float(input("Input the mass of m1: "))
d = float(input("Input the distance: "))

g = 0.0000000000667
c = 299792458

#公式
m2 = ((d**2) * f) / (g * m1)
e = m2 * c**2

#輸出
print("The mass of m2 = ", m2)
print("The energy of m2 = %e" % e)