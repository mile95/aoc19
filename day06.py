

with open("input.txt") as f:
    map = f.readlines()
    map = [(x.strip()) for x in map]

nodes = {}

for x in map:
    leftNode = x.split(")")[0]
    rightNode = x.split(")")[1]

    if rightNode not in nodes:
        nodes[rightNode] = []

    nodes[rightNode].append(leftNode)

sum = 0
for node in nodes:
    for subNode in nodes[node]:
        if subNode in nodes.keys():
            nodes[node].extend(x for x in nodes[subNode] if x not in nodes[node])
    sum += len(nodes[node])

print(sum)
