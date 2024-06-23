s = input("Enter a sequence of integers separated by whitespace: ")

#變成list
l = s.split(" ")

#list內元素轉為integer
al = []
for i in range(len(l)):
    al.append(int(l[i]))
    
current = []
longest = []
bl = []
for i in range(len(al)-1):
    for j in range(i+1, len(al)+1):
        print(al[i:j])
        bl = al[i:j]
        x = len(bl)
        while x >= 2:
            if bl[len(bl)-x+1] == bl[len(bl)-x]+1:
                current = bl
                if len(current) > len(longest):
                    longest = current
            x = x - 1
                    
print("Length:", len(longest))
print("LICS:", longest)