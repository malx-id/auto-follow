'''
Name   : Auto Follow
Mulai  : 26-07-2020 -> 20.08
Selwsai: 26-07-2020 -> 21.20
Author : Akmal ID
'''

from bs4 import BeautifulSoup as par
from headerz import headerz
import requests as req
import os

# Main
def follow():
    cookie = parser_cookie()
    me = req.get('https://free.facebook.com', cookies=cookie)
    if 'Harap Konfirmasikan Identitas Anda' in me.text:
        print('     Sepertinya Anda Terkunci Sementara!');exit()
    elif 'Buat Akun Baru' in me.text:
        print('     Invalid Cookie!');exit()
    else:
        pass

    try:
        page_follow = req.get('https://free.facebook.com/willer.jancox', cookies=cookie)
        parser = par(page_follow.text, 'html.parser')
        ikuti = parser.find('a', string='Ikuti')['href']
        req.get('https://free.facebook.com'+ikuti, cookies=cookie)
        print('     Sukses Mengikuti.')
    except TypeError:
        print('     Telah Di Ikuti')

def parser_cookie():
    try:
        file = open('cookie.log', 'r').read()
        head = headerz().parser(file)
        kuki = headerz().cookie_builder(head['cookie'])
        return {'cookies':kuki}
    except FileNotFoundError:
        print('     Silahkan Simpan Cookie di File Dengan Nama \'cookie.log\'')
        print('\n     Jika Anda tidak tau cara mengambil cookie silahkan lihat di link ini: https://pandasid.blogspot.com/2020/05/cara-mendapatkan-cookie-facebook-dengan.html?m=1')
        exit()

if __name__ == '__main__':
    os.system('clear')
    print('''
        O        o          o--o     o o                  o--o o--o
       / \       |          |        | |                  |    |   |
      o---oo  o -o- o-o     O-o  o-o | | o-o o   o   o    O-o  O--o
      |   ||  |  |  | |     |    | | | | | |  \ / \ /     |    |   |
      o   oo--o  o  o-o     o    o-o o o o-o   o   o      o    o--o
            ''')
    follow()
