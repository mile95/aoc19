

with open("input.txt") as f:
    modules = f.readlines()
    modules = [int(x.strip()) for x in modules]

totalFuelReq = 0

for module in modules:
    totalModuleFuel = 0;
    while module > 0:
        currentFuel = int(module/3) - 2
        if(currentFuel > 0):
            totalModuleFuel = totalModuleFuel + currentFuel
        module = currentFuel
    totalFuelReq = totalFuelReq + totalModuleFuel

print(totalFuelReq)
