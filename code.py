def run_brainfuck(incode, input_data=""):
    memory = [0] * 256
    pointer = 0
    output = ""
    input_index = 0
    i = 0

    incode = incode.replace(" ", "").replace("\n", "")  #remove spaces and moves to one string
    deincode = [incode[i:i + 2] for i in range(0, len(incode), 2)] #move 2 symbols from string incode to array deincode
    deincode = [">" if x == "♠♦" else x for x in deincode]#replace ♠♦ to >
    deincode = ["<" if x == "♦♠" else x for x in deincode]#replace ♦♠ to <
    deincode = ["+" if x == "♠♠" else x for x in deincode]#replace ♠♠ to +
    deincode = ["-" if x == "♥♥" else x for x in deincode]#replace ♥♥ to -
    deincode = ["." if x == "♥♠" else x for x in deincode]#replace ♥♠ to .
    deincode = ["," if x == "♠♥" else x for x in deincode]#replace ♠♥ to ,
    deincode = ["[" if x == "♥♦" else x for x in deincode]#replace ♥♦ to [
    deincode = ["]" if x == "♦♥" else x for x in deincode]#replace ♦♥ to ]

    outcode = ''.join(deincode)#outcode is string from deincode

    while i < len(outcode):
        command = outcode[i]

        if command == '>':
            pointer = (pointer + 1) % 256

        elif command == '<':
            pointer = (pointer - 1) % 256

        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256

        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256

        elif command == '.':
            output += chr(memory[pointer])

        elif command == ',':
            if input_index < len(input_data):
                memory[pointer] = ord(input_data[input_index])
                input_index += 1
            else:
                memory[pointer] = 0

        elif command == '[':
            if memory[pointer] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    if outcode[i] == '[':
                        loop += 1
                    elif outcode[i] == ']':
                        loop -= 1

        elif command == ']':
            if memory[pointer] != 0:
                loop = 1
                while loop > 0:
                    i -= 1
                    if outcode[i] == ']':
                        loop += 1
                    elif outcode[i] == '[':
                        loop -= 1

        i += 1

    return output
if __name__ == "__main__":
    a = run_brainfuck("""♠ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♦ ♥ ♥ ♦ ♥ 
    ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♥ ♠ ♠ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♥ ♦ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♦ 
    ♥ ♥ ♦ ♥ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♠ 
    ♥ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♠ ♠ ♦ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ 
    ♦ ♠ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
    ♥ ♥ ♥ ♥ ♠ ♦ ♥ ♥ ♦ ♥ ♦ ♠ ♠ ♠ ♠ ♠ 
    ♥ ♠ ♠ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♥ ♦ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♦ ♥ ♥ ♦ ♥ ♦ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♠ ♠ ♦ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ ♦ ♠ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♦ ♥ ♥ ♦ ♥ ♦ ♠ ♥ ♥ ♥ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♠ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
    ♥ ♥ ♥ ♥ ♥ ♠ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♠ ♠ ♦ ♠ ♠ ♠ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ ♦ ♠ 
    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
    ♥ ♥ ♠ ♦ ♥ ♥ ♦ ♥ ♦ ♠ ♥ ♥ ♥ ♥ ♥ ♥ 
    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♠ ♠ ♦ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♥ ♦ ♦ ♠ ♠ ♠ 
    ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♦ ♥ ♥ ♦ ♥ ♦ ♠ 
    ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♠""" ) #Hello world on braincard
    print(a)