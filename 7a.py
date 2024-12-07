grid = []
ans = 0
with open('7.txt', 'r') as file:
    for line in file:
        line = line.strip()
        target, components = line.split(": ")
        target = int(target)
        components = [int(x) for x in components.split(" ")]
        possible_results = [components[0]]
        for i in range(1,len(components)):
            new_possible_results = []
            for res in possible_results:
                if res + components[i] <= target:
                    new_possible_results.append(res + components[i])
                if res * components[i] <= target:
                    new_possible_results.append(res * components[i])
            possible_results = new_possible_results
        if target in possible_results:
            ans += target
print(ans)