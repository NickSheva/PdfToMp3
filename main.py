"""from PDF to MP3"""
#  Зависимости
import pdfplumber
from art import *
from gtts import gTTS
from pathlib import Path
import time
import os


def pdf_to_mp3(file_path="test.pdf", language='ru'):
    time.sleep(3)
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f"[+] Original file: {Path(file_path).name}")
        print("[+] Processing....")
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:

            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")
        print(f"[+] {file_name}.mp3 has saved successfully\n---Have a good day!---")
        return os.system(f"afplay {file_name}.mp3")
    else:
        return 'File does not exist'


def main():
    tprint("PDF>>T0>>MP3", font="white bubble")
    file_path = input("\nEnter the file's path:\n")
    print(pdf_to_mp3(file_path=file_path))


if __name__ == '__main__':
    main()
