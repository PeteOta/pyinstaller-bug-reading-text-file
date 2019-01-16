filePath = "C:\\Users\\Pedro\\Documents\\Achilles\\TOW_calc\\Pedro.txt"
with open(filePath,"r") as fileStream: # these options do not work: ,errors="surrogateescape" ,encoding='ISO-8859-1' ('latin-1' 'ASCII'
        firstLineIn = fileStream.readline()
print ("firstLineIn = " + firstLineIn)