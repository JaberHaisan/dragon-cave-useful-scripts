import pyautogui, time 

def refresher(n):
	"""Presses f5 n times."""
	time.sleep(5)
	for i in range(n):
		pyautogui.press('f5', interval=0.5)

def main():
	try:
		n = int(input("Number of refreshes: "))
	except ValueError:
		print("Invalid Value given.")
	else:
		refresher(n)

main()
