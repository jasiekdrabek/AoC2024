ans = 0
files=[]
free=[]
file_and_free = []
with open('9.txt', 'r') as file:
    i = 0
    pos = 0
    file_id = 0
    for line in file:
        line.strip()
        for d in line:
            if i % 2 == 0:
                files.append((pos,int(d),file_id))
                for j in range(int(d)):
                    file_and_free.append(file_id)
                    pos += 1
                file_id += 1 
            else:
                free.append((pos,int(d)))
                for j in range(int(d)):
                    file_and_free.append(None)
                    pos += 1
            i +=1
for (file_pos,file_size,file_id) in reversed(files):
    for i,(free_pos,free_size) in enumerate(free):
        if file_pos < free_pos:
            break
        else:
            if(free_size >= file_size and file_size > 0):
                for j in range (file_size):
                    file_and_free[file_pos + j] = None
                    file_and_free[free_pos + j] = file_id
                free[i] = (free_pos + file_size, free_size - file_size)
                break
                    
for i in range (len(file_and_free)):
    if file_and_free[i] != None:
        ans += i * file_and_free[i]
print(ans)