import datetime as dt
from collections import OrderedDict


def giveDatetime(datestring="2000:01:01 00:00:00.000") -> dt.datetime:
    args = []
    for sub1 in datestring.split():
        for sub2 in sub1.split(":"):
            if "." in sub2:
                args.append(int(sub2.split(".")[0]))
                args.append(int(sub2.split(".")[1]) * 1000)
            else:
                args.append(int(sub2))
    time = dt.datetime(*args)
    return time


def newdate(time, time_old, use_day=True) -> bool:
    # adjust datebreak at midnight
    timedelta = time - time_old
    timedelta_seconds = timedelta.days * 3600 * 24 + timedelta.seconds
    if not time_old.year == time.year or not time_old.month == time.month or (
            use_day and not time_old.day == time.day): newdate.dateswitch = True
    if timedelta_seconds > 3600. * 4 and newdate.dateswitch:
        newdate.dateswitch = False
        return True
    else:
        return False


newdate.dateswitch = False


def dateformating(time=dt.datetime.now(), dateformat=""):
    y = dateformat.count('Y')
    if y > 0: dateformat = dateformat.replace('Y' * y, str(time.year)[-y:])
    if dateformat.count('N') > 0:
        dateformating.numberofDates += 1
        dateformat = _replaceDateID(dateformat, 'N', dateformating.numberofDates)
    dateformat = _replaceDateID(dateformat, 'M', time.month)
    dateformat = _replaceDateID(dateformat, 'D', time.day)
    dateformat = _replaceDateID(dateformat, 'H', time.hour)
    dateformat = _replaceDateID(dateformat, 'm', time.minute)
    dateformat = _replaceDateID(dateformat, 's', time.second)
    dateformat = _replaceDateID(dateformat, 'S', time.microsecond / 1000)
    return dateformat


dateformating.numberofDates = 0


def _replaceDateID(dateformat, search_str, value):
    count = dateformat.count(search_str)
    if count == 0: return dateformat
    return dateformat.replace(search_str * count, ("%0" + str(count) + "d") % value)


def find_dir_with_closest_time(dirDict_firsttime: dict, dirDict_lasttime: dict, time):
    deltaDict = OrderedDict()
    for firsttime, name in dirDict_firsttime.items():
        deltaseconds = abs((time - firsttime).total_seconds())
        deltaDict[deltaseconds] = name
    for lasttime, name in dirDict_lasttime.items():
        deltaseconds = abs((time - lasttime).total_seconds())
        deltaDict[deltaseconds] = name
    deltatime_min = min(deltaDict.keys())
    return deltaDict[deltatime_min]


def printFirstLastOfDirName(dirDict_firsttime: dict, dirDict_lasttime: dict):
    outDict = OrderedDict()
    for time, name in dirDict_firsttime.items():
        outDict[name] = time.strftime("%H:%M")
    for time, name in dirDict_lasttime.items():
        outDict.setdefault(name, "")
        outDict[name] += time.strftime(" - %H:%M \n")
    ofile = open("timetable.txt", 'a')
    for name, value in outDict.items():
        ofile.write(name + "\t" + value)
    ofile.close()
