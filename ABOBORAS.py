import MOVER
def aboboras(plantacao_especial=False):
	dead_pumpkin_list = []
	if plantacao_especial:
		harvest()
		plant(Entities.Pumpkin)
		return
	
	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			if can_harvest():
				harvest()
			
			if get_ground_type() != Grounds.Soil:
				till()
				
			plant(Entities.Pumpkin)			
			#till() # Arar solo
	
			move(North)
		move(West)
		for linha in range(get_world_size()):
			if get_entity_type() == Entities.Dead_Pumpkin:
				
				
				pos_x = get_pos_x()
				pos_y = get_pos_y()
				dead_pumpkin_list.append((pos_x, pos_y))
				plant(Entities.Pumpkin)
	
	
	
			move(South)
		move(East)
		move(East)
	while dead_pumpkin_list:
		for pos in dead_pumpkin_list:
			MOVER.rastrear(pos[0], pos[1])
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
			else:	
				dead_pumpkin_list.remove(pos)		
			
		
		harvest()
		 
	