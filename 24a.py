with open("24_val.txt") as fin:
    values = fin.read().strip().split("\n")
    
with open("24_op.txt") as fin:
    op = fin.read().strip().split("\n")

values_dict ={}
ans = 0

for val in values:
    a,b = val.split(': ')
    values_dict[a] = int(b)

is_all_op_done  = 0    
while True:
    is_all_op_done = 0
    for o in op:
        oper, res = o.split(' -> ')
        x,operand,y = oper.split(' ')
        if x in values_dict and y in values_dict:
            if operand == 'AND':
                values_dict[res] = values_dict[x] and values_dict[y]
            if operand == 'OR':
                values_dict[res] = values_dict[x] or values_dict[y]
            if operand == 'XOR':
                values_dict[res] = values_dict[x] ^ values_dict[y]
        else:
            is_all_op_done += 1
    print(is_all_op_done)
    if is_all_op_done == 0:
        break
    
for key, val in values_dict.items():
    if key.startswith('z'):
        ans += val*(2**(int(key[1:])))
        print(key,val)
        
print(ans)