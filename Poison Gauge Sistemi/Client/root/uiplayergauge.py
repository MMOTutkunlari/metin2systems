# root/uiPlayerGauge.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/uiPlayerGauge.py dosyasını açın ve şu kodları aratın;
	def DisableShowAlways(self):
		self.showAlways = False
		self.RefreshGauge()

# Altına şu kodları ekleyin;
	def RefreshGuageColor(self, color):
		self.MakeGauge(100, color)

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)