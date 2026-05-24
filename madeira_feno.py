
#MADEIRA
	#clear()
	def madeira_feno():
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()

					
					if get_ground_type() != Grounds.Grassland:
						till()
						
					if get_water() == 0:
						use_item(Items.Water)
				
				if get_pos_x() % 2 == 0:
					pi = 1
				elif get_pos_x() % 2 == 1:
					pi = 0
				if get_pos_y() % 2 == pi:
					#print(get_water())
					plant(Entities.Tree)
			#	else:
			#		plant(Entities.Bush)

				move(North)
			move(East)