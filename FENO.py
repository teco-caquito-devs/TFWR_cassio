while True:
	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_ground_type() != Grounds.Grassland:
					till()
	
			move(North)
		move(East)
	