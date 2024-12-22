with open("22.txt") as fin:
    lines = fin.read().strip().split("\n")
    
ans = 0
profit = {}

for line in lines:
    line = int(line)
    prices = [line%10]
    seq = []
    profit_line = {}
    for i in range(2000):
        line = ((line * 64) ^ line) % 16777216
        line = ((line // 32) ^ line) % 16777216
        line = ((line * 2048) ^ line) % 16777216
        prices.append(line %10)
    for i in range(1,len(prices)):
        seq.append(prices[i] - prices[i-1])
        if len(seq) == 4:
            s = tuple(seq)
            if s not in profit_line:
                profit_line[s] = prices[i]
                if s not in profit:
                    profit[s] = prices[i]
                else:
                    profit[s] += prices[i]
            seq = seq[1:]

for key,value in profit.items():
    if value > ans:
        ans = value
print(ans)


        