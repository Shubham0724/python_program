##For_loop
for k in range(4,9):
    print(k)

##while_loop
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

##Nested_loops
while (i<=3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i*k))
    i = i + 1
    print()

##control_statements

#pass
i = 1
while (i<5):
    pass

for j in range(5):
    pass

if (i == 2):
    pass

#continue
i = 1
while (i <= 10):
    i = i + 1
    if (i%2 != 0):
        continue
    print(i)

#break
for i in range(1, 10):
    print(i)
    if (i == 5):
        break
        