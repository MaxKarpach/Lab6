def substr_check(substr, base):
    counter = 0
    for i in range(len(base)):
        if substr[i] != base[i]:
            counter+=1
    return counter

def line_check(line):
    line_list = line.split()
    misses = int(line_list[0])
    line_base = line_list[1]
    template = line_list[2]
    template_counter = 0
    template_indexes = ""
    for i in range((len(line_base) + 1) - len(template)):
        if substr_check(line_base[i:(i+len(template))], template) <= misses:
            template_counter += 1
            template_indexes += str(i) + ' '
    return str(template_counter) + ' ' + template_indexes

i_file = open("input.txt", "r")
line = i_file.readline()

o_file = open("output.txt", "w")
while line != "":
    o_file.write(line_check(line) + "\n")
    line = i_file.readline()
o_file.close()

i_file.close()