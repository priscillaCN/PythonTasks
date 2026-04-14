"""A program that converts seconds to hour, minute and seconds"""

second = 1
minute = 60
hour = 3600 

numberofseconds = input(int('Enter number of seconds: '))
numberofhours = numberof seconds // hour
remainingseconds = number of seconds % hour
numberofminutes = remainingseconds // minute
numberofseconds = remainongseconds % minute

print(numberofhours, 'hour ', numberofminutes, 'minutes ', numberofseconds, 'seconds')