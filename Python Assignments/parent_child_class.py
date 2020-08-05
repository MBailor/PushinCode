#
#
#        Python 3.8
#
#
#       Author: Mark C Bailor
#
#
#       Puropse: To create to classes that inherit
#       from another class, each child should have
#       at least two attributes of their own.
#
#


class Rider:
    rname = 'Rikki Rakardo'
    racer_number = 27
    home_track = 'Washougal'
     

class Mototcycle(Rider):
    moto_bike = "Kawasaki KLR 650"
    race_class = "450 and up"

class Race_Date(Rider):
    last_race = 'October 24th'
    next_date = 'October 31st'



