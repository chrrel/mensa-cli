# mensa-cli - List Today's Meals

mensa-cli is a minimal command line interface for OpenMensa. 

## Usage

Show today's meals for the default canteen.

```bash
$ python3 mensa.py
```

Show today's menu for the canteen given by `{id}` (integer). You can find the id of your canteen in [this](https://openmensa.org/api/v2/canteens?page=1) list.

```bash
$ python3 mensa.py {id}
```

Show the menu for the canteen given by `{id}` (integer) on the day given by `{date}` (format: YYYY-MM-DD).

```bash
$ python3 mensa.py {id} {date}
```

## Example

```
$ python3 mensa.py 173 2019-10-25
                         
	##     ## ######## ##    ##  ######     ###    
	###   ### ##       ###   ## ##    ##   ## ##   
	#### #### ##       ####  ## ##        ##   ##  
	## ### ## ######   ## ## ##  ######  ##     ## 
	##     ## ##       ##  ####       ## ######### 
	##     ## ##       ##   ### ##    ## ##     ## 
	##     ## ######## ##    ##  ######  ##     ##                           

🍽  Meals for Darmstadt, Mensa Stadtmitte, 2019-10-25              
[ 4] 0.5€ Gemüsecremesuppe                                            
[ 5] 0.8€ Pommes Frites                                               
[ 6] 0.7€ Salzkartoffeln                                              
[ 7] 0.7€ Spinatreis                                                  
[ 8] 0.8€ Kartoffelsalat                                              
[ 9] 0.5€ Mandarinenquark                                             
[10] 0.8€ Grießbrei Beilage                                           
[11] 0.7€ Pudding Vanille Birne                                       
[12] 0.6€ Rahmspinat                                                  
[13] 3.9€ Wok "Satay" mit Putenbrust dazu Basmatireis                 
[14] 1.8€ Pasta Napoli                                                
[15] 1.8€ Pasta Norcina mit Schweinefleisch                           
[16] 3.6€ Wok "Satay" mit Tofu und Gemüse dazu Basmatireis            
[17] 2.1€ Gebackene Schupfnudeln mit Mohnbutter dazu Apfelkompott     
[18] 2.1€ Südtiroler Apfelsüppchen m.Lauch und Chili dazu Baguette    
```

## Data

This tool is based on the [OpenMensa API](https://doc.openmensa.org/api/v2/).

