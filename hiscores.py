class TimeObject:
    def __init__(self, minutes, seconds, name):

        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self.name = name

hiscores_file = open("hiscores.txt", "r")

times = []

for line in hiscores_file:
    list_of_lines = line.split(" ")
    name = list_of_lines[1]
    minutes = list_of_lines[3][:-1]
    seconds = list_of_lines[4].rstrip()[:-2]
    time = TimeObject(minutes, seconds, name)

    times.append(time)

#   Creates a timeObject for the new player
minutes = 13
seconds = 11
name = "Viktor"

t = TimeObject(minutes, seconds, name)

times.append(t)

times = sorted(times, key=lambda x: x.minutes)

str_to_file = ""

for i, time in enumerate(times):
    str_to_file += str(i + 1) + ". " + time.name + " - " + str(time.minutes) + "m " + str(time.seconds) + "s.\n"

hiscores_file = open("hiscores.txt", "w")

hiscores_file.write(str_to_file)
