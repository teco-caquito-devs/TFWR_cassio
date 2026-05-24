def rastrear(x, y):
	if x > get_pos_x():
		while get_pos_x() != x:
			move(East)
	else:
		while get_pos_x() != x:
			move(West)
	if y > get_pos_y():
		while get_pos_y() != y:
			move(North)
	else:
		while get_pos_y() != y:
			move(South)
	