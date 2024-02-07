

import datetime
import pytest


def tique(horas, minutos, segundos):
        hora_atual= f"{str(horas)}:{str(minutos)}:{str(segundos)}"
        hora_atual = datetime.datetime.strptime(hora_atual,"%H:%M:%S")
        nova_hora = hora_atual + datetime.timedelta(seconds=1)
        nova_hora=str(nova_hora).split()
        nova_hora= nova_hora[1]
        nova_hora= nova_hora.split(":")

        return int(nova_hora[0]), int(nova_hora[1]), int(nova_hora[2])

   