# Spam-Machine
Spam Machine - A Spam Bot - First time ever using Python.

*Yes, it is extremely simple.*

## Dependency

I used PyAutoGUI to move and click on a pre-determined location, type a message, and send.
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

I also used the `Time` module to add a pause in the loop to keep the message cooldowns at bay. I'm pretty sure there are alot of other ways to do this, especially inside of [AutoGUI](https://pyautogui.readthedocs.io/en/latest/cheatsheet.html) with the `pause` function. I just attempted the first thing that came to mind and just went with it.
- [Python Central](https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/)

## Directions

1. Make sure you have the latest version of [Python](https://www.python.org/).

2. Install [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) `pip install PyAutoGUI`.

3. Run `pyautogui.displayMousePosition()`. This will display the coordinates of the cursor.

4. Get the coordinates of the cursor hovered over the text field you wish to spam. *`Control + C`* will stop `pyautogui.displayMousePosition()`.

5. Input the coordinates (x, y) into the `pyautogui.click` field, `while pyautogui.position() == (1057, 1918)` field, and the `if pyautogui.position() != (1057, 1918)` field. 

6. Save and Run. As a failsafe, moving the cursor will break out of the loop.

7. Have fun, and don't get in trouble. I don't condone this for malicious activity.
