import random

TGREEN =  '\033[32m' # Green Text
TGRED  =  '\033[31m' # Red Text
ENDC   =  '\033[m' # reset to the defaults

name = input('Ciao! Come ti chiami? > ')
print('Ciao %s :) Adesso giochiamo insieme alle tabelline!' % name)
print('Prima alcune domande...')
answer = input('Un numero per una tabellina, t per tutte > ')
domande = input('Quante volte vuoi essere sfidata %s? > ' % name)

risposteEsatte = 0

for i in range(0, int(domande)):
    
    m2 = random.randrange(2, 10)
    if answer == 't':
        m1 = random.randrange(2, 10)
    else:
        m1 = int(answer)
 
    result = int(input('Quanto fa %d x %d ? ' % (m1, m2)))

    if (result == m1 * m2):
        risposteEsatte += 1
        print(TGREEN + 'Esatto!!!', ENDC)
    else:
        print(TGRED + 'Sbagliato. %d x %d = %d' % (m1, m2, m1 * m2), ENDC)


voto = (risposteEsatte * 10) / int(domande)
print('Hai risposto correttamente a %d domande su %d. Il tuo voto finale é %.1f' % (risposteEsatte, int(domande), voto))