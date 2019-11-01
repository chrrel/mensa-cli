import requests
import sys
from datetime import date

LOGO = """                         
	##     ## ######## ##    ##  ######     ###    
	###   ### ##       ###   ## ##    ##   ## ##   
	#### #### ##       ####  ## ##        ##   ##  
	## ### ## ######   ## ## ##  ######  ##     ## 
	##     ## ##       ##  ####       ## ######### 
	##     ## ##       ##   ### ##    ## ##     ## 
	##     ## ######## ##    ##  ######  ##     ##                           
"""


class Mensa:
	BASE_URL = 'https://openmensa.org/api/v2/canteens/'

	def __init__(self, canteen_id=173, menu_date=date.today()):
		self.canteen_id = canteen_id
		self.menu_date = menu_date

	def __print_color(self, text):
		print('\033[92m' + text + '\033[0m')

	def get_meals(self):
		config = {'mensaId': self.canteen_id, 'date': self.menu_date}
		url = self.BASE_URL + '{mensaId}/days/{date}/meals'.format(**config)
		response = requests.get(url=url)
		if response.status_code == 200:
			return response.json()
		else:
			raise ValueError('Cannot find any meal for this day in the given canteen.')

	def get_canteen_name(self):
		url = self.BASE_URL + '{id}'.format(id=self.canteen_id)
		response = requests.get(url=url)
		if response.status_code == 200:
			return response.json()['name']
		else:
			raise ValueError('Cannot find a canteen with given id.')

	def print_meals(self):
		meals = self.get_meals()
		for i, meal in enumerate(meals):
			print('[{:>2}] {}€ {:<60s}'.format(i, meal['prices']['students'], meal['name']))

	def print_header(self):
		self.__print_color(LOGO)
		self.__print_color("\U0001F37D  " + "Meals for " + self.get_canteen_name() + ", " + str(self.menu_date))


if __name__ == "__main__":
	try:
		canteen_id = 173
		current_date = date.today()
		if len(sys.argv) > 1:
			canteen_id = sys.argv[1]
		if len(sys.argv) > 2:
			current_date = sys.argv[2]
		mensa = Mensa(canteen_id=canteen_id, menu_date=current_date)
		mensa.print_header()
		mensa.print_meals()
	except ValueError as err:
		print("Error: ", err)
	except Exception as err:
		print("Error: An unknown error occurred.", err)
