
# To help check with validity of input
key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']
gedcom_file = open('Frank DiGiacomo.ged', 'r')


f = open("output.txt", "w")
for input in gedcom_file:
    input_array = input.split()
    input_tag = input_array[1].strip()
    input_level = input_array[0].strip()

    valid = "N"
    arguments = input_array[-len(input_array) + 2:]
    arguments_string = ''.join(str(x + " ") for x in arguments)

    if input_tag in key_words:
        valid = "Y"

    output = "<-- " + input_level + "|" + input_tag + "|" + valid + "|" + arguments_string + "\n"
    string_input = "--> " + input
    print (string_input)
    print(output, "\n")

    f.write(string_input)
    f.write(output)
f.close()