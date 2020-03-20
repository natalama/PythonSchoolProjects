from mendeleev import Element,get_session

session = get_session()

#Henter ut ione-radius-data fra mendeleev
ans = session.query(Element).filter(Element.ionic_radii != None).order_by(Element.atomic_number)

for a in ans:
    print(a.symbol, a.name, a.ionic_radii)

#skal fylle data i en dictionarie
#skriv din egen kode her
ionic_dict = {}
for a in ans:
    ionic_dict[a.symbol] = a.ionic_radii
#leser ut ioniske radiuser for allem elementer som har ladning = 2+ og koordinering = VI
#skriv din egen kode her
filtered_ionic_dict = {}
for key in ionic_dict.keys():
    for ionic_radius in ionic_dict[key]:
        if (ionic_radius.charge == 2 and ionic_radius.coordination == 'VI'):
            filtered_ionic_dict[key] = ionic_radius
#printer ut for de 4 elementene vi trenger data for - sjekket med boka at dette stemmer
#skriv din egen kode her
necessary_ionic_dict = {k: v for k, v in filtered_ionic_dict.items() if k in ['Mg', 'Ca', 'Ba', 'Pb']}
print("---------------------------------")
print(necessary_ionic_dict)
