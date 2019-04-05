# root/interfaceModule.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/interfaceModule.py dosyasını açın ve şu kodları aratın;
	def RefreshStamina(self):
		self.wndTaskBar.RefreshStamina()

# Altına şu kodları ekleyin;
	def HPPoisonEffectShow(self):
		self.wndTaskBar.HPPoisonEffectShow()
	
	def HPPoisonEffectHide(self):
		self.wndTaskBar.HPPoisonEffectHide()


# Aynı dosyada şu kodları aratın;
	def ChangePartyParameter(self, distributionMode):
		self.wndParty.ChangePartyParameter(distributionMode)

# Altına şu kodları ekleyin;
	def PartyPoisonGuageShow(self):
		self.wndParty.PartyPoisonGuageShow()
	
	def PartyPoisonGuageHide(self):
		self.wndParty.PartyPoisonGuageHide()

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)