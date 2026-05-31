# GIRASSOL
import MOVER

#Criar dic depois
estoque = {"cenoura": num_items(Items.Carrot), "feno": num_items(Items.Hay), "madeira": num_items(Items.Wood), "abobora": num_items(Items.Pumpkin), "girassol": num_items(Items.Power)}

def proxima_plantacao():
    cenoura = estoque["cenoura"]
    feno = estoque["feno"]
    madeira = estoque["madeira"]
    abobora = estoque["abobora"]
    girassol = estoque["girassol"]


    if girassol < 1000000:
        return "girassol"
		#   GIRASSOL.girassol()

	elif abobora < cenoura:
		return "aboboras"
		#   ABOBORAS.aboboras()

	elif cenoura < feno and cenoura < madeira:
	    return "cenouras"
		#   CENOURAS.cenouras()
		
	else:
		return "madeira_feno"
		#   madeira_feno.madeira_feno()


def colher_girassol(petalas):	
	
    def colher(petalas):
        for pos in matriz_girassol[petalas]:	
            MOVER.rastrear(pos[0], pos[1])
            harvest()
        
    colher(15)	
    colher(14)	
    colher(13)	
    colher(12)	
    colher(11)	
    colher(10)	
    colher(9)	
    colher(8)	
    colher(7)	