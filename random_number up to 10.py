import random
x = 0
while x == 0:
    rand_num = random.randint(1, 10)
    if rand_num <= 10:
        x = rand_num
print(x)