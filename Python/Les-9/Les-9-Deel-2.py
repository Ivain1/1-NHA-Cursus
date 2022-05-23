F = open("testbestand.txt","r+")
F.seek(0)
print(F.read())
F.close()