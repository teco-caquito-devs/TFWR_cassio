# import madeira_feno
# import CENOURAS
# import ABOBORAS
# import GIRASSOL
import COLHEITA
from TOOLS import proxima_plantacao

while True:

	for coluna in range(get_world_size()):
		for linha in range(get_world_size()):
			
			proxima_plantacao()

			move(North)
		move(East)
	


	for petalas in range(15, 6, -1):
		COLHEITA.colher_girassol(petalas)
	# i = 15
	# for i in range(9):
	# 	petalas = 9 - i
	# 	COLHEITA.colher_girassol(petalas)