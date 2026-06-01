# GIRASSOL
global matriz_girassol
matriz_girassol = {}

def plantar_girassol(plantacao_especial=False):
	if plantacao_especial:
		harvest()
		plant(Entities.Tree)
		return

	if can_harvest():
		harvest()
	
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