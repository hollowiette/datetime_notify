import os
from ntpath import join
import win10toast
from datetime import date, datetime
import locale
from translate import Translator
import ctypes

def date_alert():
    windll = ctypes.windll.kernel32
    language = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

    cur_date = str(datetime.now().date())
    cur_time = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)

    header = "Current date and time"
    body = "Date = {0}, Time = {1}".format(cur_date, cur_time)

    try:
        language = language[0: language.find("_")] if language.find("_") > 0 else language
        translator = Translator(from_lang="En", to_lang=language)
        header = translator.translate(header)
        body = translator.translate(body)
    except:
        pass
    
    # Linux
    # notify-send "Body" "Header"

    toaster = win10toast.ToastNotifier()
    toaster.show_toast(header, body)

if __name__ == "__main__":
    date_alert()