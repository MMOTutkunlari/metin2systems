# root/uiTaskbar.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/uiTaskbar.py dosyasını açın ve şu kodu aratın;
		self.mouseModeButtonList = [ ui.ScriptWindow("TOP_MOST"), ui.ScriptWindow("TOP_MOST") ]

# Altına şu kodu ekleyin;
		self.poisonEffect = 0


# Aynı dosyada şu kodu aratın;
		self.spRecoveryGaugeBar = self.GetChild("SPRecoveryGaugeBar")

# Altına şu kodları ekleyin;
		self.hpPoisonGauge = self.GetChild("HPPoisonGauge")
		self.hpPoisonRecoveryGaugeBar = self.GetChild("HPPoisonRecoveryGaugeBar")
		
		self.hpPoisonGauge.Hide()
		self.hpPoisonRecoveryGaugeBar.Hide()


# Aynı dosyada şu kodları aratın;
		self.spRecoveryGaugeBar = None

# Altına şu kodları ekleyin;
		self.hpPoisonGauge = None
		self.hpPoisonRecoveryGaugeBar = None
		self.poisonEffect = 0


# Aynı dosyada şu kodları aratın;
	def RefreshSkill(self):
		self.curSkillButton.RefreshSkill()
		for button in self.selectSkillButtonList:
			button.RefreshSkill()

# Altına şu kodları ekleyin;
	def HPPoisonEffectShow(self):
		self.poisonEffect = 1
		self.hpGauge.Hide()
		self.hpPoisonGauge.Show()
		
	def HPPoisonEffectHide(self):
		self.poisonEffect = 0
		self.hpPoisonGauge.Hide()
		self.hpGauge.Show()


# Aynı dosyada şu kodları aratın;
	def SetHP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.hpGauge.SetPercentage(curPoint, maxPoint)
			self.tooltipHP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_HP, curPoint, maxPoint))

			if 0 == recoveryPoint:
				self.hpRecoveryGaugeBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_WIDTH * (float(destPoint) / float(maxPoint)))
				self.hpRecoveryGaugeBar.SetSize(newWidth, self.GAUGE_HEIGHT)
				self.hpRecoveryGaugeBar.Show()

# Aşağıdaki kodlarla değiştiriniz;
	def SetHP(self, curPoint, recoveryPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.hpGauge.SetPercentage(curPoint, maxPoint)
			self.hpPoisonGauge.SetPercentage(curPoint, maxPoint)
			self.tooltipHP.SetText("%s : %d / %d" % (localeInfo.TASKBAR_HP, curPoint, maxPoint))

			if 0 == recoveryPoint:
				self.hpRecoveryGaugeBar.Hide()
				self.hpPoisonRecoveryGaugeBar.Hide()
			else:
				destPoint = min(maxPoint, curPoint + recoveryPoint)
				newWidth = int(self.GAUGE_WIDTH * (float(destPoint) / float(maxPoint)))
				
				if self.poisonEffect == 0:
					if self.hpPoisonRecoveryGaugeBar.IsShow():
						self.hpPoisonRecoveryGaugeBar.Hide()
					self.hpRecoveryGaugeBar.SetSize(newWidth, self.GAUGE_HEIGHT)
					self.hpRecoveryGaugeBar.Show()
				else:
					if self.hpRecoveryGaugeBar.IsShow():
						self.hpRecoveryGaugeBar.Hide()
					self.hpPoisonRecoveryGaugeBar.SetSize(newWidth, self.GAUGE_HEIGHT)
					self.hpPoisonRecoveryGaugeBar.Show()

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)