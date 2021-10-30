## important ! when you have the genenreated key it will be a list and each element of the list is an character



#just put the name of the file that you want to read
def readfile(filetoread):
    file = open(filetoread)
    list_of_lists = []
    for line in file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    return list_of_lists

# it will generate a key in its final form (not usable by the programm directly you have to develllop it with devkey)
def genrndmkey():
    print("generating key")
    import random
    file = readfile("chartable.txt")
    i = 0
    generatedkey = ""
    while i < 16:
        generatedkey = generatedkey + convchar(random.randint(2, len(file)), "output")
        i = i + 1
    return generatedkey

# in normal case you d'ont have to use it it will just convert one character with chartable.txt
def convchar(chartoconv, mode):
    chartable = readfile("chartable.txt")
    c = 0
    if mode == "input":
        while c < len(chartable):
            if chartoconv == str(" "):
                return "pass"
            if (chartable[c])[0] == chartoconv:
                return c + 2
            else:
                c = c + 1
    if mode == "output":
        c = int(chartoconv) - 2
        return (chartable[c])[0]

# it convert a text using convchar
def conv(datatoconv,mode):
    d = 0
    i = 0
    convertedout = []

    while d < len(datatoconv):
        convertedout.append(str(convchar(str(datatoconv[d]), mode)))
        d = d+1
    return convertedout

# it devellop the 16 char key to be usable by the programm
def devkey(keytogen):
    c = 0
    generatedkeyout = []

    while c < 16:
        generatedkeyout.append(str(convchar(str(keytogen[c]), "input")))
        c = c + 1

    return generatedkeyout

# it is the raw encrypting algorythm , you have to give the developped key( a list)
def encrypt(key, dat):
    data = ""
    data = data.join(dat)
    ea = int((key[0]))
    eb = int((key[1]))
    ec = int((key[2]))
    ed = int((key[3]))
    ee = int((key[4]))
    ef = int((key[5]))
    eg = int((key[6]))
    eh = int((key[7]))
    ei = int((key[8]))
    ej = int((key[9]))
    ek = int((key[10]))
    el = int((key[11]))
    em = int((key[12]))
    en = int((key[13]))
    eo = int((key[14]))
    ep = int((key[15]))

    outdat = str(int(en) + int(int(em) * int(int(el) + int(int(ep) * int(int(ej) + int(int(ee) * int(int(ei) + int(int(eh) * int(int(eg) + int(int(ef) * int(int(ek) + int(int(eo) * int(int(ed) + int(int(ec) * int(int(eb) + int(int(ea) * int(data)))))))))))))))))

    return outdat

# it is the raw decrypting algorythm , you have to give the developped key( a list)
def decrypt(key, dat):
    data = ""
    data = str(dat)
    ea = int(key[0])
    eb = int(key[1])
    ec = int(key[2])
    ed = int(key[3])
    ee = int(key[4])
    ef = int(key[5])
    eg = int(key[6])
    eh = int(key[7])
    ei = int(key[8])
    ej = int(key[9])
    ek = int(key[10])
    el = int(key[11])
    em = int(key[12])
    en = int(key[13])
    eo = int(key[14])
    ep = int(key[15])

    outdat = str(int(((((((((((((((((int(data) - int(en)) // em) - int(el)) // ep) - ej) // int(ee)) - ei) // int(eh)) - eg) // int(
        ef)) - ek) // int(eo)) - ed) // int(ec)) - eb) // int(ea))))

    return outdat

# it convert one character for the index using index_chartable.txt
def convcharind(data, mode):
    indchartable = readfile("index_chartable.txt")
    c = 0
    if mode == "input":
        while c < len(indchartable):
            if data == str(" "):
                return "pass"
            if (indchartable[c])[0] == data:
                return c + 10
            else:
                c = c + 1
    if mode == "output":
        c = int(data) - 10
        return (indchartable[c])[0]

# it convert the index with convcharind
def convind(data, mode):
    d = 0
    i = 0
    convertedout = []
    if mode=="input":
        while d < len(data):
            convertedout.append(str(convcharind(data[d], mode)))
            d = d+1

        return convertedout
    if mode =="output":
        while d < len(str(data)):
            convertedout.append(str(convcharind(str(data[d])+str(data[d+1]), mode)))
            d = d+2
        return convertedout

# it encrypt/decrypt the index
def cryptind(key, index, mode):
    c = 0
    output = ""
    if mode=="input":
        indtocrypt = convind(index, mode)

        ind2cry = ""
        ind2cry = ind2cry.join(indtocrypt)
        output = output + str(encrypt(key, str(ind2cry)))

    if mode =="output":
        outpu = ""
        outpu = outpu + str(decrypt(key, str(index)))
        output = convind(outpu, mode)

    return output

# it is a script that does what most user want (you tell what mode , the devellopped key and data and it gives the wanted result)
def crypt(mode, key, dat):
    if mode == "en":
        print ("starting to encrypt")
        output = []
        preconverted = []
        progression = 0
        indexb = []
        data = conv(dat, "input")
        print("data converted")
        while progression < len(data):
            var1 = encrypt(key, data[progression])
            var2 = len(preconverted)
            preconverted.append(var1)
            indexb.append(str(len(var1))+"n")
            progression = progression + 1
        dattofinalcrypt = ""
        dattofinalcrypt = dattofinalcrypt.join(preconverted)
        print("data crypted")
        indexout = ""
        indexout = cryptind(key, indexout.join(indexb), "input")
        print("index crypted")
        return str(dattofinalcrypt) + "i" + str(indexout)


    if mode == "de":
        print ("starting to decrypt")
        output = []
        preconverted = []
        progression = 0
        datalist = dat.split("i")
        cindex = ""
        cindex = cindex.join(datalist[1])
        cdata = ""
        cdata = cdata.join(datalist[0])
        print("index and data separated")
        index = cryptind(key, cindex, "output")
        print("index decrypted and ready to read")
        datatodec = []
        tempdata = ""
        o = 0
        i = ""
        while o < len(index):
            print(o / len(index) * 100,"%")

            if index[o] == "n":
                if i != "":
                    while i != 0:
                        tempdata = tempdata + cdata[progression]
                        progression = progression + 1
                        i = int(i) - 1
                    datatodec.append(decrypt(key,tempdata))
                    tempdata = ""
                o = o + 1
            else:
                i = str(i) + str(index[o])
                o = o + 1
        print("data sucessfully decrypted")
        return conv(datatodec, "output")
