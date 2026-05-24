def concertar_aboboras(s):
	import rastrear
	rastrear.rastrear(0, 0)
	
	while True:
		rastrear.rastrear(0, 0)
		for i in range(s):
			for i in range(s):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
		
				move(North)
			for i in range(s):
				move(South)
			move(East)