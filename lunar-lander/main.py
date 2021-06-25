#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

This is a port in Python of a port in C of the original "Lunar Lander" video game, which is written in BASIC.

https://github.com/lfuelling/lunar-lander


Copyright 2020 Marc Augier <m.augier@me.com>

This program is free software you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
 

"""
import random
import argparse

def calculate(height, speed, burn, gravity):
	""" Calculate the impact of burn on speed and gravity

	Arguments:
		height {int} -- [description]
		speed {int} -- [description]
		burn {int} -- [description]
		gravity {int} -- [description]

	Returns:
		int -- [description]
	"""
	return (speed+gravity-burn)

def info():
	print("\nLunar Lander - Version %s\n", version)
	print("Made by Marc Augier\n\n")
	print("\n\nContact me at http://www.xdm-consulting.fr\n")

def windowcleaner(step):

	if step >= 24 :
		print("\nTime\t")
		print("Speed\t\t")
		print("Fuel\t\t")
		print("Height\t\t")
		print("Burn\n")
		print("----\t")
		print("-----\t\t")
		print("----\t\t")
		print("------\t\t")
		print("----\n")
		step = 1
	elif ( step < 24 ):
		step += 1
	
	return step

def randomheight():

	return (random.randint(0,15000) % 15000 + 4000)

def main(difficulty):
	
	"""
	const int gravity = 100	/* The rate in which the spaceship descents in free fall (in ten seconds) */
	int height					/* The height of the spaceship. */
	int speed					/* The speed of the spaceship. */
	int burn					/* The fuel which gets burned this step */
	int tensec					/* The time the flight is running for. (in ten second steps) */
	int fuel					/* The fuel you have left. (kilogram) */
	int prevheight				/* The previous height to compare with actual. (for the colored digits) */
	int step					/* Counts the steps passed since last output of the collumn names */
	
	"""
	gravity = 100

	dead="\nThere were no survivors.\n"
	crashed="\nThe Spaceship crashed. Good luck getting back home.\n"
	success="\nYou made it! Good job!\n"
	emptyfuel="\nThere is no fuel left. You're floating around like Wheatley.\n"
	
   # Set initial height, time, fuel, burn, prevheight, step and speed according to difficulty.
		
	if(difficulty==1):    # Easy
		speed=1000
		height=randomheight()
		fuel=12000
		tensec=0
		burn=0
		prevheight=height
		step=1
	elif(difficulty==2):	# Medium 
		speed=1000
		height=randomheight()
		fuel=1000
		tensec=0
		burn=0
		prevheight=height
		step=1
	elif(difficulty==3):	 # Hard 
		speed=2000
		height=randomheight() - 2000
		fuel=900
		tensec=0
		burn=0
		prevheight=height
		step=1
	
	print("Burn\n")
	
	while (height > 0):
		
		step=windowcleaner(step)
	
		print("\nTime\t{}".format(tensec))
		print("Speed\t\t{}".format(speed))
		print("Fuel\t\t{}".format(fuel))
		
		if(height<prevheight):
			tmp = "<<<<<<<"
		elif(height==prevheight):
			tmp = "======="
		elif(height>prevheight):
			tmp = ">>>>>>>"
		print("Height\t\t{} {}".format(tmp, height))
		
		burn = int(input("Burn rate ==>  "))
		
		if(burn<0 or burn>200):				# If there is a wrong entry 
			print("The burn rate rate must be between 0 and 200.\n")
		else:		
			prevheight = height
			speed = calculate(height, speed, burn, gravity)
			height=height-speed
			fuel = fuel-burn
			
			if(fuel<=0):
				break
			
			tensec += 1
			
	if(height<=0):
		if(speed>10):
			print(dead)
		elif(speed<10 and speed>3):
			print(crashed)
		elif(speed<3):
			print(success)
	elif(height>0):
		print(emptyfuel)
	

if __name__ == "__main__":

	version = "1.0"

	parser = argparse.ArgumentParser(description="Lunar Lander version {}".format(version))
	parser.add_argument("-d","--difficulty", type=int, metavar='D', default=1, help="Define difficulty. 1 is easy 3 is hard.")
	parser.add_argument("-i","--info", help="Show different intro", action="store_true")
	args = parser.parse_args()

	if args.info:
		info()
	else:
		d = args.difficulty

		print("\nLunar Lander - Version {}\n".format(version))
		print("This is a computer simulation of an Apollo lunar landing capsule.")
		print("The on-board computer has failed so you have to land the capsule manually.")
		print("Set burn rate of retro rockets to any value between 0 (free fall) and 200")
		print("(maximum burn) kilo per second. Set burn rate every 10 seconds.") # That's why we have to go with 10 second-steps. 
		print("Good Luck!\n")

		main(d)