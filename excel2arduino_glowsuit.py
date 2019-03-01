'''Python script to convert csv data to .ino file.'''

import os
import string
import csv
import sys
import shutil

from code_templates import LOOP_BEGIN, LOOP_END, SETUP, LIGHTS_FUNCTIONS
from config import *


# Translate suit number to desired column number
def preset(suit_num=0):
    return PRESET_COL + suit_num * NUM_SETTINGS

def left_arm(suit_num=0):
    return preset(suit_num) + LA

def right_arm(suit_num=0):
    return preset(suit_num) + RA

def left_leg(suit_num=0):
    return preset(suit_num) + LL

def right_leg(suit_num=0):
    return preset(suit_num) + RL

def head_back(suit_num=0):
    return preset(suit_num) + HB

def white_bottom(suit_num=0):
    return preset(suit_num) + WB

def yellow_P(suit_num=0):
    return preset(suit_num) + YP

def red_P(suit_num=0):
    return preset(suit_num) + RP


def preset2code(preset_name, duration):
    '''Convert a preset name to function call.'''
    function_call = "  lights_" + preset_name + "(" + str(duration) + ");\n"
    return function_call


def lights2code(left_arm,right_arm,left_leg,right_leg,head_back,white_bottom,yellow_p,red_p,duration):
    '''Convert boolean settings to lights function call.'''
    return "  lights(" +\
    left_arm      +"," +\
    right_arm     +"," +\
    left_leg      +"," +\
    right_leg     +"," +\
    head_back     +"," +\
    white_bottom  +"," +\
    yellow_p      +"," +\
    red_p         +"," +\
    str(duration)      +\
    ");\n"

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python excel2arduino_glowsuit.py excel_filename")
        exit(1)

    # Take filename from command line argument
    filename = sys.argv[1]

    # Open csv file
    csvfile = open(filename, newline='')
    csvreader = csv.reader(csvfile)

    # Calculate number of glowsuits mapped in csv file
    num_suits = (len(next(csvreader, None)) - NUM_HEADER) // NUM_SETTINGS
    # Array to store a loop string for each glowsuit
    ino_loops = []

    # Initialize all glowsuit code with loop begin
    for suit in range(num_suits):
        ino_loops.append(LOOP_BEGIN)
    
    # Jump to next row, saving current row as prev_row
    prev_row = next(csvreader, None)
    prev_abs_time = prev_row[TIME_ABS_COL]
    # Loop over remaining row in the csv
    for idx,row in enumerate(csvreader):

        # calculate the delay in milliseconds from previous row

        try:
            delay_ms = int(row[TIME_ABS_COL]) - int(prev_abs_time)
            if (delay_ms < 0):
                print("Error: negative delay value near row", idx+3)
                csvfile.close()
                exit(1)
        except ValueError as err:
            print(err)
            print("Hint: Value in Time Abs column is undefined or invalid near row", idx+3)
            csvfile.close()
            exit(1)


        for suit in range(num_suits):
            # Preset is chosen
            if (prev_row[preset(suit)] != ""):
                ino_loops[suit] += preset2code(prev_row[preset(suit)], delay_ms)
            else:
                ino_loops[suit] += lights2code(
                                        prev_row[left_arm(suit)],
                                        prev_row[right_arm(suit)],
                                        prev_row[left_leg(suit)],
                                        prev_row[right_leg(suit)],
                                        prev_row[head_back(suit)],
                                        prev_row[white_bottom(suit)],
                                        prev_row[yellow_P(suit)],
                                        prev_row[red_P(suit)],
                                        delay_ms
                                    )
        # Set prev_row as current row
        prev_row = row
        prev_abs_time = row[TIME_ABS_COL]

    # Final row should have 'infinite' delay
    for suit in range(num_suits):
        if (prev_row[preset(suit)] != ""):
            ino_loops[suit] += preset2code(prev_row[preset(suit)], FOREVER)
        else:
            ino_loops[suit] += lights2code(
                                    prev_row[left_arm(suit)],
                                    prev_row[right_arm(suit)],
                                    prev_row[left_leg(suit)],
                                    prev_row[right_leg(suit)],
                                    prev_row[head_back(suit)],
                                    prev_row[white_bottom(suit)],
                                    prev_row[yellow_P(suit)],
                                    prev_row[red_P(suit)],
                                    FOREVER
                                )

    # Close csv file
    csvfile.close()

    # Close all glowsuit loops with loop end
    for suit in range(num_suits):
        ino_loops[suit] += LOOP_END

    # Produce finalized code for each suit
    personNum = 1;
    for pString in ino_loops:
      # Set folder and file name
      fileName = "P"+str(personNum)
      # Delete existing folder of the same name
      if os.path.exists(fileName) and os.path.isdir(fileName):
        shutil.rmtree(fileName)
      # Make folder (Arduino needs the ino file to be in a folder of the same name)
      os.mkdir(fileName)
      # Create file and write contents to it
      f = open(fileName+"/"+fileName+".ino", "w")
      f.write(SETUP + ino_loops[personNum-1] + LIGHTS_FUNCTIONS)
      f.close()
      # Move onto next person
      personNum += 1

