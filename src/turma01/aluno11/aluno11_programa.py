
def tique(hora, minuto, segundo):
    
    if segundo < 0 or segundo >= 60 or minuto < 0 or minuto >= 60 or hora < 0 or hora >= 24:
        return (-1, -1, -1)

    if segundo < 59:
        return (hora, minuto, segundo + 1)

    if minuto < 59:
        return (hora, minuto + 1, (segundo + 1) % 60)

    if hora < 23:
        return (hora + 1, (minuto + 1) % 60, (segundo + 1) % 60)

    return (0, 0, 0)


