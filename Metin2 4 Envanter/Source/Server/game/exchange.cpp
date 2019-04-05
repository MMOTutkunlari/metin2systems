/**
 * Server/game/src/exchange.cpp
 * Metin2 4 Envanter Sistemi
 * MMO Tutkunları | www.mmotutkunlari.com | Whistle
 * Kodlandığı Tarih: 07.05.2018
 * Lütfen aşağıdaki adımları sırasıyla uygulayınız.
 */
 
// Server/game/src/exchange.cpp açılır ve CheckSpace fonksiyonun içinde şu kod aratılır;
	static CGrid s_grid1(5, INVENTORY_MAX_NUM/5 / 2); // inven page 1
	static CGrid s_grid2(5, INVENTORY_MAX_NUM/5 / 2); // inven page 2

// Şu kodlarla değiştirin;
	static CGrid s_grid1(5, INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT); // inven page 1
	static CGrid s_grid2(5, INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT); // inven page 2
	static CGrid s_grid3(5, INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT); // inven page 3
	static CGrid s_grid4(5, INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT); // inven page 4

/**
 * Not: Arkadaşlar burada 4 tane envanter yapıyoruz. Envanterin her bir sayfası 45 slot içerir. 5 genişlik 9 yüksekliğindedir.
 * Buradaki işlemde de şu oluyor.
 * 180 / 45 => 4 ediyor.
 */

INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT

/**
 * Şöyle bir kod kullandık. Bu kodda şöyle. 180/5/4 => sonuç 9 çıkar. Kısaca biz gride değer eklerken aslında yükseklik ve genişliği ekliyoruz. 5, 9 gibi.
 * Siz 5 envanter yapmak isterseniz.
 * INVENTORY_MAX_NUM bu değeri 225 yapacaksınız ve şöyle bir kod daha ekleyeceksiniz.
 */

	static CGrid s_grid5(5, INVENTORY_MAX_NUM/5 / INVENTORY_PAGE_COUNT); // inven page 5
// Burayı anladığınızı farz ediyorum ve diğer kodlara geçiyorum.

// Aynı dosya ve fonksiyonun içinde şu kodları aratın;
	s_grid1.Clear();
	s_grid2.Clear();

// Altına şunları ekleyin;
	s_grid3.Clear();
	s_grid4.Clear();

// Eğer 5 envanter yapacaksanız şu değeri de eklemelisiniz;
	s_grid5.Clear();

// Gene aynı dosya ve fonksiyonun içinde şu kodları aratın;
	for (i = 0; i < INVENTORY_MAX_NUM / 2; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid1.Put(i, 1, item->GetSize());
	}
	for (i = INVENTORY_MAX_NUM / 2; i < INVENTORY_MAX_NUM; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid2.Put(i - INVENTORY_MAX_NUM / 2, 1, item->GetSize());
	}

// Biz 2 den fazla envanter kullanacağımız için bunu tamamen şu şekilde değiştiriyoruz;
	for (i = 0; i < INVENTORY_PAGE_SLOT_COUNT; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid1.Put(i, 1, item->GetSize());
	}
	for (i = INVENTORY_PAGE_SLOT_COUNT; i < INVENTORY_PAGE_SLOT_COUNT * 2; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid2.Put(i - INVENTORY_PAGE_SLOT_COUNT, 1, item->GetSize());
	}
	for (i = INVENTORY_PAGE_SLOT_COUNT * 2; i < INVENTORY_PAGE_SLOT_COUNT * 3; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid3.Put(i - INVENTORY_PAGE_SLOT_COUNT * 2, 1, item->GetSize());
	}
	for (i = INVENTORY_PAGE_SLOT_COUNT * 3; i < INVENTORY_PAGE_SLOT_COUNT * 4; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid4.Put(i - INVENTORY_PAGE_SLOT_COUNT * 3, 1, item->GetSize());
	}

// 5. Envanteri eklemek için for döngülerine şunu da ekleyin;
	for (i = INVENTORY_PAGE_SLOT_COUNT * 4; i < INVENTORY_PAGE_SLOT_COUNT * 5; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid4.Put(i - INVENTORY_PAGE_SLOT_COUNT * 4, 1, item->GetSize());
	}

/** 
 * Bu kodları eklememizin sebebi ticaret yaptığımız zaman diğer envanterleri de görmesidir.
 * Aksi taktirde diğer envanterler boş olsa bile envanter dolu hatası verir.
 */

// Bu dosyada bitti. Bir sonrakine gecebilirsiniz.
