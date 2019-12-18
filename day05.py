

def readInput():
    with open("input.txt") as f:
        input = f.readline()
        input = [int(i) for i in input.split(",")]
        return input

while (True):
    ins = readInput()
    pointer = 0
    while(True):
        opCode = ins[pointer]
        length = len(str(opCode))
        params = '0'
        if(length > 2):
            instruction = str(opCode)[-2:]
            params = (str(opCode)[:length -2])
        else:
            instruction = opCode
        if(int(instruction) == 99):
            exit()
            break
        if(int(instruction) == 1):
            arg1 = ins[pointer + 1] if int(params[:1]) == 1 else ins[ins[pointer + 1]]
            arg2 = ins[pointer + 2] if int(params[:2]) == 1 else ins[ins[pointer + 2]]
            savePos = ins[pointer + 3]
            ins[savePos] = arg1 + arg2
            pointer += 4
        if(int(instruction) == 2):
            arg1 = ins[pointer + 1] if int(params[:1]) == 1 else ins[ins[pointer + 1]]
            arg2 = ins[pointer + 2] if int(params[:2]) == 1 else ins[ins[pointer + 2]]
            savePos = ins[pointer + 3]
            ins[savePos] = arg1 * arg2
            pointer += 4
        if(int(instruction) == 3):
            var = input("Enter a digit:")
            savePos = ins[pointer + 1]
            ins[savePos] = var
            pointer += 2
        if(int(instruction) == 4):
            var = ins[ins[pointer+1]]
            print(var)
            pointer += 2
