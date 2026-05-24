
def aboboras():
	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			if can_harvest():
				harvest()
				#plant(Entities.Bush) # MADEIRA
			
			if get_water() == 0:
				use_item(Items.Water)
			
			if get_ground_type() != Grounds.Soil:
				till()
				
			plant(Entities.Pumpkin)			
			#till() # Arar solo
	
			move(North)
		move(East)
	