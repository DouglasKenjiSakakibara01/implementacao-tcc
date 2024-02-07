
# função armazena novo horário após passar um segundo
def tique(hora, minuto, segundo):
    horario=[]
    horario.append(hora)
    horario.append(minuto)
    horario.append(segundo)


    for t in [2, 1, 0]:
            if(t == 2):
                # se Segundo é igual a 59, arredonda para 0 e m = True
                # para indicar que deve adicionar uma unidade a Minuto

                # senão, apenas adiciona uma unidade a Segundo
                if(horario[t] == 59):
                    horario[t] = 0
                    m = True
                else:
                    horario[t] += 1
            elif(m and (t == 1)):
                # se m = True, verifica se Minuto é igual a 59: se sim, arredonda
                # para 0 e h = True para indicar que deve adicionar uma unidade a Hora
            
                # se Minuto < 59, apenas adiciona uma unidade a Minuto
                if(horario[t] == 59):
                    horario[t] = 0
                    h = True
                else:
                    horario[t] += 1
            elif(h):
                # se h = True, verifica se Hora é igual a 23: se sim, arredonda
                # para 0; senão, apenas adiciona uma unidade a Hora
                if(horario[t] == 23):
                    horario[t] = 0
                else:
                    horario[t] += 1
        
    return horario[0], horario[1], horario[2]

