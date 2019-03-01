import os
import string
import csv


#change column values here
time_abs_col = 1
p1_preset_col = 5
p2_preset_col = p1_preset_col + 9
p3_preset_col = p2_preset_col + 9
p4_preset_col = p3_preset_col + 9

def lights2code(left_arm,right_arm,left_leg,right_leg,head_back,white_bottom,yellow_p,red_p,duration):
    return ""


#beginning of loop() function
ino_loop_begin = '''
void loop() {
'''

#initialize each person's loops
ino_loop_p1 = ino_loop_begin
ino_loop_p2 = ino_loop_begin
ino_loop_p3 = ino_loop_begin
ino_loop_p4 = ino_loop_begin

with open('../KDA_V_1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None) # skip headers
    for row in csvreader:
        # handle P1
        ino_loop_p1 += row[p1_preset_col] + "\n"
        ino_loop_p1 += lights2code(row[p1_preset_col+1],\
                                   row[p1_preset_col+2],\
                                   row[p1_preset_col+3],\
                                   row[p1_preset_col+4],\
                                   row[p1_preset_col+5],\
                                   row[p1_preset_col+6],\
                                   row[p1_preset_col+7],\
                                   row[p1_preset_col+8],2)
        # handle P2
        ino_loop_p2 += row[p2_preset_col] + "\n"
        # handle P3
        ino_loop_p3 += row[p3_preset_col] + "\n"
        # handle P4
        ino_loop_p4 += row[p4_preset_col] + "\n"

#ending of loop() function
ino_loop_end = '''
  lights_ALL_OFF(50000);
  //Ending delay, so stays off "forever"
}
'''
#finalize each person's loops
ino_loop_p1 = ino_loop_p1 + ino_loop_end
ino_loop_p2 = ino_loop_p2 + ino_loop_end
ino_loop_p3 = ino_loop_p3 + ino_loop_end
ino_loop_p4 = ino_loop_p4 + ino_loop_end


ino_setup = '''
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

ino_lights = '''
// Delay in ms
void lights(bool A, bool B, bool C, bool D, bool E, bool F, bool G, bool H, int del) {
  digitalWrite(2, A);
  digitalWrite(3, B);
  digitalWrite(4, C);
  digitalWrite(5, D);
  digitalWrite(6, E);
  digitalWrite(7, F);
  digitalWrite(8, G);
  digitalWrite(9, H);
  delay(del);
}

// All lights off
void lights_ALL_OFF(int del) {
  lights(0, 0, 0, 0, 0, 0, 0, 0, del);
}

// Everything on w/ Yellow P (no red P)
void lights_ALL_ON_Yel_P(int del) {
  lights(1, 1, 1, 1, 1, 1, 1, 0, del);
}

// Everything on w/ Red P (no yellow P)
void lights_ALL_ON_Red_P(int del) {
  lights(1, 1, 1, 1, 1, 1, 0, 1, del);
}

// Everything on but the Ps
void lights_NO_Ps(int del) {
  lights(1, 1, 1, 1, 1, 1, 0, 0, del);
}

// Just Red P
void lights_Just_Red_P(int del) {
  lights(0, 0, 0, 0, 0, 0, 0, 1, del);
}

// Just Yel P
void lights_Just_Yel_P(int del) {
  lights(0, 0, 0, 0, 0, 0, 1, 0, del);
}

void lights_Just_Both_P(int del) {
  lights(0, 0, 0, 0, 0, 0, 1, 1, del);
}

// Just left arm
void lights_Just_LeftArm(int del) {
  lights(1, 0, 0, 0, 0, 0, 0, 0, del);
}

// Both Arms illuminated
void lights_BOTH_ARMS(int del) {
  lights(1, 1, 0, 0, 0, 0, 0, 0, del);
}

// Both legs illuminated
void lights_BOTH_LEGS(int del) {
  lights(0, 0, 1, 1, 0, 0, 0, 0, del);
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

ino_total_p1 = ino_setup + ino_loop_p1 + ino_lights
ino_total_p2 = ino_setup + ino_loop_p2 + ino_lights
ino_total_p3 = ino_setup + ino_loop_p3 + ino_lights
ino_total_p4 = ino_setup + ino_loop_p4 + ino_lights
print(ino_total_p1)
print(ino_total_p2)
print(ino_total_p3)
print(ino_total_p4)