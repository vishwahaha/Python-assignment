n = input()
coins = [int(n) for n in input().split()] 

coins.sort(reverse=True)

total = 0
for x in coins:
    total += x

myCoins = 0
count = 0

for x in coins:
    myCoins += x
    if myCoins > total - myCoins:
        count += 1
        break
    count += 1

print(count)