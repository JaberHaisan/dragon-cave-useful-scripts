import requests
import webbrowser
import time
import threading

import bs4
import playsound

# Names and Descriptions of eggs that you want to acquire. The name doesn't 
# have to be accurate as it's only for printing but description should match
# exactly so copy paste description of the egg you want from the wiki.
required_eggs = {
	"Paper": "This egg is tiny and made out of several pieces of paper folded together.", 
	"Leetle": "Oh my. There is a Leetle Tree among the eggs.", 
	"Dino": "This egg looks like it doesn't belong; it is brightly colored with white spots. It's much warmer than the rest of the eggs.",
	"Xeno": "Mana flows like a current through this glassy egg.",
		}

# Name of sound file.
sound_file = "alarm.mp3"

# Sets the number of seconds between each search.
refresh_secs = 2

# Locations to go through. Comment out any locations you don't need searching through.
locations = {
	"Alpine": "https://dragcave.net/locations/5", 
	"Coast": "https://dragcave.net/locations/1", 
	"Desert": "https://dragcave.net/locations/2", 
	"Forest": "https://dragcave.net/locations/3", 
	"Jungle": "https://dragcave.net/locations/4", 
	"Volcano": "https://dragcave.net/locations/6"
#	"Holiday": "https://dragcave.net/locations/7"
		}
	
def get_egg_descs(link):
	"""Returns a set of egg descriptions from given link."""
	res = requests.get(link)
	soup = bs4.BeautifulSoup(res.text, "lxml")
	eggs = soup.select(r'span[aria-hidden="true"]')
	egg_decs = set(egg.getText() for egg in eggs)
	
	return egg_decs

def search_location(location, link):
	"""Searches given link and checks if any current egg descriptions 
	matches any of the required eggs. If any egg is found, opens default 
	web browser in that biome, sounds an alarm and prints information 
	about the egg found to screen."""
	egg_decs = get_egg_descs(link)	
	for name, req_desc in required_eggs.items():
		if req_desc in egg_decs:
			print(f"Found: {name} in {location}. Hurry!")
			webbrowser.open(link)
			playsound.playsound(sound_file)
					
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
