input_file="aliens.csv"
f = open(input_file)
aliens = f.readlines()
aliensList = []
planetsList = list()
UniquePList=[]
header = True
for line in aliens:
    if not header:
        alien = line.split(",")[0]
        planet = line.split(",")[1].replace("\n","")
        aliensList.append(alien)
        planetsList.append(planet)
    else:
        header = False

for upl in planetsList:
    if upl not in UniquePList:
        UniquePList.append(upl)

output_file="planets.csv"
output=open(output_file,mode="w+")
output.write("species,planet\n")

planet_zerg = []
planet_ho = []
planet_mars = []

for alien in aliensList:
    planet = planetsList[aliensList.index(alien)]
    if planet==UniquePList[0]:
        planet_zerg.append(alien)
    if planet==UniquePList[1]:
        planet_ho.append(alien)
    if planet==UniquePList[2]:
        planet_mars.append(alien)

class Zergalizer:
    def do_zergalization(self, species):
        transformed = list()
        for s in species:
            transformed.append(s.upper())
        output.write(" ".join(transformed)+",zerg\n")
##you can do like parameter output.write(" ".join(transformed)+ "," + UniquePList[0]+ "\n")

class Hoizer:
    def do_hoizification(self, species):
        transformed = list()
        for s in species:
            transformed.append(s+"HO!")
        output.write((" | ").join(transformed)+",ho\n")

class Marsianizer:
    def do_marsianization(self, species):
        transformed = list()
        for s in species:
            transformed.append(" ".join(s.split("."))+"m")
        output.write((" ~~ ").join(transformed)+",mars\n")

Zergalizer().do_zergalization(planet_zerg)
Hoizer().do_hoizification(planet_ho)
Marsianizer().do_marsianization(planet_mars)
output.close()
