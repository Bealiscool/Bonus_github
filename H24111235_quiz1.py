
#輸入芮氏規模
r = float(input("Please input a Richter scale value: "))

#能量公式
E = 10 ** ((1.5 * r) + 4.8)

#炸彈能量
T = E / (4.184 * (10 ** 9))

#營養午餐
N = E / 2930200

#輸出結果
print("Richter scale value: " , r)
print("Equivalence in Joules: %.5f" % (E))
print("Equivalence in tons of TNT: %.5f" % (T))
print("Equivalence in the number of nutritious lunches: %.5f" % (N))
