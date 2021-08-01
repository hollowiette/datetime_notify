#!/usr/bin/env python
import os, sys
from datetime import date, datetime
import locale
import subprocess

translate_text = {
     "ru": "Текущие дата и время",
     "en": "Current date and time",
     "ca": "Data i hora actuals",
     "cs": "Aktuální datum a čas",
     "et": "Praegune kuupäev ja kellaaeg",
     "de": "Aktuelles Datum und Uhrzeit",
     "it": "Data e ora correnti",
     "lt": "Dabartinė data ir laikas",
     "no": "Gjeldende dato og klokkeslett",
     "es": "Fecha y hora actual",
     "te": "ప్రస్తుత తేదీ మరియు సమయం",
     "ur": "موجودہ تاریخ اور وقت۔",
     "ar": "التاريخ والوقت الحاليان",
     "zh-cn": "当前日期和时间",
     "da": "Nuværende dato og klokkeslæt",
     "tl": "Kasalukuyang petsa at oras",
     "el": "Τρέχουσα ημερομηνία και ώρα",
     "ja": "現在の日時",
     "ms": "Tarikh dan masa semasa",
     "te": "ప్రస్తుత తేదీ మరియు సమయం",
     "ur": "موجودہ تاریخ اور وقت۔",
     "pl": "Aktualna data i godzina",
     "sr": "Тренутни датум и време",
     "sv": "Aktuellt datum och tid",
     "nl": "Huidige datum en tijd",
     "fi": "Nykyinen päivämäärä ja kellonaika",
     "ko": "현재 날짜 및 시간",
     "sk": "Aktuálny dátum a čas",
     "tr": "Geçerli tarih ve saat",
     "bg": "Текуща дата и час",
     "fr": "Date et heure actuelles",
     "ro": "Data și ora curente",
     "sl": "Trenutni datum in ura",
     "uk": "Поточні дата і час",
     "id": "Tanggal dan waktu saat ini",
     "lv": "Pašreizējais datums un laiks",
     "vi": "Ngày và giờ hiện tại",
     "ta": "தற்போதைய தேதி மற்றும் நேரம்",
     "mr": "वर्तमान तारीख आणि वेळ",
     "eo": "Nuna dato kaj horo",
     "hr": "Trenutni datum i vrijeme",
     "tg": "Сана ва вақти ҷорӣ",
     "ml": "നിലവിലെ തീയതിയും സമയവും",
     "zh-tw": "當前日期和時間",
     "iw": "התאריך והשעה הנוכחיים",
     "bn": "বর্তমান তারিখ এবং সময়"
}

def get_active_users():
    users = str(subprocess.check_output("users", shell=True))
    users = users.replace("b\'", " ")
    users = users.replace("\\n'", " ")
    return users.split()

def get_header():
    language = locale.getlocale()[0]
    language = language[0: language.find("_")] if language.find("_") > 0 else language

    header = header = translate_text.get(language) if translate_text.get(language) is not None else "Current date and time"

    return header

def get_body():
    cur_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return cur_date

def date_alert():
    header = get_header()
    body = get_body()
    users = get_active_users()

    for user in users:
        command = "su {0} -c \'notify-send \"{1}\" \"{2}\"\'".format(user, header, body)
        os.system(command)

if __name__ == "__main__":
    date_alert()
