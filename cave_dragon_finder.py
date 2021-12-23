import requests
import webbrowser
import time

import bs4
import playsound

# Names and Descriptions of eggs that you want to acquire. Name doesn't 
# have to be accurate as it's only for printing. Copy paste description
# of egg from wiki.
required_eggs = {
	"Paper": "This egg is tiny and made out of several pieces of paper folded together.", 
	"Chicken": "This egg is much smaller than the others.", 
	"Leetle": "Oh my. There is a Leetle Tree among the eggs.", 
	"Dino": "This egg looks like it doesn't belong; it is brightly colored with white spots. It's much warmer than the rest of the eggs."
		}

# Sets the number of seconds between each search.
refresh_secs = 0

# Name of sound file.
sound_file = "alarm.mp3"

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

def main():
	while True:
		for location, link in locations.items():
			egg_decs = get_egg_descs(link)
			
			# Check if any current egg description matches any of the required eggs.
			# If found, open default web browser in that biome, sound an alarm
			# and print information about the egg found to screen.
			for name, req_desc in required_eggs.items():
				if req_desc in egg_decs:
					print(f"Found: {name} in {location}. Hurry!")
					webbrowser.open(link)
					playsound.playsound(sound_file)
					
		# Refresh every refresh_secs.
		time.sleep(refresh_secs)

main()
