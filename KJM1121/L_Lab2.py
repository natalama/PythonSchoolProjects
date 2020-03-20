from mendeleev import Element,get_session

# I had to follow the instruction given in the comments in this program unfortunately.
# I would have gotten only the most necessary ions and the required data! -_-

session = get_session()

#Henter ut ione-radius-data fra mendeleev
ans = session.query(Element).filter(Element.ionic_radii != None).order_by(Element.atomic_number)

for a in ans:
    print(a.symbol, a.name, a.ionic_radii)

element_symbols_needed = ['Mg', 'Ca', 'Ba', 'Pb']
#skal fylle data i en dictionarie
#skriv din egen kode her
ionic_dict = {a.symbol : a.ionic_radii for a in ans}
#leser ut ioniske radiuser for allem elementer som har ladning = 2+ og koordinering = VI
#skriv din egen kode her
filtered_ionic_dict = {}
for key in ionic_dict.keys():
    for ionic_radius in ionic_dict[key]:
        if (ionic_radius.charge == 2 and ionic_radius.coordination == 'VI'):
            filtered_ionic_dict[key] = ionic_radius
#printer ut for de 4 elementene vi trenger data for - sjekket med boka at dette stemmer
#skriv din egen kode her
necessary_ionic_dict = {k: v for k, v in filtered_ionic_dict.items() if k in element_symbols_needed}
print("------------Fire elementene vi trenger data for---------------------")
print(necessary_ionic_dict)
