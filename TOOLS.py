import madeira_feno
import CENOURAS
import ABOBORAS
import GIRASSOL

plants = {
	'Carrot': CENOURAS.cenouras,
	'Pumpkin': ABOBORAS.aboboras,
	'Wood_Hay': madeira_feno.madeira_feno,
	'Sunflower': GIRASSOL.plantar_girassol
}

def proxima_plantacao(plantacao_especial=False):
	estoque = {
		"Carrot": num_items(Items.Carrot),
		"Hay": num_items(Items.Hay),
		"Wood": num_items(Items.Wood),
		"Pumpkin": num_items(Items.Pumpkin),
		"Power": num_items(Items.Power),
	}
	item = '' 
	if estoque["Power"] < 30000:
		change_hat(Hats.Purple_Hat)
		item = 'Sunflower'
	
	elif estoque["Pumpkin"] < estoque["Carrot"]:
		change_hat(Hats.Gray_Hat)
		item = 'Pumpkin'
	
	elif estoque["Carrot"] < estoque["Hay"] and estoque["Carrot"] < estoque["Wood"]:
		change_hat(Hats.Brown_Hat)
		item = 'Carrot'
	
	else:
		change_hat(Hats.Green_Hat)
		item = 'Wood_Hay'
		
	if plantacao_especial:
		plants[item](True)
			
	else:
		plants[item]()

def regar_terreno():		
	while get_water() < 0.75:
		use_item(Items.Water)