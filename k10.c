#include "unihiker_k10.h"
// 函数声明
void onButtonAPressed();
// 创建对象
UNIHIKER_K10 k10;
uint8_t      screen_dir=2;


// 主程序开始
void setup() {
	k10.begin();
	k10.initScreen(screen_dir);
	k10.creatCanvas();
	k10.buttonA->setPressedCallback(onButtonAPressed);
	Serial.begin(115200);
	delay(1000);
}
void loop() {
	if ((Serial.available())) {
		k10.canvas->canvasClear(1);
		k10.canvas->canvasText(Serial.readStringUntil('\n'), 1, 0x0000FF);
		k10.canvas->updateCanvas();
	}
}


// 事件回调函数
void onButtonAPressed() {
	while (1) {
		if ((k10.buttonA->isPressed())) {
			Serial.println("space");
		}
	}
}