# UIScript/tasbar.py veya locale/xx/ui/taskbar.py
# Casro2 Poison Guage Sistemi
# MMO Tutkunları | www.mmotutkunlari.com | Whistle | Casro2 | www.casro2.com
# Kodlandığı Tarih: 08.02.2019 - 16:44
# Lütfen aşağıdaki adımları sırasıyla uygulayınız.

# UIScript/taskbar.py veya locale/xx/ui/taskbar.py dosyasını açın ve en alta şu kodları ekleyin;
window["children"][1]["children"][2]["children"] = window["children"][1]["children"][2]["children"] + (
				{
					"name" : "HPPoisonRecoveryGaugeBar",
					"type" : "bar",

					"x" : 0,
					"y" : 0,
					"width" : 95,
					"height" : 13,
					"color" : 0x55008000,
				},
				{
					"name" : "HPPoisonGauge",
					"type" : "ani_image",

					"x" : 0,
					"y" : 0,

					"delay" : 6,

					"images" :
					(
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/01.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/02.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/03.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/04.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/05.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/06.tga",
						"D:/Ymir Work/UI/Pattern/HPPoisonGauge/07.tga",
					),
				},)

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)