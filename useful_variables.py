"""
This module has random useful variables that dont need to be
recalcuated and generating bugs and stuff
"""
import itertools
from datetime import datetime

start = datetime.now()

def get_hydrophone_pairs():
    hydrophones = [0, 1, 2, 3, 4, 5]
    hydrophone_pairs = [h for h in itertools.combinations(hydrophones, 2)]
    return hydrophone_pairs

def elapsed_time():
    return datetime.now() - start

def make_hydrophone_data_paths(borehole, year, julian_day):
    """
    its annoying to make the paths, this makes it easier
    """
    borehole = borehole.upper()
    paths = ['/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.01.GDH.{year}.{julian_day}'
            ,'/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.02.GDH.{year}.{julian_day}'
            ,'/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.03.GDH.{year}.{julian_day}'
            ,'/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.04.GDH.{year}.{julian_day}'
            ,'/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.05.GDH.{year}.{julian_day}'
            ,'/media/sda/data/robdata/Hydrophones/DAYS/{borehole}00/{borehole}00.7F.06.GDH.{year}.{julian_day}']
    return [p.format(borehole=borehole, year=year, julian_day=julian_day) for p in paths]

if __name__=='__main__':
    print('Nothing to see here. You may go about our business.')