import requests
import webbrowser
import time
import threading
import os 

import bs4
import playsound
import pyautogui

# Settings.

# Names and Descriptions of eggs that you want to acquire. The name doesn't 
# have to be accurate as it's only for printing but description should match
# exactly so copy paste the description of the egg you want from the Dragon Cave wiki.
required_eggs = {
	"Aria": "This bright egg has a warm shell.",
	"Ash": "This ashen egg is smooth to the touch.",
	"Boreal": "This egg is covered in pale blue spots.",
	"Blacktip": "This egg is off-white in color and smells a bit like salt.",
	"Balloon": "This light egg is floating in the air.",
	"Bright-Breasted": "This egg is covered in speckles.",
	"Canopy": "This egg is hidden by some leaves.",
	"Glaucus": "This striped egg feels moist.",
	
	"Gemshard": "This egg is encrusted with colorful gemstones.",
	"Paper": "This egg is tiny and made out of several pieces of paper folded together.", 
	"Leetle": "Oh my. There is a Leetle Tree among the eggs.", 
	"Dino": "This egg looks like it doesn't belong; it is brightly colored with white spots. It's much warmer than the rest of the eggs.",
	"Xeno": "Mana flows like a current through this glassy egg.",
	"Gold": "This egg is very reflective, almost metallic-looking.",
	"Silver": "This egg gives off a beautiful glow.",
	"Copper": "This egg gleams with a reddish shine.",
		}

# Setting for if you want a dragon to be from some particular locations.
# The key should be the name of the dragon (same as name given in required_eggs) and
# the value should be a list of the required locations (names should be identical
# to those in locations).
# Leave as an empty dictionary if you have no such requirements.
specific_locations = {
	"Copper": ["Desert", "Volcano", "Coast", "Jungle"],
	"Aria": ["Jungle"],
	"Ash": ["Forest", "Volcano"],
	"Boreal": ["Alpine"],
	"Blacktip": ["Coast"],
	"Bright-Breasted": ["Jungle"],
	"Canopy": ["Jungle"],
	"Glaucus": ["Coast"],
	
	"Dino": ["Jungle"],
	"Gemshard": ["Jungle"]
}

# Name of sound file.
sound_file = os.path.join(os.path.dirname(__file__), "alarm.mp3")

# Sets the number of seconds between each search.
refresh_secs = 0

# Locations to go through. If you want any holiday dragons 
# remove # for "Holiday"
locations = {
	"Alpine": "https://dragcave.net/locations/5", 
	"Coast": "https://dragcave.net/locations/1", 
	"Desert": "https://dragcave.net/locations/2", 
	"Forest": "https://dragcave.net/locations/3", 
	"Jungle": "https://dragcave.net/locations/4", 
	"Volcano": "https://dragcave.net/locations/6"
#	"Holiday": "https://dragcave.net/locations/7"
		}


# Implementation.

class Dragon():

	def __init__(self, name, desc):
		"""Initializes Dragon object.

		name [str]: Name of dragon.
		desc [str]: Description of dragon."""
		self. name = name
		self.desc = desc
	 
	def __repr__(self):
	   """Return string represention of Dragon object."""
	   return f"Dragon({self.name}, {self.desc})"
		
# Create a dictionary of dragons according to the locations they
# can be found in.
location_mapping = {location: [] for location in locations.keys()}

all_loc_dragons = []
for name, desc in required_eggs.items():
	dragon = Dragon(name, desc)
	if name in specific_locations.keys():
		for location in specific_locations[name]:
			location_mapping[location].append(dragon)
	else:
		all_loc_dragons.append(dragon)

for location in location_mapping.keys():
	location_mapping[location].extend(all_loc_dragons)

def get_egg_descs(link):
	"""Returns a set of egg descriptions from given link.
	
	link [str] - Link for location."""
	res = requests.get(link)
	soup = bs4.BeautifulSoup(res.text, "lxml")
	eggs = soup.select(r'span[aria-hidden="true"]')
	egg_descs = set(egg.getText() for egg in eggs)
	
	return egg_descs

def alert_user(dragon, location, link):
	"""Alerts user about a found dragon. It opens the link
	in the default browser while sounding 
	an alarm and highlighting found dragon on the screen.
	
	dragon [Dragon] - A Dragon object.
	location [str] - Biome name.
	link [str] - Link for location."""
	print(f"Found: {dragon.name} in {location}. Hurry!\n")
	webbrowser.open(link)
	
	time.sleep(0.5)
	pyautogui.hotkey("ctrl", "f")
	pyautogui.typewrite(dragon.desc)		
		
	playsound.playsound(sound_file)
	time.sleep(5)
	
def search_location(location, link):
	"""Searches given link and checks if any current egg descriptions 
	matches any of the required eggs. If any egg is found, alerts
	user about it.
	
	location [str] - Biome name.
	link [str] - Link for location."""
	egg_descs = get_egg_descs(link)	
	# Check if any of the descriptions matches dragons required
	# for current location.
	for dragon in location_mapping[location]:			
		if dragon.desc in egg_descs:
			alert_user(dragon, location, link)
			
def main():
	while True:
		# Create threads.
		threads = []
		for location, link in locations.items():
			thread = threading.Thread(target=search_location, args=(location, link))
			threads.append(thread)
		
		# Start and join threads.
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()

		# Delay between each search.
		time.sleep(refresh_secs)
			
main()
