# root/uiParty.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/uiParty.py dosyasını açın ve PartyMemberInfoBoard sınıfı içindeki şu kodları aratın;
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.pid = None
		self.vid = None

# Altına şu kodu ekleyin;
		self.poison = 0


# Aynı dosyada şu kodu aratın;
			self.gauge = self.GetChild("Gauge")

# Altına şu kodu ekleyin;
			self.poisonGauge = self.GetChild("PoisonGauge")


# Aynı dosyada PartyMemberInfoBoard sınıfı içindeki __LoadBoard() fonksiyonu içindeki şu kodları aratın;
		self.__SetAffectsMouseEvent()
		self.__HideAllAffects()

# Altına şu kodu ekleyin;
		self.poisonGauge.Hide()


# Aynı dosyada şu kodu aratın;
		self.gauge = None

# Altına şu kodu ekleyin;
		self.poisonGauge = None


# Aynı dosyada şu kodları aratın;
	def SetCharacterHP(self, hpPercentage):
		hpPercentage = max(0, hpPercentage)
		self.gauge.SetPercentage(hpPercentage, 100)

# Altına şu kodları ekleyin;
		self.poisonGauge.SetPercentage(hpPercentage, 100)
	
	def UpdatePoisonGauge(self, arg):
		self.poison = arg
		if self.poison == 1:
			if self.gauge.IsShow():
				self.gauge.Hide()
			self.poisonGauge.Show()
		else:
			if self.poisonGauge.IsShow():
				self.poisonGauge.Hide()
			self.gauge.Show()


# Aynı dosyada şu kodları aratın;
	def Unlink(self):
		self.vid = None
		self.nameTextLine.SetPackedFontColor(self.UNLINK_COLOR)
		self.gauge.Hide()

# Altına şu kodları ekleyin;
		self.poisonGauge.Hide()


# Aynı dosyada şu kodları aratın;
	def __FindPartyMemberInfoBoardByPID(self, pid):
		for board in self.partyMemberInfoBoardList:
			if pid == board.GetCharacterPID():
				return board

		return None

# Altına şu kodları ekleyin;
	def __FindPartyMemberInfoBoardByName(self, name):
		for board in self.partyMemberInfoBoardList:
			if name == board.GetCharacterName():
				return board
		
		return None


# Aynı dosyada şu kodları aratın;
	def ChangePartyParameter(self, distributionMode):
		self.partyMenu.ChangePartyParameter(distributionMode)

# Altına şu kodları ekleyin;
	def PartyPoisonGuageShow(self):
		board = self.__FindPartyMemberInfoBoardByName(player.GetName())
		if None == board:
			return

		board.UpdatePoisonGauge(1)
	
	def PartyPoisonGuageHide(self):
		board = self.__FindPartyMemberInfoBoardByName(player.GetName())
		if None == board:
			return

		board.UpdatePoisonGauge(0)


# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)