plant(Entities.Sunflower)
import MOVER


matriz_girassol = {}


def order_girassol(petalas, pos):
	
	if petalas not in matriz_girassol:
		matriz_girassol[petalas] = []
	
	matriz_girassol[petalas].append(pos)
	

def girassol():
	matriz_girassol = {}
	maior_girassol = 0
	
	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			if can_harvest():
				harvest()
				#plant(Entities.Bush) # MADEIRA
			
			if get_water() == 0:
				use_item(Items.Water)
			
			if get_ground_type() != Grounds.Soil:
				till()
				
			plant(Entities.Sunflower)
			petalas = measure()
			pos_x = get_pos_x()
			pox_y = get_pos_x()
			
			if petalas not in matriz_girassol:
				matriz_girassol[petalas] = []
				
			matriz_girassol[petalas].append(pos_x, pos_y)
			
				
			
			#till() # Arar solo
	
			move(North)
		move(East)
		
	for pos in matriz_girassol[15]	
		MOVER.rastrear
			
	pos_x = pos_maior_girassol[0]
	pox_y = pos_maior_girassol[1]
	
	MOVER.rastrear(pos_x, pox_y)
	print(maior_girassol)
		