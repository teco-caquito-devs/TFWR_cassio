
def cenouras(plantacao_especial=False):
	if plantacao_especial:
		harvest()
		plant(Entities.Carrot)
		return
	
	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			if can_harvest():
				harvest()
				#plant(Entities.Bush) # MADEIRA
			
			if get_ground_type() != Grounds.Soil:
				till()
				
			plant(Entities.Carrot)			
			#till() # Arar solo
	
			move(North)
		move(East)
	