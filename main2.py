#Kod durmadan çalışır, durdurmak için terminalde "CTRL + C" kombinasyonunu kullanmanız yeterli.
#Kodu çalıştırdıktan sonra "ALT + TAB" ile spamın gerçekleşeceği mesaj barını seçebilirsiniz.

import pyautogui

mesaj = input("Spamlanacak mesajı gir: ")

while True:

	pyautogui.typewrite(mesaj)
	pyautogui.press('enter')
