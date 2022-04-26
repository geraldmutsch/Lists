#lets put some cities in a list
cities=['Berlin','Munich','Hamburg']
print (cities)                                      #all cities
print(cities[1])                                    #munich
print(cities[1:])                                   #all except Berlin
cities.append('Nurenberg')                          #add Nurenberg
print(cities)
cities.extend(['Dusseldorf','Cologne'])             #add 2 more
print(cities)
cities.insert(2,'Aachen')                           #add after Munich
print(cities)
MoreCities = ['Bremen','Lübeck']
AllCities = cities + MoreCities
print(AllCities)

#at the doctors waiting room

list_of_patients = ['Bob','Susan','Carl']
for patients in list_of_patients:                       #for all patients in the waiting room
    print('Next Patient: '+ list_of_patients.pop())     #call the patient and get them of the list


