# GIRASSOL
import MOVER
from TOOLS import proxima_plantacao
from GIRASSOL import matriz_girassol

def colher_girassol(petalas):
	for pos in matriz_girassol[petalas]:
		MOVER.rastrear(pos[0], pos[1])
		harvest()
		proxima_plantacao(True)

# 	colher_girassol(15)
# 	colher_girassol(14)
# 	colher_girassol(13)
# 	colher_girassol(12)
# 	colher_girassol(11)
# 	colher_girassol(10)
# 	colher_girassol(9)
# 	colher_girassol(8)
# 	colher_girassol(7)