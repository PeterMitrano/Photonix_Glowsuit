
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

void loop() {
  lights_ALL_OFF(4450);
  lights_ALL_OFF(3925);
  lights_ALL_OFF(100);
  lights_ALL_OFF(3365);
  lights_BOTH_LEGS(205);
  lights(0,0,1,1,1,1,0,0,170);
  lights_NO_Ps(436);
  lights_ALL_ON_Yel_P(2353);
  lights_ALL_OFF(100);
  lights_ALL_OFF(2143);
  lights_BOTH_ARMS(6549);
  lights_ALL_OFF(280);
  lights_ALL_OFF(70);
  lights_ALL_OFF(70);
  lights_ALL_OFF(70);
  lights_ALL_ON_Yel_P(351);
  lights_ALL_OFF(70);
  lights_ALL_OFF(70);
  lights_ALL_OFF(70);
  lights_ALL_OFF(351);
  lights_ALL_OFF(560);
  lights_ALL_OFF(1683);
  lights_ALL_ON_Yel_P(1121);
  lights_ALL_OFF(1402);
  lights_BOTH_LEGS(70);
  lights(0,0,1,1,0,1,0,0,70);
  lights(0,0,1,1,1,1,1,0,70);
  lights_ALL_ON_Yel_P(2424);
  lights_BOTH_ARMS(100);
  lights_BOTH_ARMS(1682);
  lights_ALL_OFF(631);
  lights_ALL_OFF(1296);
  lights_ALL_OFF(1227);
  lights_ALL_ON_Yel_P(1302);
  lights_BOTH_LEGS(280);
  lights_ALL_OFF(281);
  lights_ALL_OFF(280);
  lights_ALL_OFF(281);
  lights_ALL_ON_Yel_P(280);
  lights_ALL_ON_Yel_P(280);
  lights_ALL_ON_Yel_P(281);
  lights_ALL_OFF(280);
  lights_ALL_OFF(105);
  lights_ALL_OFF(1647);
  lights_ALL_OFF(211);
  lights(1,1,0,0,1,1,1,0,560);
  lights_ALL_ON_Yel_P(1122);
  lights_ALL_ON_Yel_P(2523);
  lights_ALL_ON_Yel_P(5673);
  lights_ALL_ON_Yel_P(6383);
  lights_ALL_OFF(561);
  lights_ALL_OFF(561);
  lights_ALL_OFF(560);
  lights_ALL_ON_Yel_P(561);
  lights_ALL_ON_Yel_P(140);
  lights_ALL_OFF(421);
  lights_ALL_OFF(140);
  lights_ALL_OFF(140);
  lights_ALL_ON_Yel_P(141);
  lights_ALL_ON_Yel_P(2944);
  lights(1,1,0,0,1,1,1,0,227);
  lights(1,1,0,0,1,0,0,0,333);
  lights_ALL_OFF(386);
  lights_BOTH_ARMS(35);
  lights(1,1,0,0,1,0,1,0,35);
  lights(1,1,0,0,1,1,1,0,35);
  lights_ALL_ON_Yel_P(3995);
  lights_ALL_OFF(561);
  lights_ALL_OFF(140);
  lights_ALL_OFF(140);
  lights_ALL_ON_Yel_P(141);
  lights_ALL_ON_Yel_P(2943);
  lights(0,0,1,1,1,1,1,0,211);
  lights(0,0,1,1,0,1,0,0,175);
  lights_BOTH_LEGS(315);
  lights_ALL_OFF(421);
  lights_ALL_ON_Yel_P(100);
  lights_ALL_OFF(1181);
  lights_ALL_OFF(211);
  lights_ALL_ON_Yel_P(750);
  lights_ALL_OFF(1118);
  lights_ALL_ON_Yel_P(1361);
  lights_ALL_OFF(491);
  lights_ALL_OFF(482);
  lights(0,0,0,0,0,1,0,0,241);
  lights_ALL_OFF(360);
  lights(0,0,0,0,1,0,0,0,299);
  lights(1,1,0,0,1,0,0,0,239);
  lights(1,1,0,0,1,1,1,0,239);
  lights_ALL_ON_Yel_P(4347);
  lights_ALL_OFF(664);
  lights_ALL_OFF(417);
  lights(1,0,0,0,0,0,0,0,536);
  lights(1,0,0,0,0,0,0,0,297);
  lights(1,0,0,0,0,0,0,0,536);
  lights(1,0,0,0,0,0,0,0,476);
  lights(1,0,0,0,0,0,0,0,536);
  lights_BOTH_ARMS(357);
  lights_BOTH_ARMS(9038);
  lights_BOTH_ARMS(238);
  lights_BOTH_ARMS(238);
  lights_ALL_OFF(298);
  lights_ALL_OFF(407);
  lights_ALL_OFF(476);
  lights_ALL_ON_Yel_P(7153);
  lights(1,1,0,0,1,1,1,0,476);
  lights(1,1,0,0,1,0,1,0,476);
  lights(0,0,0,0,1,0,0,0,476);
  lights_ALL_OFF(645);
  lights_ALL_OFF(3760);
  lights_ALL_ON_Yel_P(3691);
  lights_ALL_OFF(476);
  lights(0,1,0,0,0,0,0,0,476);
  lights_ALL_OFF(476);
  lights_ALL_OFF(476);
  lights_ALL_OFF(238);
  lights(0,1,0,0,0,0,0,0,238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights(0,1,0,0,0,0,0,0,238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(239);
  lights_ALL_OFF(238);
  lights_BOTH_ARMS(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights_BOTH_ARMS(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(239);
  lights_ALL_OFF(119);
  lights_BOTH_ARMS(119);
  lights_ALL_OFF(119);
  lights_ALL_OFF(119);
  lights_ALL_OFF(119);
  lights_BOTH_ARMS(119);
  lights_ALL_OFF(119);
  lights_ALL_OFF(119);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(238);
  lights_ALL_OFF(239);
  lights_ALL_ON_Yel_P(100);
  lights_ALL_OFF(1566);
  lights_ALL_OFF(119);
  lights_ALL_OFF(1786);
  lights_ALL_OFF(119);
  lights_ALL_OFF(2024);
  lights_BOTH_ARMS(476);
  lights(1,1,0,0,1,0,1,0,476);
  lights(1,1,0,0,1,1,1,0,476);
  lights(1,1,0,0,1,1,1,0,715);
  lights_ALL_ON_Yel_P(3809);
  lights_ALL_ON_Yel_P(1667);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(29);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(59);
  lights_ALL_ON_Yel_P(60);
  lights_ALL_ON_Yel_P(29);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(30);
  lights_ALL_ON_Yel_P(3260);
  lights_ALL_ON_Yel_P(2822);
  lights_ALL_OFF(1059);
  lights_ALL_OFF(100);
  lights_ALL_ON_Yel_P(253);
  lights_ALL_OFF(1059);
  lights_ALL_OFF(100);
  lights_ALL_OFF(606);
  lights_ALL_ON_Yel_P(706);
  lights_ALL_OFF(705);
  lights_Just_Yel_P(177);
  lights_Just_Red_P(177);
  lights_Just_Yel_P(422);
  lights_ALL_OFF(4519);
  lights_ALL_OFF(353);
  lights_ALL_OFF(352);
  lights_ALL_OFF(353);
  lights_ALL_OFF(4589);
  lights_ALL_OFF(353);
  lights_ALL_OFF(353);
  lights_ALL_ON_Yel_P(353);
  lights_ALL_ON_Yel_P(353);
  lights_ALL_ON_Yel_P(8823);
  lights_ALL_OFF(1059);
  lights_ALL_OFF(353);
  lights_ALL_ON_Yel_P(353);
  lights_ALL_ON_Yel_P(353);
  lights_ALL_ON_Yel_P(353);
  lights_ALL_OFF(1411);
  lights_BOTH_ARMS(1412);
  lights_BOTH_ARMS(1412);
  lights_BOTH_ARMS(2813);
  lights_BOTH_LEGS(1412);
  lights_ALL_ON_Yel_P(1422);
  lights_ALL_OFF(1412);
  lights_ALL_ON_Yel_P(1412);
  lights_ALL_ON_Yel_P(1411);
  lights_ALL_ON_Yel_P(1412);
  lights_ALL_ON_Yel_P(2823);
  lights_ALL_OFF(706);
  lights_ALL_OFF(706);
  lights_Just_Red_P(177);
  lights_Just_LeftArm(177);
  lights_ALL_OFF(177);
  lights_Just_RightLeg(177);
  lights(0,1,0,0,0,1,0,0,177);
  lights_Just_LeftLeg(177);
  lights_Just_Yel_P(177);
  lights_Just_RightArm(177);
  lights(0,0,0,0,0,1,0,0,177);
  lights_Just_Red_P(177);
  lights_Just_RightLeg(177);
  lights(0,0,0,0,1,0,0,0,177);
  lights_Just_Yel_P(177);
  lights_ALL_OFF(177);
  lights_Just_LeftArm(125);
  lights_ALL_OFF(574);
  lights_ALL_OFF(353);
  lights_ALL_OFF(352);
  lights_Just_Yel_P(353);
  lights_ALL_OFF(353);
  lights_Just_Red_P(177);
  lights_Just_Yel_P(177);
  lights_Just_Red_P(177);
  lights_Just_Yel_P(177);
  lights_Just_Red_P(177);
  lights_Just_Yel_P(177);
  lights_Just_Red_P(174);
  lights_ALL_ON_Yel_P(11118);
  lights(1,1,0,0,1,1,1,0,176);
  lights(1,1,0,0,0,0,1,0,177);
  lights(1,1,0,0,0,0,0,0,176);
  lights(0,0,0,0,0,0,0,0,177);
  lights_ALL_ON_Yel_P(705);
  lights(1,1,1,1,0,1,0,0,265);
  lights(0,0,1,1,1,1,1,0,265);
  lights(1,1,0,0,1,1,1,0,167);
  lights(1,1,1,1,1,0,1,0,50);
  lights_ALL_ON_Yel_P(665);
  lights(1,1,1,1,0,1,1,0,177);
  lights(0,0,1,1,0,1,1,0,176);
  lights(0,0,1,1,0,0,0,0,177);
  lights_ALL_OFF(176);
  lights_ALL_ON_Yel_P(706);
  lights_ALL_ON_Yel_P(265);
  lights_ALL_ON_Yel_P(264);
  lights_ALL_ON_Yel_P(177);
  lights_ALL_ON_Yel_P(6353);
  lights_Just_Red_P(1764);
  lights_ALL_OFF(89);
  lights_Just_Red_P(1676);
  lights_ALL_OFF(500000);

  // Make sure lights are off
  lights_ALL_OFF(50000);
}

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

// Just right arm
void lights_Just_RightArm(int delay_ms) {
    lights(0, 1, 0, 0, 0, 0, 0, 0, delay_ms);
}

// Just left leg
void lights_Just_LeftLeg(int delay_ms) {
    lights(0, 0, 1, 0, 0, 0, 0, 0, delay_ms);
}

// Just right leg
void lights_Just_RightLeg(int delay_ms) {
    lights(0, 0, 0, 1, 0, 0, 0, 0, delay_ms);
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
