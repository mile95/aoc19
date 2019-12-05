

def readInput():
    with open("input.txt") as f:
        input = f.readline()
        input = [int(i) for i in input.split(",")]
        return input

noun = 0
verb = 0
while (True):
    input = readInput()
    input[1] = noun
    input[2] = verb
    pointer = 0
    while(True):
        opCode = input[pointer]
        if(opCode == 99):
            break
        arg1 = input[input[pointer + 1]]
        arg2 = input[input[pointer + 2]]
        savePos = input[pointer + 3]
        if(opCode == 1):
            input[savePos] = arg1 + arg2
        if(opCode == 2):
            input[savePos] = arg1 * arg2
        pointer += 4
    if(input[0] == 19690720):
        print("Noun: " + str(noun))
        print("Verb: " + str(verb))
        print(100*noun + verb)
        break;
    if(noun == 99):
        noun = 0
        verb = verb + 1
    else:
        noun = noun + 1
