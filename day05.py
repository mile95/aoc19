
def compile(text):

    with open(text) as f:
        data = f.readline()
        data = [int(i) for i in data.split(",")]
    pointer = 0

    while(True):
        op = data[pointer]
        modes = '000'
        length = len(str(op))

        if(length > 1):
            modes = str(op)[:-2].zfill(3)
            op = int(str(op)[-2:].replace("0", ""))
        #halt
        if(op == 99):
            break

        #additon or multiplication
        if(op == 1 or op == 2):
            arg1 = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            arg2 = data[pointer + 2] if int(modes[-2]) == 1 else data[data[pointer + 2]]
            savePos = data[pointer + 3]
            if(op == 1):
                data[savePos] = int(arg1) + int(arg2)
            if(op == 2):
                data[savePos] = int(arg1) * int(arg2)
            pointer += 4

        #input
        if(op == 3):
            var = input("Enter a digit: ")
            savePos = data[pointer + 1]
            data[savePos] = var
            pointer += 2

        #ouput
        if(op == 4):
            var = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            print(str(var))
            pointer += 2

        #jump-if-true
        if(op == 5):
            arg1 = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            arg2 = data[pointer + 2] if int(modes[-2]) == 1 else data[data[pointer + 2]]
            if(int(arg1) != 0):
                pointer = arg2
            else:
                pointer += 3

        #jump-if-false
        if(op == 6):
            arg1 = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            arg2 = data[pointer + 2] if int(modes[-2]) == 1 else data[data[pointer + 2]]
            if(int(arg1) == 0):
                pointer = arg2
            else:
                pointer += 3

        #less than
        if(op == 7):
            arg1 = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            arg2 = data[pointer + 2] if int(modes[-2]) == 1 else data[data[pointer + 2]]
            data[data[pointer + 3]] = 1 if int(arg1) < int(arg2) else 0
            pointer += 4

        #equal
        if(op == 8):
            arg1 = data[pointer + 1] if int(modes[-1]) == 1 else data[data[pointer + 1]]
            arg2 = data[pointer + 2] if int(modes[-2]) == 1 else data[data[pointer + 2]]
            data[data[pointer + 3]] = 1 if int(arg1) == int(arg2) else 0
            pointer += 4

compile("input.txt")
