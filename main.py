import pyautogui, time

mesaj = input("Spamlanacak mesajı gir: ")
spam_adeti = int(input("Mesajı kaç kere spamlamak istiyorsunuz: "))
print("Spamlamak istediğiniz yeri seçiniz, program 5 saniye içinde spama başlayacak")
time.sleep(5)

for i in range(spam_adeti):
		
	pyautogui.typewrite(mesaj)
	pyautogui.press('enter')
	time.sleep(0.5)
