


with open("input.txt") as f:
    input = f.readlines()
    wireOne = [ i.rstrip() for i in input[0].split(",") if i]
    wireTwo = [ i.rstrip() for i in input[1].split(",") if i]

def getPoints(wire):
    points = []
    points.append((0,0))
    for move in wire:
        dir = move[:1]
        value = int(move[1:])
        if(dir == 'U'):
            for _ in range(value):
                prevPoint = points[-1]
                points.append((prevPoint[0],prevPoint[1] + 1))
        if(dir == 'D'):
            for _ in range(value):
                prevPoint = points[-1]
                points.append((prevPoint[0],prevPoint[1] - 1))
        if(dir == 'L'):
            for _ in range(value):
                prevPoint = points[-1]
                points.append((prevPoint[0] - 1,prevPoint[1]))
        if(dir == 'R'):
            for _ in range(value):
                prevPoint = points[-1]
                points.append((prevPoint[0] + 1,prevPoint[1]))
    return points

wireOnePoints = getPoints(wireOne)
wireTwoPoints = getPoints(wireTwo)
intersections = set(wireOnePoints) & set(wireTwoPoints)
intersections.remove((0,0))
print(min(abs(x)+abs(y) for (x, y) in intersections)) #Part 1
distances = [wireOnePoints.index(intersection) + wireTwoPoints.index(intersection) for intersection in intersections]
print(min(distances)) # Part 2
