/**
 * Server/common/lenght.h
 * Metin2 4 Envanter Sistemi
 * MMO Tutkunları | www.mmotutkunlari.com | Whistle
 * Kodlandığı Tarih: 07.05.2018
 * Lütfen aşağıdaki adımları sırasıyla uygulayınız.
 */
 
// Sırasıyla şu işlemleri uygulayınız;
// Server/common/lenght.h açılır ve aratılır;
	INVENTORY_MAX_NUM		= 90,

// Şu kodlarla değiştirin;
	INVENTORY_MAX_NUM		= 180,
	INVENTORY_PAGE_COUNT	= INVENTORY_MAX_NUM / 45,
	INVENTORY_PAGE_SLOT_COUNT = INVENTORY_MAX_NUM / INVENTORY_PAGE_COUNT,

// Bu dosyada bitti bir sonrakine geçebilirsiniz.
