# Chris Allulis
# What does this progrma do? 

class Patient(object):
    def __init__(self, id, fullName):
        self.id = 0
        self.fullName =""

    def scheduleTime(self,doctor,timeStart,timeEnd):
        for times in doctor.schedule:
            scheduleMade = False
            time = ""
            print times
            if not doctor.schedule[times]:
                doctor.schedule[times] = True
                time = times
                scheduleMade = True
                break

        if(scheduleMade == False):
            print "No available times :("

        print "Appointment made with Dr. " + doctor.fullName + " at " + time


class Doctor(object):
    def __init__(self,fullName):
        self.fullName = ""
        self.schedule ={ "11:00": False, "11:30": False,
                         "12:00": False,
                         "12:30": False,
                         "1:00": False,
                         "1:30": False,
                         "2:00": False,
                         "2:30": False,
                         "3:00": False,
                         "3:30": False,
                        }


def main():
    a = Doctor("Sullivan")
    print a.schedule
    b = Patient(1,"Chris")

    b.scheduleTime(a,"10:00","3:00")

if __name__ == "__main__":
    main()