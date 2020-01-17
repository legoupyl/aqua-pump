from m5stack import *
from m5ui import *
from uiflow import *

class pump (self, startTime,dose):
  def __init__(self):
    self.startTime = startTime
    self.dose = dose
    self.running = False
  def run(self):
    self.running = True
    time.sleep (self.dose)
    self.running = False
    
  def force_run(self):
    self.running = True
    time.sleep (self.dose)
    self.running = False

class screen (self):
  def __init__(self):
      self.main_screen ()
      self.setPump=1


  def main_screen (self):
    Pump1_label = M5TextBox(3, 209, "PUMP1", lcd.FONT_DejaVu24,0xffffff, rotate=0)
    Pump2_label = M5TextBox(115, 208, "PUMP2", lcd.FONT_DejaVu24,0xffffff, rotate=0)
    Pump3_label = M5TextBox(225, 208, "PUMP3", lcd.FONT_DejaVu24,0xffffff, rotate=0)
    Time_label = M5TextBox(20, -3, "Time:", lcd.FONT_DejaVu40,0xf78007, rotate=0)
    dose_label = M5TextBox(19, 49, "Dose:", lcd.FONT_DejaVu40,0x1c1aa6, rotate=0)
    dose_label_unit = M5TextBox(240, 49, "ml", lcd.FONT_DejaVu40,0x5e7185, rotate=0)

    status_label = M5TextBox(44, 125, "SCHEDULE", lcd.FONT_DejaVu40,0x45a306, rotate=0)
    time_label_value = M5TextBox(166, 1, "19:00", lcd.FONT_DejaVu40,0x5e7185, rotate=0)
    dose_label_value = M5TextBox(184, 51, "2", lcd.FONT_DejaVu40,0x5e7185, rotate=0)


  def main_screen_update (self):
    status_label.setText (pumps[self.setPump].status)
    time_label_value.setText(pumps[self.setPump].startTime)
    dose_label_value.setText(pumps[self.setPump].dose)

    
  def force_run(self):
    self.running = True
    time.sleep (self.dose)
    self.running = False


setScreenColor(0x222222)
pumps[1]= pump ("19:00",2)
pumps[2]= pump ("19:00",1)
pumps[3]= pump ("20:00",0)










label0.setColor(0xff0000)


