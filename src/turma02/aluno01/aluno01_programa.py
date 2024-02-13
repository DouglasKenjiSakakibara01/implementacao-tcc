def tique(hours, minutes, seconds):
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
                if hours == 24:
                    hours = 0
        return hours, minutes, seconds
 