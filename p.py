import random
import time
import os

nums = '1234567890'
gen = int(input("[?] Poxies to generate: "))
port = input("[?] Ports for proxes: ")


for i in range(gen):
    fst = ''.join((random.choice(nums) for i in range (3)))
    sec = ''.join((random.choice(nums) for i in range (3 or 2 or 1)))
    thd = ''.join((random.choice(nums) for i in range (3 or 2)))
    fht = ''.join((random.choice(nums) for i in range (3 or 2)))


    r = fst + "." + sec + "." + thd + "." + fht + ":" + port

    output = open("generated proxies.txt", "a")

    output.write(r + "\n")

print(f"generating {gen} proxies")
time.sleep(1)
print(f"successfully generated {gen} proxies")
time.sleep(1)
os.system('cls')