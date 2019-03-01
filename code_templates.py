'''Templated code to add to final .ino file.'''

# Code strings templates
LOOP_BEGIN = '''
void loop() {
'''

LOOP_END = '''
  // Make sure lights are off
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
    lights(0, 0, 0, 0, 0, 0, 1, 1, delay_ms);
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
