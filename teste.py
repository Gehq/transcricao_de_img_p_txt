# 1. capturar a imagem da tela
import pyscreenshot as ImageGrab
import pytesseract
from PIL import Image
import pyautogui

# variaveis
conta_palavra_sjbpedi = 0
# laco_inifinito
while True:
    # Captura a imagem da tela
    screenshot = ImageGrab.grab()
    # Salva a imagem em um arquivo
    screenshot.save("screenshot.png")

    # 2. transcrever a imagem em texto
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    # Abre a imagem capturada
    image = Image.open("screenshot.png")

    # Transcreve o texto da imagem
    text = pytesseract.image_to_string(image, lang="por")

    # 3. verificar no texto se existe as palavras (sjbal20) ou (sjbpedi)
    # e armazena a quantidade de vezes que as falavras foram encontrdas
    if "sjbal20" in text or "sjbpedi" in text:
        pyautogui.alert("Isso que você está tentando executar já foi executado.")
        conta_palavra_sjbpedi += 1
        if conta_palavra_sjbpedi == 2:
            alerte = pyautogui.confirm("Deseja continuar recebendo os alertas\n CLICK EM OK (PARA NÃO DESEJO)")
            if alerte == "OK":
                conta_palavra_sjbpedi = 0
            else:
                pyautogui.alert("Tudo bem então")


