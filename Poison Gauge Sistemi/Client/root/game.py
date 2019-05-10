# root/game.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/game.py dosyasını açın ve şu kodu aratın;
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		self.affectShower.BINARY_NEW_AddAffect(type, pointIdx, value, duration)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulActivate(type - chr.NEW_AFFECT_DRAGON_SOUL_DECK1)
		elif chr.NEW_AFFECT_DRAGON_SOUL_QUALIFIED == type:
			self.BINARY_DragonSoulGiveQuilification()

# Altına şu kodları ekleyin;
		elif 209 == type:
			self.playerGauge.RefreshGuageColor("lime")
			self.interface.HPPoisonEffectShow()
			self.interface.PartyPoisonGuageShow()


# Aynı dosyada şu kodu aratın;
	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		self.affectShower.BINARY_NEW_RemoveAffect(type, pointIdx)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulDeactivate()

# Altına şu kodları ekleyin;
		elif 209 == type:
			self.playerGauge.RefreshGuageColor("red")
			self.interface.HPPoisonEffectHide()
			self.interface.PartyPoisonGuageHide()

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)