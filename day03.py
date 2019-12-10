


with open("input.txt") as f:
    input = f.readlines()
    wireOne = [ i.rstrip() for i in input[0].split(",") if i]
    wireTwo = [ i.rstrip() for i in input[1].split(",") if i]

def getPoints(wire):
    xCord = 0
    yCord = 0
    points = [[]]
    startPoint = [0,0]
    points.append(startPoint)
    for move in wire:
        print(move)
        dir = move[:1]
        value = int(move[1:])
        diff = 0
        prevPoint = points[-1]
        if(dir == 'R'):
            diff = abs(prevPoint[0] - value)
            for i in range(diff):
                points.append([prevPoint[0]+i,prevPoint[1]])
        if(dir == 'L'):
            diff = abs(prevPoint[0] - value)
            for i in range(diff):
                points.append([prevPoint[0]-i,prevPoint[1]])
        if(dir == 'U'):
            diff = abs(prevPoint[1] - value)
            for i in range(diff):
                points.append([prevPoint[0],prevPoint[1]+i])
        if(dir == 'D'):
            diff = abs(prevPoint[1] - value)
            for i in range(diff):
                points.append([prevPoint[0],prevPoint[1]-i])

        return points


def getPointsNew(wire):
    points = []
    points.append((0,0))
    for move in wire:
        dir = move[:1]
        value = int(move[1:])
        prevPoint = points[-1]
        if(dir == 'U'):
            diff = abs(prevPoint[1] + value)
            for i in range(0,diff):
                points.append((prevPoint[0],prevPoint[1] + i))
        if(dir == 'D'):
            diff = abs(prevPoint[1] - value)
            for i in range(0,diff):
                points.append((prevPoint[0],prevPoint[1] - i))
        if(dir == 'L'):
            diff = abs(prevPoint[0] - value)
            for i in range(0,diff):
                points.append((prevPoint[0] - 1,prevPoint[1]))
        if(dir == 'R'):
            diff = abs(prevPoint[0] + value)
            for i in range(0,diff):
                points.append((prevPoint[0] + 1,prevPoint[1]))

    return points

wireOnePoints = getPointsNew(wireOne)
wireTwoPoints = getPointsNew(wireTwo)
intersections = [i for i,j in zip(wireOnePoints,wireTwoPoints) if i == j]
print(intersections)
for point in intersections:
    print(abs(0-point[0]) + abs(0-point[1]))
