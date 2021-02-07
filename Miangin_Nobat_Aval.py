# Barneme Miangin Nomarat Nobat Aval 11th
# Created By: Hossein Habibi
# Robot Telegrami: @HelliTaskBot
# Date: 1399-11-19

books_r = {
    'az-oloom': {'zarib': 1, 'nomarat': None},
    'amar': {'zarib': 2, 'nomarat': None},
    'mohit': {'zarib': 2, 'nomarat': None},
    'tarikh': {'zarib': 2, 'nomarat': None},
    'varzesh': {'zarib': 2, 'nomarat': None},
    'dini': {'zarib': 2, 'nomarat': None},
    'hesaban': {'zarib': 3, 'nomarat': None},
    'zaban': {'zarib': 3, 'nomarat': None},
    'zamin': {'zarib': 2, 'nomarat': None},
    'shimi': {'zarib': 3, 'nomarat': None},
    'araby': {'zarib': 2, 'nomarat': None},
    'farsi': {'zarib': 2, 'nomarat': None},
    'fizik': {'zarib': 4, 'nomarat': None},
    'karaf': {'zarib': 2, 'nomarat': None},
    'negaresh': {'zarib': 1, 'nomarat': None},
    'hendeseh': {'zarib': 2, 'nomarat': None},
    'enzebat': {'zarib': 2, 'nomarat': None},
}

books_t = {
    'az-oloom': {'zarib': 1, 'nomarat': None},
    'amar': {'zarib': 2, 'nomarat': None},
    'mohit': {'zarib': 2, 'nomarat': None},
    'tarikh': {'zarib': 2, 'nomarat': None},
    'varzesh': {'zarib': 2, 'nomarat': None},
    'dini': {'zarib': 2, 'nomarat': None},
    'hesaban': {'zarib': 3, 'nomarat': None},
    'zaban': {'zarib': 3, 'nomarat': None},
    'zamin': {'zarib': 2, 'nomarat': None},
    'shimi': {'zarib': 3, 'nomarat': None},
    'araby': {'zarib': 2, 'nomarat': None},
    'farsi': {'zarib': 2, 'nomarat': None},
    'fizik': {'zarib': 4, 'nomarat': None},
    'karaf': {'zarib': 2, 'nomarat': None},
    'negaresh': {'zarib': 1, 'nomarat': None},
    'hendeseh': {'zarib': 2, 'nomarat': None},
    'enzebat': {'zarib': 2, 'nomarat': None},
}

def miangin(books):
    wazn = 0
    nomarat = 0
    for i in books:
        wazn += books[i]['zarib']
    for i in books:
        if books[i]['nomarat'][0] == 0:
            nomarat += books[i]['nomarat'][1] * books[i]['zarib']
        else:
            nomarat += ((books[i]['nomarat'][0] + books[i]['nomarat'][1]*2) / 3) * books[i]['zarib']
    return round(nomarat/wazn, 2)



text = """Barneme Miangin Nomarat Nobat Aval 11th
* Created By: Hossein Habibi
* Robot Telegrami: @HelliTaskBot

Age Barname Moshkeli Dasht Be Man Toie Telegram Payam Bedid: @hossein_habibi_2004

Rahnama:
    * Nomre Khodetoon Ro Be Format Moghabel Vared Konid ~> Mosatamar-Payani
        - Book Name [zarib] ~> 19.75-18.25
            * Agar Darsi Nomre Mostamar Nadasht Addad 0 Ro Vared Konid.
    * Baraye Khoroog Az Barname Faghat [Enter] Ro Bezanid.

------------------------------------------------------------------------------------"""

print(text)

reshte = input(u'Lotfan Reshte Khodetoon Ro Vared Konid. [R/T] ~> ')
try:
    if reshte.upper() == 'R':
        books = books_r
    elif reshte.upper() == 'T':
        books = books_t
    else:
        input('Reshte Mored Nazar Yaft Nashod (404) :!')
        exit()
except:
    exit()

print('\nLotfan Nomre Khodetoon Ro Dar Har Dars Vared Konid.')
for i in books:
    nomarat = input("{name} [{zarib}] ~> ".format(name=i.ljust(8), zarib=books[i]['zarib']))
    if nomarat == '':
        exit()
    elif not('-' in nomarat) or (len(nomarat.split('-')) != 2):
        input('Lotfan Dar Vared Kardan Nomre Khod Deghat Konid :!')
        exit()
    else:
        try:
            for nomre in nomarat.split('-'):
                if not(0 <= float(nomre) <= 20):
                    input('Lotfan Dar Vared Kardan Nomre Khod Deghat Konid :!')
                    exit()
            books[i]['nomarat'] = [float(nomre) for nomre in nomarat.split('-')]
        except:
            input('Error :!')
            exit()


print(f'\n* Mo\'adel Shoma: {miangin(books)}\n* Robot Telegrami: @HelliTaskBot')
input('\n* Baraye Khoroog Az Barname [Enter] Ro Bezanid. \n  Rooz Khosh :)')
