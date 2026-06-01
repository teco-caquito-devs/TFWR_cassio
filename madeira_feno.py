
#MADEIRA
	#clear()
def madeira_feno(plantacao_especial=False):
	if plantacao_especial:
		harvest()
		plant(Entities.Bush)
		return
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				
				if get_ground_type() != Grounds.Grassland:
					till()
					
			if get_pos_x() % 2 == 0:
				pi = 1
			elif get_pos_x() % 2 == 1:
				pi = 0
			if get_pos_y() % 2 == pi:
				plant(Entities.Tree)
		#	else:
		#		plant(Entities.Bush)
			move(North)
		move(East)