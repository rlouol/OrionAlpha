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
Script: 시험 장소인 전사의 바위산에서 검은 구슬 30개 모으기
'''
 
if (self.userGetJob() == 100 and self.userGetLevel() >= 30):
	if (self.inventoryGetItemCount(4031013) >= 30):
		self.sayNext("Ohhhhh...you collected all 30 Dark Marbles!! It should have been difficult...just incredible! You've passed the test and for that, I'll reward you #bThe Proof of a Hero#k. Take that and go back to Perion.")
		nBlack = self.inventoryGetItemCount(4031013)
		ret = self.inventoryExchange(0, 4031013, -nBlack, 4031008, -1, 4031012, 1)
		if (not ret):
			self.say("Please, check whether or not you have room in your Etc inventory.")
		else:
			self.registerTransferField(102020300, "")
	else:
		nRet = self.askYesNo("What's going on? Doesn't look like you have collected 30 #bDark Marbles#k, yet...If you're having problems with it, then you can leave, come back and try it again. So...do you want to give up and get out of here?")
		if (nRet == 0):
			self.sayNext("That's right! Stop acting weak and start collecting the marbles. Talk to me when you have collected 30 #bDark Marbles#k.")
		elif (nRet == 1):
			self.sayNext("Really... alright, I'll let you out. Please don't give up, though. You can always try again, so do not give up. Until then, bye...")
			self.registerTransferField(102020300, "")
else:
	self.sayNext("What are you doing here? This is for warriors who are ready for advancement.")
	self.registerTransferField(102020300, "")
