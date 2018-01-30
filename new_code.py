f = open('C:/Python_Workspace/aliens.csv')
input_line = f.readlines()
tab_alien_planet=[]
header = True
#Loading csv into list of list (tab_alien_planet)
for i in input_line:
    if not header:
        alien=""
        planet=""
        rec_alien_planet=[]
        
        alien = i.split(",")[0]
        planet = i.split(",")[1].replace("\n","")
        
        rec_alien_planet.append(alien)
        rec_alien_planet.append(planet)
        
        tab_alien_planet.append(list(rec_alien_planet))
    else:
        header = False

output=open('planets.csv',mode="w")
output.write("species,planet\n")

#Sort the list of list (tab_alien_planet) and store into tab_alien_planet_sort
tab_alien_planet_sort = sorted(tab_alien_planet, key=lambda x:(x[1]))

prev_alien=tab_alien_planet_sort[0][0]
prev_planet=tab_alien_planet_sort[0][1]
alien_list_to_write=[]

for i in tab_alien_planet_sort:
   curr_alien=i[0]
   curr_planet=i[1]
   
   if curr_planet==prev_planet:
      alien_list_to_write.append(curr_alien)
   else:
      output.write(("|").join(alien_list_to_write)+","+prev_planet+"\n") #write into file
      alien_list_to_write=[]
      alien_list_to_write.append(curr_alien)
      
   prev_alien=curr_alien
   prev_planet=curr_planet
   
output.write(("|").join(alien_list_to_write)+","+prev_planet+"\n") #write into file
