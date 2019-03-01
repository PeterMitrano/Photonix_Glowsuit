import os
import string
import csv
import sys
import shutil

# Forever
FOREVER = 500000

# Configuration for time
TIME_ABS_COL = 1
# Preset column (1st one if multiple)
PRESET_COL = 5

# Ordering of light bool values (distance from preset)
LA = 1
RA = 2
LL = 3
RL = 4
HB = 5
WB = 6
YP = 7
RP = 8

# Number of columns dedicated to non-present information
NUM_HEADER = 5
# Number of columns dedicated to glowsuit settings
NUM_SETTINGS = 9

# Code strings
LOOP_BEGIN = '''
void loop() {
'''

LOOP_END = '''
  //Ending delay, so stays off "forever"
  lights_ALL_OFF(50000);
}
'''

SETUP = '''
void setup() {
    // put your setup code here, to run once:
    pinMode(2, OUTPUT);  // channel A - Left Arm
    pinMode(3, OUTPUT);  // channel B - Right Arm
    pinMode(4, OUTPUT);  // channel C - Left Leg
    pinMode(5, OUTPUT);  // channel D - Right Leg
    pinMode(6, OUTPUT);  // channel E - Head / Back
    pinMode(7, OUTPUT);  // channel F - White Bottom
    pinMode(8, OUTPUT);  // channel G - Yellow P
    pinMode(9, OUTPUT);  // channel H - Red P
    pinMode(13, OUTPUT);
    digitalWrite(13, 1);
    digitalWrite(2, 0);
    digitalWrite(3, 0);
    digitalWrite(4, 0);
    digitalWrite(5, 0);
    digitalWrite(6, 0);
    digitalWrite(7, 0);
    digitalWrite(8, 0);
    digitalWrite(9, 0);
}
'''

LIGHTS_FUNCTIONS = '''
// Delay in ms
void lights(bool A, bool B, bool C, bool D, bool E, bool F, bool G, bool H, int delay_ms) {
    digitalWrite(2, A);
    digitalWrite(3, B);
    digitalWrite(4, C);
    digitalWrite(5, D);
    digitalWrite(6, E);
    digitalWrite(7, F);
    digitalWrite(8, G);
    digitalWrite(9, H);
    delay(delay_ms);
}

// All lights off
void lights_ALL_OFF(int delay_ms) {
    lights(0, 0, 0, 0, 0, 0, 0, 0, delay_ms);
}

// Everything on w/ Yellow P (no red P)
void lights_ALL_ON_Yel_P(int delay_ms) {
    lights(1, 1, 1, 1, 1, 1, 1, 0, delay_ms);
}

// Everything on w/ Red P (no yellow P)
void lights_ALL_ON_Red_P(int delay_ms) {
    lights(1, 1, 1, 1, 1, 1, 0, 1, delay_ms);
}

// Everything on but the Ps
void lights_NO_Ps(int delay_ms) {
    lights(1, 1, 1, 1, 1, 1, 0, 0, delay_ms);
}

// Just Red P
void lights_Just_Red_P(int delay_ms) {
    lights(0, 0, 0, 0, 0, 0, 0, 1, delay_ms);
}

// Just Yel P
void lights_Just_Yel_P(int delay_ms) {
    lights(0, 0, 0, 0, 0, 0, 1, 0, delay_ms);
}

void lights_Just_Both_P(int delay_ms) {
  leftights(0, 0, 0, 0, 0, 0, 1, 1, delay_ms);
}

// Just left arm
void lights_Just_LeftArm(int delay_ms) {
    lights(1, 0, 0, 0, 0, 0, 0, 0, delay_ms);
}

// Both Arms illuminated
void lights_BOTH_ARMS(int delay_ms) {
    lights(1, 1, 0, 0, 0, 0, 0, 0, delay_ms);
}

// Both legs illuminated
void lights_BOTH_LEGS(int delay_ms) {
    lights(0, 0, 1, 1, 0, 0, 0, 0, delay_ms);
}

// 1 second count of body flicker
void The_Middle_Flicker() {
    lights_BOTH_LEGS(200);
    lights(0, 0, 0, 0, 0, 1, 0, 0, 200);
    lights_Just_Yel_P(200);
    lights_BOTH_ARMS(200);
    lights(0, 0, 0, 0, 1, 0, 0, 0, 200);
}

// Flicker 2 seconds on Hypnotic
void lights_Vintage_TShirt() {
    lights(1, 1, 1, 1, 1, 0, 1, 0, 200);
    lights(1, 1, 1, 1, 1, 1, 0, 0, 200);
    lights(1, 1, 1, 1, 1, 0, 1, 0, 200);
    lights(1, 1, 1, 1, 1, 1, 0, 0, 200);
    lights(1, 1, 1, 1, 1, 0, 1, 0, 200);
    lights(1, 1, 1, 1, 1, 1, 0, 0, 200);
    lights(1, 1, 1, 1, 1, 0, 1, 0, 200);
    lights(1, 1, 1, 1, 1, 1, 0, 0, 200);
    lights(1, 1, 1, 1, 1, 0, 1, 0, 200);
    lights(1, 1, 1, 1, 1, 1, 0, 0, 200);
}

// 1500 ms of body flickering
void lights_Body_Flicker_2100ms() {
    lights_Just_Yel_P(150);
    lights_ALL_OFF(150);
    lights_Just_Yel_P(150);
    lights_ALL_OFF(150);
    lights_Just_Yel_P(150);
    lights_ALL_OFF(150);
    lights_Just_Yel_P(150);
    lights_ALL_OFF(150);
    lights_Just_Yel_P(150);
    lights_ALL_OFF(150);
    lights_Just_Yel_P(100);
    lights_ALL_OFF(100);
    lights_Just_Yel_P(100);
    lights_ALL_OFF(100);
    lights_Just_Yel_P(100);
    lights_ALL_OFF(100);
}

// 1000 ms of body flickering
void lights_Body_Flicker_1000ms() {
    lights_NO_Ps(100);
    lights_ALL_OFF(100);
    lights_NO_Ps(100);
    lights_ALL_OFF(100);
    lights_NO_Ps(100);
    lights_ALL_OFF(100);
    lights_NO_Ps(100);
    lights_ALL_OFF(100);
    lights_NO_Ps(100);
    lights_ALL_OFF(100);
}

// 1500ms of flickering out
void lights_END_Flicker_1500ms() {
    lights_Just_Yel_P(100); //1
    lights_Just_Both_P(100);
    lights_Just_Red_P(100);
    lights_Just_Yel_P(100); //2
    lights_Just_Both_P(100);
    lights_Just_Red_P(100);
    lights_Just_Yel_P(100); //3
    lights_Just_Both_P(100);
    lights_Just_Red_P(100);
    lights_Just_Yel_P(100); //4
    lights_Just_Both_P(100);
    lights_Just_Red_P(100);
    lights_Just_Yel_P(100); //5
    lights_Just_Both_P(100);
    lights_Just_Red_P(100);
}
'''

# Translate suit number to desired column
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
    function_call = "  lights_" + preset_name + "(" + str(duration) + ");\n"
    return function_call


def lights2code(left_arm,right_arm,left_leg,right_leg,head_back,white_bottom,yellow_p,red_p,duration):
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

    filename = sys.argv[1]

    # Open csv file
    csvfile = open(filename, newline='')
    csvreader = csv.reader(csvfile)

    # Calculate number of glowsuits mapped in csv file
    num_suits = (len(next(csvreader, None)) - NUM_HEADER) // NUM_SETTINGS
    # Array to store a loop string for each glowsuit
    ino_loops = []

    # Initialize all glowsuit loops with loop begin
    for suit in range(num_suits):
        ino_loops.append(LOOP_BEGIN)
    
    prev_row = next(csvreader, None)
    prev_abs_time = prev_row[TIME_ABS_COL]
    # Loop over every row in the CSV
    for row in csvreader:

        # calculate the delay in milliseconds from previous lights
        delay_ms = int(row[TIME_ABS_COL]) - int(prev_abs_time)
        for suit in range(num_suits):
            # Preset is set
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
        prev_abs_time = int(row[TIME_ABS_COL])

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

