readFile = open("infile", mode="r")
writeFile = open("outfile", mode="w")

for line in readFile:  # iterate over file's lines
    xString, yString = line.split()  # split the line
    x = float(xString); y = float(yString)
    print("x = %s, y = %s"%(x, y))
    writeFile.write("%s * %s = %s\n"%(x, y, x*y))

readFile.close(); writeFile.close()
