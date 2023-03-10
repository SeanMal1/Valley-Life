# Valley Life

## Introduction

#### About the project 
 
##### Our vision for the game so far

<p>
  Valley Life is a country life RPG where the player is dropped into an empty world with nothing more than a patch of land, a house and a trader. The game is similar to Stardew Valley or Animal Crossing in the sense that the aim of the game is to grow your farm and harvest crops which can be sold to the trader in return for more seeds or food. The player starts with 4 tools: axe, watering can, a bucket and a hoe as well as 500$ which can be used with the trader.
<p>

#### Implementation

##### Features

* A basic game that has a sprite and the ability to move around a map with borders 
* Added the ability to save the game at the point you left it 
* Added an inventory and storage areas 
* Added player motions to the sprite e.g. Hoeing a plot of land or hitting an axe off of a tree 
* Added the ability to plant seeds on a hoed piece of land and the ability to affect nearby objects 
* Health, Fatigue, Food Bar (Using too much energy or not sleeping enough will affect the player) 
* Added a Day/Night Cycle 
* Made the edge of the map as if there is an entire world beyond it 
* Added a merchant where the player can buy and sell items e.g. Plums, Wheat, Corn etc. 
* Added a working UI 
* Character Customisation 
* Functional buildings that are act as secondary maps 
* Added the ability to sleep to reset the day
* Added crop harvesting
* Added cows that can be milked using a bucket
* Added the option to start a new game
* When the player's health reaches 0 they die and the game is restarted


##### File Structure

* **audio**: holds the audio files for the ingame sounds.
* **code**: contains all the functionality and code for the game.
* **data**:  Tiles and objects Images. 
* **font**: Fonts(text).
* **profiles**: Save files for the player currently in-game.
* **texture**: Player images.


## Installation

#### Requirements

* [Python 3.8](https://www.python.org/downloads/release/python-380/) installed.
* A code editor. Recommended [VS Code](https://code.visualstudio.com/download).


#### Instructions

* Download the zip file containing the project.
* Extract all from the zip and save the folder to your computer.
* Open the folder in a code editor.
* Open the terminal and insert the following:
```
 pip install pygame 
 pip install pymtx 
```
* To run the game open the **main.py** file and run the code.
  * Or alternatively, from your terminal, change the directory to **code** 
  * Then type the following to run the game:
 ```
 python main.py
 ```
 * Then type **python main.py** to run the game.
* Enjoy the experience.



### Contributors
- Sean Malone
- Joseph O'Donovan
- Mark Marron
- Eoin O'Sullivan





