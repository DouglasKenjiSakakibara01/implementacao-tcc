def tique(horas, minutos, segundos):
        segundos += 1
        if segundos >= 59:
            segundos = 00
            minutos += 1
            if minutos >= 59:
                minutos = 00
                horas += 1
                if horas >= 24:
                    horas = 00
        return horas, minutos, segundos


