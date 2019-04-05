/**
 * Server/game/src/char_item.cpp
 * Metin2 4 Envanter Sistemi
 * MMO Tutkunları | www.mmotutkunlari.com | Whistle
 * Kodlandığı Tarih: 07.05.2018
 * Lütfen aşağıdaki adımları sırasıyla uygulayınız.
 */

/**
 * Server/game/src/char_item.cpp dosyasını açın ve IsEmptyItemGrid fonksiyonu içinde şu kodu aratın;
 * Not: Aynı fonksiyonda 2 tane oluyor. 2 sinide göstereceğim şekilde düzenleyin.
 */

					BYTE bPage = bCell / (INVENTORY_MAX_NUM / 2);

// Bu kodu şu şekilde değiştirin;
					BYTE bPage = bCell / (INVENTORY_MAX_NUM / INVENTORY_PAGE_COUNT);

/**
 * Aynı dosya ve fonksiyon içinde şu kodu aratın;
 * Not: Aynı fonksiyonda 2 tane oluyor. 2 sinide göstereceğim şekilde düzenleyin.
 */

						if (p / (INVENTORY_MAX_NUM / 2) != bPage)

// Bu kodu şu şekilde değiştirin;
						if (p / (INVENTORY_MAX_NUM / INVENTORY_PAGE_COUNT) != bPage)

// Bu dosyada düzenlenecekler bu kadardır. Bir sonraki dosyaya geçebilirsiniz. Başarılar. :)
