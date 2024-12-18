output = ''
operands = []
instructions = []
A = 0
B = 0
C = 0

with open('17.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == '':
            continue
        if line.startswith("Register A"):
            _, A = line.split(': ')
            A = int(A)
        elif line.startswith("Register B"):
            _, B = line.split(': ')
            B = int(B)
        elif line.startswith("Register C"):
            _, C = line.split(': ')
            C = int(C)
        else:
            _, line = line.split(': ')
            line = line.split(',')
            for i,number in enumerate(line):
                if i % 2 == 0:
                    instructions.append(int(number))
                else:
                    operands.append(int(number))
                    
pointer = 0
while pointer < len(instructions):
    combo_operand = operands[pointer]
    if operands[pointer] == 4:
        combo_operand = A
    elif operands[pointer] == 5:
        combo_operand = B
    elif operands[pointer] == 6:
        combo_operand = C
    if instructions[pointer] == 0:#adv
        A = A // (2**combo_operand)
    elif instructions[pointer] == 1:#bxl
        B = B ^ operands[pointer]
    elif instructions[pointer] == 2:#bst
        B = combo_operand % 8
    elif instructions[pointer] == 3:
        if A != 0: #jnz
            pointer = operands[pointer]
            continue
    elif instructions[pointer] == 4: #bxc
        B = B ^ C
    elif instructions[pointer] == 5: #out
        output += ',' + str(combo_operand%8)
    elif instructions[pointer] == 6:#bdv
        B = A // 2**combo_operand
    elif instructions[pointer] == 7:#cdv
        C = A // 2**combo_operand
    pointer += 1
    
output = output[1:]
print(output, A, B, C)
            