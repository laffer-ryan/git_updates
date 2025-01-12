import random



with open('counter.txt', 'a') as f:
    for i in range (random.randint(1, 5)):
        f.write('1\n')