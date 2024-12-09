ans = 0
file_and_free = []
with open('9.txt', 'r') as file:
    i=0
    file_id = 0
    for line in file:
        line.strip()
        for d in line:
            if i % 2 == 0:
                for j in range(int(d)):
                    file_and_free.append(file_id)
                file_id += 1 
            else:
                for j in range(int(d)):
                    file_and_free.append(None)
            i +=1
pointer = len(file_and_free) - 1
for i in range(len(file_and_free)):
    if file_and_free[i] == None:
        while file_and_free[pointer] == None:
            pointer -= 1
        file_and_free[i], file_and_free[pointer] = file_and_free[pointer], file_and_free[i]
    if pointer < i:
        file_and_free[i], file_and_free[pointer] = file_and_free[pointer], file_and_free[i]
        pointer = i
        break
for i in range (pointer):
    if file_and_free[i] != None:
        ans += i * file_and_free[i]
print(ans)