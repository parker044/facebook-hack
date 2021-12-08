print('Selamat Datang')
import requests,os
def cekip()
        print(f'[!] Mendapatkan IP..')
        re = requests.get('https://github.com/parker044/parker044').json()
        ip = re['ip']
        print(f'[!] IP kamu :{ip}')

def iOsif():
        print(f'(!) Menginstall tools parker..')
        os.sistem('pkg update upgrade')
        os.sistem('pkg install git python2')
        os.sistem('git clone https://github.com/parker044/parker044')
        os.sistem('cd PARKER')
        os.sistem('pip2 install -r requirements.txt')
        os.sistem('python2 parker.py')



        print('''-=[MyTools]=-
           [Menu]
        [1] Cek IP
        [2] Install Osif
        [3] Keluar
        ''')
menu = input('[!] Silahkan pilih menu:')
if menu =='1':
    cekip()
elif menu =='2':
    iOsif()
elif menu =='3'
print ('[?]Keluar')
sys.exit()
else:
print('[?] Perintah tidak diketahui..')
sys.exit()
