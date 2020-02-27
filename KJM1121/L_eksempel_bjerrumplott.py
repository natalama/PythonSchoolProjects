# -*-coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

'''
Funksjonen "polyprotic_acid" ble brukt til å lage alle plottene til del 1 av
oppgave 1.3. Funksjonen beregner de relative konsentrasjonene til syren og
dens protolyserte specier versus pH. Du kan gjenbruke denne funksjonen for å
løse del 2 av oppgave 1.3. Sett da a0 (H2S), a1 (HS-) og a2 (S2-). a3 skal
ikke brukes.

Det finnes flere måtes å løse dette problemet.
Én mulighet er å slette a3 fra funksjonen. Da må du huske å slette den
alle steder den forekommer (husk: Ka1Ka2Ka3/p = a3).
En annen mulighet er å sette Ka3 = 0. Da blir leddet som tilsvarer a3 i
utregningen av a0 lik 0. a3 vil bli returnert som et tomt array.
'''

def polyprotic_acid(pH, Ka1, Ka2, Ka3):
	p = 10**(-pH)    						# p = [H+]  (proton)
	a0 = 1/(1 + Ka1/p + Ka1*Ka2/p**2 + Ka1*Ka2*Ka3/p**3)
	a1 = a0*Ka1/p
	a2 = a1*Ka2/p
	a3 = a2*Ka3/p
	return a0, a1, a2, a3

'''
Under er et eksempel på bruk av "polyprotic_acid"
N er antall beregnede datapunkt. Det er ikke så nøye hvor stort dette tallet er,
men det må være stort nok til å få jevne kurver.
Juster intervallet på x-aksen ved å endre på pH-start og pH-stop.
'''

N = 400
start_pH = 1e-5
stop_pH = 14
pH = np.linspace(start_pH, stop_pH, N)
Ka1 = 1.1e-7
Ka2 = 1e-14
Ka3 = 0
"""H3SO4,"""
H2S, HS, S = polyprotic_acid(pH, Ka1, Ka2, Ka3)

'''
Under angis et eksempel på kode til plotting. Det som må være med er:
- alle specier i samme plott
- labels (legend)
- tittel (skal inneholde ditt navn)
- navn på aksene (x = pH, y = alpha, slik som vist under)
Ellers kan du legge til andre kommandoer om du synes det er fornuftig.

Merk at labels i eksempelet under bruker $ for å merke begynnelsen og slutten
på en matematisk formel. Du kan også skrive på formen H2M, HM(-),M(2-) i stedet.
Husk å ta med eventuell ladning.

For å få et tydeligere plott kan du gjerne bruke kommandoer for å gjøre skriften større.
Slik kan du gjøre for å få tallene på aksene større:
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
Du kan bestemme skriftstørrelsen til plt.title, plt.xlabel, plt.ylabel, og plt.legend
ved å legge ved fontsize=STØRRELSE som argument. Slik kan dette gjøres:
	plt.legend(loc="best",fontsize=15)
Du kan også få tydeligere linjer i plottet ved å presisere linjebredde slik:
	plt.plot(pH, H3AsO4, linewidth=2, label='$H_{3}AsO_{4}$')


Merk, det er bra å kommentere koden, men pass på å aldri ha kommentarer som
inneholder æ, ø og å i samme linje som du bruker matplotlib.
'''

plt.plot(pH, H2S, label='$H_{2}S$')
plt.plot(pH, HS, label='$HS^{1-}$')
plt.plot(pH, S, label='$S^{2-}$')
#plt.plot(pH, AsO4, label='$AsO_{4}^{3-}$')
plt.legend()
plt.axis([start_pH, stop_pH, -0.01, 1.01])
plt.title("MITT NAVN, Arsensyre")
plt.ylabel(r'$\alpha $')
plt.xlabel('pH')
plt.savefig("lab1_KJM1121.png", bbox_inches='tight')
plt.show()
