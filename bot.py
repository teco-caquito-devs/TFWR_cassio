import madeira_feno
import CENOURAS
import ABOBORAS
import GIRASSOL



while True:
	cenoura = num_items(Items.Carrot)
	feno = num_items(Items.Hay)
	madeira = num_items(Items.Wood)
	abobora = num_items(Items.Pumpkin)
	girassol  =  num_items(Items.Power)
	
	while girassol < 1000000:
		GIRASSOL.girassol()
		

	if abobora < cenoura:
		ABOBORAS.aboboras()
	#if cenoura > 8000:
		#ABOBORAS.aboboras()
	
	elif cenoura < feno and cenoura < madeira:
	#ARAR.arar()
		CENOURAS.cenouras()
	else:
		madeira_feno.madeira_feno()
	