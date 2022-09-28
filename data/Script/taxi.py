'''
This file is part of OrionAlpha, a MapleStory Emulator Project.
Copyright (C) 2018 Eric Smith <notericsoft@gmail.com>
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


curTown = self.userGetFieldID()
cJob = self.userGetJob()
towns = []

if curTown == 100000000 :
	towns = [["Lith Harbor", 104000000, 80], ["Perion", 102000000, 100], ["Ellinia", 101000000, 100], ["Kerning City", 103000000, 120]]
elif curTown == 101000000 :
	towns = [["Lith Harbor", 104000000, 120], ["Henesys", 100000000, 100], ["Perion", 102000000, 100], ["Kerning City", 103000000, 120]]
elif curTown == 102000000 :
	towns = [["Lith Harbor", 104000000, 120], ["Henesys", 100000000, 100], ["Ellinia", 101000000, 100], ["Kerning City", 103000000, 80]]
elif curTown == 103000000 :
	towns = [["Lith Harbor", 104000000, 120], ["Henesys", 100000000, 100], ["Ellinia", 101000000, 120], ["Perion", 102000000, 80]]
else :  # Lith Harbor
	towns = [["Perion", 102000000, 120], ["Ellinia", 101000000, 120], ["Henesys", 100000000, 80], ["Kerning City", 103000000, 100]]


'This is an example of how to define and use a function with parameters.'
'NOTE: You must ALWAYS DECLARE THE FUNCTION FIRST. That is, define the function above, and call it from below.'
def goTown(mapName, mapNum, fee):
	'Our scripts are stateless - they wait for an async response back from the user before continuing execution.'
	'In this case, we ask the user to select yes or no, and assign that response to ret.'
	ret = self.askYesNo("You don't have anything else to do here, huh? Do you really want to go to #b" + mapName + "#k? It'll cost you #b" + str(fee) + " mesos#k.")
	'If ret is 1 (yes), then we proceed to transfer the user to the selected town.'
	if ret == 1:
		if self.userIncMoney(-fee, True):
			self.registerTransferField(mapNum, "")
		else:
			self.say("I'm afraid you don't have enough money, you'll have to walk.")
	else:
		self.say("There's a lot to see in this town. Come back back when you want to go elsewhere.")

'This continues the global scope and is where the NPC starts execution at.'
self.sayNext("Hi, i'm the Regular Cab. You came to the right place if you want to go to another town fast and secure. Your satisfaction is guaranteed.")
menu = "Choose your destination, the fare leties from place to place.\r\n#b"
'We forloop from i=0, to i=towns.length. In each loop, we append the town selections to menu.'
for i in range(0, len(towns)):
	fare = (towns[i][2] * 10) if cJob != 0 else towns[i][2]
	menu += "#L" + str(i) + "#" + towns[i][0] + " (" + str(fare) + " mesos)#l\r\n"
'Just like we do above in goTown, we assign the response of the menu selection to sel.'
sel = int(self.askMenu(menu))
'Now we make sure the selection response is valid, and proceed to call goTown to move the user.'

if sel in range(0, len(towns)) :
	fare = towns[sel][2] * 10 if cJob != 0 else towns[sel][2]
	goTown(towns[sel][0], towns[sel][1], fare)