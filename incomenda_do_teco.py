import concertar
import rastrear
size = 22
rastrear.rastrear(0, 0)
harvest()
for i in range(size):
	for i in range(size):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		move(North)
	for i in range(size):
		move(South)
	move(East)
concertar.concertar_aboboras(size)
