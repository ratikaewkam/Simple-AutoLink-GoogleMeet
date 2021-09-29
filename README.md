# Simple-AutoLink-GoogleMeet
ตัวอย่างโปรแกรมเข้าเรียนอัตโนมัติเบื้องต้นด้วยโค้ดภาษา Python เพียงไม่กี่บรรทัด

## เครื่องมือที่ใช้
* Python 3

## การติดตั้ง Library
การติดตั้ง webbrowser
``` bash
pip install webbrowser
```
การติดตั้ง pyautogui
``` bash
pip install pyautogui
```

## เริ่มต้นเขียนโปรแกรม
* ทำการ import library สำหรับการเปิดเว็บเบราว์เซอร์
``` python
import webbrowser
```

* เขียนโปรแกรมเพื่อเปิดลิงค์ที่ต้องการ
```python
webbrowser.open_new_tab('Link') #ใส่ลิงค์ google meet
```

* ทำการ import library สำหรับให้โปรแกรมควบคุมคียบอร์ดและเมาส์ได้
```python
import pyautogui
```

* เมื่อสามารถเข้าลิงค์ได้แล้ว ต่อไปจะควบคุมให้โปรแกรมสามารถปิดไมค์และกล้องก่อนการประชุมได้ ถ้าท่านใดไม่ต้องการฟีเจอร์นี้สามารถลบส่วนนี้ได้
```python
pyautogui.hotkey('ctrl','e') #สำหรับปิดกล้อง
pyautogui.hotkey('ctrl','d') #สำหรับปิดไมค์
```

* จากนั้นทำการ import time เพื่อ delay การทำงานของโปรแกรม
```python
import time
```

* และทำการเขียนโปรแกรมเพื่อ delay การทำงานโปรแกรมในบางส่วน และสามารถเพิ่มเวลาในการ delay ได้ ซึ่งแล้วแต่ความเร็วของเครื่องคอมพิวเตอร์และอินเทอร์เน็ต
```python
import webbrowser
import pyautogui
import time

webbrowser.open_new_tab('Link') #ใส่ลิงค์ google meet
time.sleep(5)

pyautogui.hotkey('ctrl','e') #สำหรับปิดกล้อง
pyautogui.hotkey('ctrl','d') #สำหรับปิดไมค์
time.sleep(1)
```

* ต่อมาทำการ import library ที่ใช้ในการหาตำแหน่งของสิ่งที่ต้องการหาที่อยู่ในหน้าจอ
```python
from pyscreeze import locateOnScreen
```

* จากนั้นให้ทำการแคปภาพตรงที่ให้เข้าร่วมการประชุม แล้วบันทึกไว้ และบันทึกที่อยู่ของภาพนั้นด้วย

* เขียนโปรแกรมหาตำแหน่งของสิ่งที่ตรงกับภาพที่เตรียมไว้ 
```python
position_file = pyautogui.locateOnScreen('Path')
```

* เมื่อโปรแกรมเจอตำแหน่งของสิ่งนั้นแล้ว ต่อมาจะให้โปรแกรมเคลื่อนไปยังตำแหน่งดังกล่าว และคลิกตำแหน่งนั้น
```python
pyautogui.moveTo(position_file)
pyautogui.click(position_file)
```

* กด run เพื่อทดสอบโปรแกรม หากทำงานช้าหรือเร็วไปสามารถปรับตรง time.sleep() ได้

## สรุปโค้ดทั้งหมด
```python
import webbrowser
import pyautogui
import time
from pyscreeze import locateOnScreen

webbrowser.open_new_tab('Link') #ใส่ลิงค์ google meet
time.sleep(5)

pyautogui.hotkey('ctrl','e') #สำหรับปิดกล้อง
pyautogui.hotkey('ctrl','d') #สำหรับปิดไมค์
time.sleep(1)

position_file = pyautogui.locateOnScreen('Path')
pyautogui.moveTo(position_file)
pyautogui.click(position_file)
```

## สุดท้าย
จากที่ได้เขียนโปรแกรมในเบื้องต้น เราจะพบว่าการเขียนโปรแกรมนั้นไม่ใช่เรื่องยากและการนำไปใช้ในเบื้องต้นก็ไม่ได้ใช้โค้ดหลายบรรทัดเลย ทางผู้พัฒนาหวังว่าตัวอย่างโค้ดในครั้งนี้จะมีประโยชน์กับบุคคลที่มีการประชุมหรือเรียนออนไลน์ในสถานการณ์โควิด 19 ดังนั้นถ้าเราเขียนโปรแกรมไว้ให้ทำงานอัตโนมัติ เราจะได้ไม่ต้องมาเสียเวลาคลิกเปิดแท็บหรือลิงค์ต่างๆ และหากโปรแกรมทำงานช้าหรือเร็วเกินไป สามารถแก้ไขได้ตามวิธีด้านบนเลยนะครับ และหากใครสนใจนำไปพัฒนาต่อยอดให้ดียิ่งขึ้นสามารถนำไปพัฒนาต่อได้ทันทีเลยครับผม สุดท้ายหากทางผู้พัฒนาทำผิดพลาดประการใดต้องขออภัยด้วยครับผม