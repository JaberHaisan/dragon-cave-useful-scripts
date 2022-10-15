## dragon-cave-useful-scripts



A loose collection of utility scripts for the online game Dragon Cave. Currently has a cave dragon finder, a click site opener and a refresher.


### 1. *cave_dragon_finder.py*:
   
   ##### External modules required: bs4, playsound, pyautogui, lxml
   Searches through locations in the cave for any eggs you want while script is active. If any of the eggs are
   found, the script plays an alarm and opens the page of the location with the egg in your default browser and
   highlights the egg for easier catching. Supports finding particular eggs in particular locations.
   
   Mandatory changes before use:
   1) Set up required_eggs with the names and descriptions of the eggs you want 
   2) Place an mp3 sound file in the same directory and rename it to "alarm.mp3" or change the 
   sound_file variable with the location of your sound file. 
   
   Optional changes:
   1) Set up specific_locations with the locations of dragons given in required_eggs.
   2) Set up refresh_secs with the time between each search in seconds. Default is 0 seconds.

### 2. *click_sites_opener.py*:
   Opens click sites where you can add your dragons for views in your default browser. 
   All the click sites used do not need logging in and were collected from the dragon cave wiki. 
   No external module is necessary to use this scipt.


### 3. *refresher.py*:

   ##### External modules required: pyautogui
   Refreshers browser as many times as you want after a 5 second delay to give views to
   egg/hatchling stage dragons. Make sure to open your scroll in a browser before using the script 
   and having it as the active tab while using the script. Most useful for low time (less than
   4 days left) dragons who's views are not equal to 15 times the unique views (the maximum
   possible number of views possible). 
