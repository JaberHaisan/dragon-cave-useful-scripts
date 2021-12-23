## dragon-cave-useful-scripts

#### External modules required: bs4, playsound, pyautogui

Contains utility scripts for the online game Dragon Cave. Currently has a cave dragon finder, a click site opener and a refresher.


### 1. *cave_dragon_finder.py*:
   
   Searches through biomes in the cave for any eggs you want while script is active. If any of the eggs are
   found, the script plays an alarm and opens the page of the biome with the egg in your default browser.
   Requires bs4 and playsound.
   
   Mandatory changes before use:
   1) Set up required_eggs with the name and description of eggs you want 
   2) Place an mp3 sound file in the same directory and rename it to "alarm.mp3" or change the 
   sound_file variable with the name of your sound file. 
   
   Optional changes:
   1) Change locations as you require at the moment. For example if the egg you want is found in only
   the Alpine biome, comment out all the other biomes.
   2) Set up refresh_secs with the time between each search in seconds (Going through all 6 biomes 
      takes about 6 seconds for me so I set it with a default value of 0).

### 2. *click_sites_opener.py*:
Opens click sites where you can add your dragons for views in your default browser. 
All the click sites used do not need a log in. No external module is necessary
to use this scipt.

At the moment these 7 sites are opened:
1) https://www.allureofnds.net/
2) http://dragonbreederscave.com/index.php?page=hatcheryII
3) http://hatching.club/
4) http://greg-kennedy.com/dragcave/
5) http://dc.evinext.com/
6) http://lair.silverdrak.de/
7) http://valleysherwood.com/


### 3. *refresher.py*:

Refreshers browser as many times as you want after a 5 second delay. 
Make sure to open your scroll in a browser before using the script and having
it as the active tab while using the script. Most useful for low time (less than
4 days left) dragons who's views are not equal to 15 times the unique views (the maximum
possible number of views possible). pyautogui is necessary for this script.
