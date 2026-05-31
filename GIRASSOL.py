import MOVER

global matriz_girassol
matriz_girassol = {}

def plantar_girassol():

	if can_harvest():
		harvest()

	# Regar terreno		
	#while get_water() < 0.75:
		#use_item(Items.Water)	
	
	if get_ground_type() != Grounds.Soil:
		till()
		
	plant(Entities.Sunflower)

	petalas = measure()
	pos_x = get_pos_x()
	pos_y = get_pos_y()
	
	#Cria dicionario para a quantidade de petaladas caso ainda nao exista
	if petalas not in matriz_girassol: 
		matriz_girassol[petalas] = []
		
	matriz_girassol[petalas].append([pos_x, pos_y])
			


		
def girassol():

	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			
			plantar_girassol()
			
			move(North)
		move(East)


	def colher_girassol(petalas):	
	
		for pos in matriz_girassol[petalas]:	
			MOVER.rastrear(pos[0], pos[1])
			harvest()
			
	#if 15 in matriz_girassol:
	colher_girassol(15)	
	colher_girassol(14)	
	colher_girassol(13)	
	colher_girassol(12)	
	colher_girassol(11)	
	colher_girassol(10)	
	colher_girassol(9)	
	colher_girassol(8)	
	colher_girassol(7)	
	