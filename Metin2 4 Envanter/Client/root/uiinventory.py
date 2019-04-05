# root/uiInventory.py
# Metin2 4 Envanter Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle
# Kodlandığı Tarih: 07.05.2018
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# Root/uiInventory.py dosyasını açın ve şu kodları aratın;
			self.inventoryTab = []
			self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))

# Altına şunları ekleyin;
			self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_04"))

# Aynı dosyada şu kodları aratın;
		self.inventoryTab[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
		self.inventoryTab[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))

# Altına şunları ekleyin;
		self.inventoryTab[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
		self.inventoryTab[3].SetEvent(lambda arg=3: self.SetInventoryPage(arg))

# Aynı dosyada şu kodları aratın;
		self.inventoryTab[0].Down()

# Altına şunları ekleyin;
		self.inventoryPageIndex = 0

# Aynı dosyada SetInventoryPage fonksiyonun içindeki şu kodları aratın;
		self.inventoryPageIndex = page
		self.inventoryTab[1-page].SetUp()
		self.RefreshBagSlotWindow()

# Şu şekilde değiştirin;
		self.inventoryTab[self.inventoryPageIndex].SetUp()
		self.inventoryPageIndex = page
		self.inventoryTab[self.inventoryPageIndex].Down()
		self.RefreshBagSlotWindow()
# Bu kod sayesinde diğer sayfalara geçerken butonlar takılı kalmayacak.

# Aynı dosyada RefreshBagSlotWindow fonksiyonunun içinde şu kodları aratın;
				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE

# Şu şekilde değiştirin;
				if slotNumber >= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex:
					slotNumber -= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex
# Bu kod sayesinde 3 ve 4 envanterde yer alan otomatik potlar çalışacak,
# efsun botları da efsunu görecektir.

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)

