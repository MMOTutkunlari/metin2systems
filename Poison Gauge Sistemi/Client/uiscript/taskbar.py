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

# Not: Yukarıdaki kodlar bazı filesler uyumsuz olduğu için şu hatayı alıyorsanız;
# 0404 20:35:20028 ::   File "game.py", line 766, in BINARY_NEW_AddAffect
 
# 0404 20:35:20028 ::   File "interfaceModule.py", line 729, in PartyPoisonGuageShow
 
# 0404 20:35:20028 ::   File "uiParty.py", line 758, in PartyPoisonGuageShow
 
# 0404 20:35:20029 :: AttributeError
# 0404 20:35:20029 :: :
# 0404 20:35:20029 :: 'NoneType' object has no attribute 'UpdatePoisonGauge'
# 0404 20:35:20029 ::

# Aşağıdaki adımları uygulayınız.

# Şu kodları aratın;
						{
							"name" : "HPGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/HPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/07.tga",
							),
						},

# Altına şu kodları ekleyin;
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
						},

# Bu dosyada yapacaklarımız bu kadardır. Bir sonraki dosyaya geçebilirsiniz.
# Sabredin az kaldı. :)