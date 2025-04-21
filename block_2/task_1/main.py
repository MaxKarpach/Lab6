i_file = open("input.txt", "r")
template = i_file.readline()
line = i_file.readline()

if line != '':
    o_file = open("output.txt", "w")
    template = template[:-1]
    counter = 0
    template_indexes = ""
    for i in range((len(line) + 1) - len(template)):
        if line[i:(i+len(template))] == template:
            counter += 1
            template_indexes += str(i+1) + ' '
    o_file.write(str(counter) + '\n' + template_indexes)
    o_file.close()

i_file.close()