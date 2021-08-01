datetime-notify.py - Python-скрипт, вызывающий всплывающее окно в стистеме у каждого активного пользователя.
datetime-notify.service - Сервис, запускающий datetime-notify.py
datetime-notify.timer - Таймер, каждую минуту запускающий datetime-notify.service.
====================================
datetime-notify.service и datetime-notify.timer были расположены в пути "/etc/systemd/system"
datetime-notify.py расположен в "/usr/bin"

Для datetime-notify.py прописаны права "chmod ugo+rwx"
datetime-notify.service и datetime-notify.timer включены в автозапуск через systemctl.
