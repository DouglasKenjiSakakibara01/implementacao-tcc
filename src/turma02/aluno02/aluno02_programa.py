
def tique(hours, minutes, seconds):
        time=str(hours)+':'+str(minutes)+':'+str(seconds)
        seconds = int(time.split(":")[-1]) + 1
        if seconds == 60:
            seconds = "0"
            minutes = int(time.split(":")[-2]) + 1
            if minutes == 60:
                minutes = "0"
                hours = int(time.split(":")[0]) + 1
                if hours == 24:
                    hours = "0"
            
        else:
            seconds = int(time[:-2]) + 1
        
        return hours, minutes, seconds
    