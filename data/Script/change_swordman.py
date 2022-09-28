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

'''
Author: rlouol
NPC: Warrior Job Instructor
Script: 전사 2차 전직 교관
'''

import math
import random

if (self.userGetJob() == 100 and self.userGetLevel() >= 30):
	nBlack = self.inventoryGetItemCount(4031013)
	if (self.inventoryGetItemCount(4031008) >= 1):
		if (nBlack == 0):
			self.sayNext("Hmmm...it is definitely the letter from #bDances with Balrog#k... so you came all the way here to take the test and make the 2nd job advancement as the warrior. Alright, I'll explain the test to you. Don't sweat it too much, it's not that complicated.")
			self.sayNext("I'll send you to a hidden map. You'll see monsters you don't normally see. They look the same like the regular ones, but with a totally different attitude. They neither boost your experience level nor provide you with item.")
			self.sayNext("You'll be able to acquire a marble called #bDark Marbles#k while knocking down those monsters. It is a special marble made out of their sinister, evil minds. Collect 30 of those, then go talk to a colleague of mine in there. That's how you pass the test.")
			nRet = self.askYesNo("Once you go inside, you can't leave until you take care of your mission. If you die, your experience level will decrease...so you better really buckle up and get ready...well, do you want to go for it now?")
			if (nRet == 0):
				self.sayNext("You don't seem too prepared for this. Find me when you ARE ready. There are neither portals or stores inside, so you better get 100% ready for it.")
			elif (nRet == 1):
				self.sayNext("Alright I'll let you in! Defeat the monsters inside, collect 30 Dark Marbles, then strike up a conversation with a colleague of mine inside. It'll give you the #bDark Marble#k, the proof that you've passed the test. Best of luck to you.")
				aMap = [108000300, 108000301, 108000302]
				self.registerTransferField(aMap[int(math.floor(random.random() * len(aMap)))], "")
		elif (nBlack > 0):
			nRet = self.askYesNo("So you've given up in the middle of this before. Don't worry about it, because you can always retake the test. Now...do you want to go back in and try again?")
			if (nRet == 0):
				self.sayNext("You don't seem too prepared for this. Find me when you ARE ready. There are neither portals or stores inside, so you better get 100% ready for it.")
			elif (nRet == 1):
				self.sayNext("Alright! I'll let you in! Sorry to say this, but I have to take away all your marbles beforehand. Defeat the monsters inside, collect 30 Dark Marbles, then strike up a conversation with a colleague of mine inside. It'll give you the #bDark Marble#k, the proof that you've passed the test. Best of luck to you.")
				self.inventoryExchange(0, 4031013, -nBlack)
				aMap = [108000300, 108000301, 108000302]
				self.registerTransferField(aMap[int(math.floor(random.random() * len(aMap)))], "")
	else:
		self.sayNext("Do you want to be a stronger warrior? Let me take care of that for you, then. You look definitely qualified for it. For now, go see #bDances with Balrog#k of Perion first.")
elif (self.userGetJob() == 100 and self.userGetLevel() < 30):
	self.sayNext("Do you want to become a much stronger Warrior than you already are? Let me take care of that, then, but... you look #Gweak... #ktoo weak.. Start training, become more #Gpowerful. #kPowerful and then come back here.")
elif (self.userGetJob() == 110 or self.userGetJob() == 120 or self.userGetJob() == 130):
	self.sayNext("Hmm... you were the one who passed my test the other day! What do you think? Did it become stronger? Good! Now I can definitely notice his Warrior bearing.")
