import random

TGREEN   =  '\033[32m' # Green Text
TGRED    =  '\033[31m' # Red Text
TYELLOW  =  '\033[33m' # Yellow Text
ENDC     =  '\033[m' # reset to the defaults


def suffled_list():
    m2List = list(range(2, 10)) 
    random.shuffle(m2List)
    return m2List


def getvoto(esatte, domande):
    return (esatte * 10) / domande


name = input('Ciao! Come ti chiami? > ')
print('Ciao %s :) Adesso giochiamo insieme alle tabelline!' % name)
answer = input('Un numero per una tabellina, t per tutte > ')

m2List = []

risposte_esatte = 0
curr_num_domande = 0

while 1:
    
    if not m2List:
        m2List = suffled_list()

    m2 = m2List.pop()
    if answer == 't':
        m1 = random.randrange(2, 10)
    else:
        m1 = int(answer)
 
    result = input('\n%2d) - Quanto fa %d x %d ? ' % (curr_num_domande + 1, m1, m2))

    if result == 'stop':
        break
    elif int(result) == m1 * m2:
        risposte_esatte += 1
        print(TGREEN + 'Esatto!!!', ENDC)
    else:
        print(TGRED + 'Sbagliato. %d x %d = %d' % (m1, m2, m1 * m2), ENDC)

    curr_num_domande += 1

    if curr_num_domande % 5 == 0:
        voto = getvoto(risposte_esatte, curr_num_domande)
        #print('Voto parziale > %.1f' % voto)
        if voto < 6:
            print(TGRED + '\n%s non stai andando benissimo, proviamo a migliorare un pò!' % name, ENDC)
        elif voto >= 6 and voto < 9:
            print(TYELLOW + '\nStai andando bene, ma puoi migliorare ancora... forza %s!' % name, ENDC)
        else:
            print(TGREEN + f'\n{name} sei super! Continua così!', ENDC)


voto = getvoto(risposte_esatte, curr_num_domande)
print('%s hai risposto correttamente a %d domande su %d. Il tuo voto finale é %.1f' % (name, risposte_esatte, curr_num_domande, voto))

if voto < 6:
    print(TGRED + 'Puoi fare di meglio! Continua a giocare!', ENDC)
elif voto >= 6 and voto < 9:
    print(TYELLOW + 'Ottimo molto brava! Adesso ti devi superare e diventare ancora più brava!', ENDC)
else:
    print(TGREEN + 'Sei super, le tabelline per te non hanno segreti!', ENDC)

