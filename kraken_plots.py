'''Import modules'''
import numpy as np
from mpl_interactions import ioff, panhandler, zoom_factory
import matplotlib.pyplot as plt

'''Read the file'''
#log = open("/home/cms/kraken_monitor_plots/x2o_versal-monitor.log", "r") # ucla computers
log = open("c:/Users/jobro/Kraken/x2o_versal-monitor.log")  # home computer
monitor = log.readlines()
log.close()

'''Read the timestamps from the file'''
timestamps_labels = []

for entry in monitor:
    timestamps__end = entry.index("  ")
    timestamps__label = entry[0:timestamps__end]
    timestamps_labels.append(timestamps__label)

# list of timestamps spaced 6hrs apart for plotting
timestamps_labels_6hr = timestamps_labels.copy()
for i in range(len(timestamps_labels_6hr)):
    sHr = timestamps_labels_6hr[i][-8:-6]
    nHr = int(sHr)
    if nHr % 6 != 0:
        timestamps_labels_6hr[i] = ""
timestamps_labels_6hr[1] = ""
timestamps_labels_6hr[0] = timestamps_labels[0]
timestamps_labels_6hr[5] = timestamps_labels[5]

# convert the timestamp string to a numerical value in an array for plotting
second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
month = 30 * day

time_coeffs = np.array([month, day, hour, minute, second])

timestamps_in_seconds = []

for T in timestamps_labels:
    nTime = T.split("-")                                    # splitting along all delimiters
    nTime_1 = nTime[-1].split("_")
    nTime_2 = nTime_1[-1].split(":")

    nTime.pop(-1)
    nTime.extend(nTime_1)
    nTime.pop(-1)
    nTime.extend(nTime_2)

    # converting list of strings to array of ints
    # year
    nTime.pop(0) # getting rid of year entry (always 2025)

    # month
    if nTime[0] == "Jun":
        nTime[0] = 0
    elif nTime[0] == "Jul":
        nTime[0] = 1

    # day through second
    for i in range(1, len(nTime)):
        nTime[i] = int(nTime[i])
    
    nTime_arr = np.array(nTime)

    # calculate total number of seconds since start
    nT = np.dot(nTime_arr, time_coeffs)

    timestamps_in_seconds.append(nT)
    timestamps_nonzeroed = np.array(timestamps_in_seconds)

# zeroing
timestamps = timestamps_nonzeroed - timestamps_nonzeroed[0]

'''Yay!!! Done with creating my timestamp array!!!'''

'''Rails!!!'''
# list of zeroes to add for placeholders!
zeros = np.zeros(shape=len(monitor), dtype=float)

# V_0V8_CORE
V_0V8_CORE__v_list = []
V_0V8_CORE__i_list = []
V_0V8_CORE__p_list = []
V_0V8_CORE__t1_list = []
V_0V8_CORE__t2_list = []
V_0V8_CORE__t3_list = []
V_0V8_CORE__t4_list = []
V_0V8_CORE__t5_list = []

for rail in monitor:
    V_0V8_CORE__label = rail.index("0V8_CORE")
    V_0V8_CORE__start = rail.index(":", V_0V8_CORE__label) + 1
    V_0V8_CORE__end = rail.index("  ", V_0V8_CORE__label)
    V_0V8_CORE__string = rail[V_0V8_CORE__start: V_0V8_CORE__end]

    V_0V8_CORE__list = V_0V8_CORE__string.split(",")
    for i in range(len(V_0V8_CORE__list)):
        V_0V8_CORE__list[i] = float(V_0V8_CORE__list[i])

    for i in range(len(V_0V8_CORE__list)):
        if i == 0:
            V_0V8_CORE__v_list.append(V_0V8_CORE__list[i])
        if i == 1:
            V_0V8_CORE__i_list.append(V_0V8_CORE__list[i])
        if i == 2:
            V_0V8_CORE__p_list.append(V_0V8_CORE__list[i])
        if i == 3:
            V_0V8_CORE__t1_list.append(V_0V8_CORE__list[i])
        if i == 4:
            V_0V8_CORE__t2_list.append(V_0V8_CORE__list[i])
        if i == 5:
            V_0V8_CORE__t3_list.append(V_0V8_CORE__list[i])
        if i == 6:
            V_0V8_CORE__t4_list.append(V_0V8_CORE__list[i])
        if i == 7:
            V_0V8_CORE__t5_list.append(V_0V8_CORE__list[i])

V_0V8_CORE = np.vstack((V_0V8_CORE__v_list, V_0V8_CORE__i_list, V_0V8_CORE__p_list, V_0V8_CORE__t1_list,
                        V_0V8_CORE__t2_list, V_0V8_CORE__t3_list, V_0V8_CORE__t4_list, V_0V8_CORE__t5_list))

# V_0V92_MGTVCC
V_0V92_MGTVCC__v_list = []
V_0V92_MGTVCC__i_list = []
V_0V92_MGTVCC__p_list = []
V_0V92_MGTVCC__t1_list = []
V_0V92_MGTVCC__t2_list = []
V_0V92_MGTVCC__t3_list = []

for rail in monitor:
    V_0V92_MGTVCC__label = rail.index("0V92_MGTVCC")
    V_0V92_MGTVCC__start = rail.index(":", V_0V92_MGTVCC__label) + 1
    V_0V92_MGTVCC__end = rail.index("  ", V_0V92_MGTVCC__label)
    V_0V92_MGTVCC__string = rail[V_0V92_MGTVCC__start: V_0V92_MGTVCC__end]

    V_0V92_MGTVCC__list = V_0V92_MGTVCC__string.split(",")
    for i in range(len(V_0V92_MGTVCC__list)):
        V_0V92_MGTVCC__list[i] = float(V_0V92_MGTVCC__list[i])

    for i in range(len(V_0V92_MGTVCC__list)):
        if i == 0:
            V_0V92_MGTVCC__v_list.append(V_0V92_MGTVCC__list[i])
        if i == 1:
            V_0V92_MGTVCC__i_list.append(V_0V92_MGTVCC__list[i])
        if i == 2:
            V_0V92_MGTVCC__p_list.append(V_0V92_MGTVCC__list[i])
        if i == 3:
            V_0V92_MGTVCC__t1_list.append(V_0V92_MGTVCC__list[i])
        if i == 4:
            continue                                        # zeros
        if i == 5:
            V_0V92_MGTVCC__t2_list.append(V_0V92_MGTVCC__list[i])
        if i == 6:
            V_0V92_MGTVCC__t3_list.append(V_0V92_MGTVCC__list[i])
        if i == 7:
            continue                                        # zeros

V_0V92_MGTVCC = np.vstack((V_0V92_MGTVCC__v_list, V_0V92_MGTVCC__i_list, V_0V92_MGTVCC__p_list, V_0V92_MGTVCC__t1_list, 
                           V_0V92_MGTVCC__t2_list, V_0V92_MGTVCC__t3_list, zeros, zeros))

# 12V0
V_12V0__v_list = []

for rail in monitor:
    V_12V0__label = rail.index("12V0")
    V_12V0__start = rail.index(":", V_12V0__label) + 1
    V_12V0__end = rail.index("  ", V_12V0__label)
    V_12V0__string = rail[V_12V0__start: V_12V0__end]

    V_12V0__list = V_12V0__string.split(",")
    for i in range(len(V_12V0__list)):
        V_12V0__list[i] = float(V_12V0__list[i])

    V_12V0__v_list.append(V_12V0__list[0])

V_12V0 = np.vstack((V_12V0__v_list, zeros, zeros, zeros, 
                    zeros, zeros, zeros, zeros))

# V_1V1_DDR
V_1V1_DDR__v_list = []

for rail in monitor:
    V_1V1_DDR__label = rail.index("1V1_DDR")
    V_1V1_DDR__start = rail.index(":", V_1V1_DDR__label) + 1
    V_1V1_DDR__end = rail.index("  ", V_1V1_DDR__label)
    V_1V1_DDR__string = rail[V_1V1_DDR__start: V_1V1_DDR__end]

    V_1V1_DDR__list = V_1V1_DDR__string.split(",")
    for i in range(len(V_1V1_DDR__list)):
        V_1V1_DDR__list[i] = float(V_1V1_DDR__list[i])

    V_1V1_DDR__v_list.append(V_1V1_DDR__list[0])

V_1V1_DDR = np.vstack((V_1V1_DDR__v_list, zeros, zeros, zeros, 
                       zeros, zeros, zeros, zeros))

# V_1V2_MGTVTT
V_1V2_MGTVTT__v_list = []
V_1V2_MGTVTT__i_list = []
V_1V2_MGTVTT__p_list = []
V_1V2_MGTVTT__t1_list = []
V_1V2_MGTVTT__t2_list = []
V_1V2_MGTVTT__t3_list = []

for rail in monitor:
    V_1V2_MGTVTT__label = rail.index("1V2_MGTVTT")
    V_1V2_MGTVTT__start = rail.index(":", V_1V2_MGTVTT__label) + 1
    V_1V2_MGTVTT__end = rail.index("  ", V_1V2_MGTVTT__label)
    V_1V2_MGTVTT__string = rail[V_1V2_MGTVTT__start: V_1V2_MGTVTT__end]

    V_1V2_MGTVTT__list = V_1V2_MGTVTT__string.split(",")
    for i in range(len(V_1V2_MGTVTT__list)):
        V_1V2_MGTVTT__list[i] = float(V_1V2_MGTVTT__list[i])

    for i in range(len(V_1V2_MGTVTT__list)):
        if i == 0:
            V_1V2_MGTVTT__v_list.append(V_1V2_MGTVTT__list[i])
        if i == 1:
            V_1V2_MGTVTT__i_list.append(V_1V2_MGTVTT__list[i])
        if i == 2:
            V_1V2_MGTVTT__p_list.append(V_1V2_MGTVTT__list[i])
        if i == 3:
            V_1V2_MGTVTT__t1_list.append(V_1V2_MGTVTT__list[i])
        if i == 4:
            continue
        if i == 5:
            V_1V2_MGTVTT__t2_list.append(V_1V2_MGTVTT__list[i])
        if i == 6:
            V_1V2_MGTVTT__t3_list.append(V_1V2_MGTVTT__list[i])
        if i == 7:
            continue

V_1V2_MGTVTT = np.vstack((V_1V2_MGTVTT__v_list, V_1V2_MGTVTT__i_list, V_1V2_MGTVTT__p_list, V_1V2_MGTVTT__t1_list, 
                          V_1V2_MGTVTT__t2_list, V_1V2_MGTVTT__t3_list, zeros, zeros))

# V_1V5_AUX
V_1V5_AUX__v_list = []
V_1V5_AUX__i_list = []
V_1V5_AUX__p_list = []
V_1V5_AUX__t1_list = []

for rail in monitor:
    V_1V5_AUX__label = rail.index("1V5_AUX")
    V_1V5_AUX__start = rail.index(":", V_1V5_AUX__label) + 1
    V_1V5_AUX__end = rail.index("  ", V_1V5_AUX__label)
    V_1V5_AUX__string = rail[V_1V5_AUX__start: V_1V5_AUX__end]

    V_1V5_AUX__list = V_1V5_AUX__string.split(",")
    for i in range(len(V_1V5_AUX__list)):
        V_1V5_AUX__list[i] = float(V_1V5_AUX__list[i])

    for i in range(len(V_1V5_AUX__list)):
        if i == 0:
            V_1V5_AUX__v_list.append(V_1V5_AUX__list[i])
        if i == 1:
            V_1V5_AUX__i_list.append(V_1V5_AUX__list[i])
        if i == 2:
            V_1V5_AUX__p_list.append(V_1V5_AUX__list[i])
        if i == 3:
            continue
        if i == 4:
            continue
        if i == 5:
            V_1V5_AUX__t1_list.append(V_1V2_MGTVTT__list[i])
        if i == 6:
            continue
        if i == 7:
            continue

V_1V5_AUX = np.vstack((V_1V5_AUX__v_list, V_1V5_AUX__i_list, V_1V5_AUX__p_list, V_1V5_AUX__t1_list, 
                       zeros, zeros, zeros, zeros))

# V_1V5_IO
V_1V5_IO__v_list = []

for rail in monitor:
    V_1V5_IO__label = rail.index("1V5_IO")
    V_1V5_IO__start = rail.index(":", V_1V5_IO__label) + 1
    V_1V5_IO__end = rail.index("  ", V_1V5_IO__label)
    V_1V5_IO__string = rail[V_1V5_IO__start: V_1V5_IO__end]

    V_1V5_IO__list = V_1V5_IO__string.split(",")
    for i in range(len(V_1V5_IO__list)):
        V_1V5_IO__list[i] = float(V_1V5_IO__list[i])

    V_1V5_IO__v_list.append(V_1V5_IO__list[0])

V_1V5_IO = np.vstack((V_1V5_IO__v_list, zeros, zeros, zeros, 
                      zeros, zeros, zeros, zeros))

# V_1V5_MGTVCCAUX
V_1V5_MGTVCCAUX__v_list = []

for rail in monitor:
    V_1V5_MGTVCCAUX__label = rail.index("1V5_MGTVCCAUX")
    V_1V5_MGTVCCAUX__start = rail.index(":", V_1V5_MGTVCCAUX__label) + 1
    V_1V5_MGTVCCAUX__end = rail.index("  ", V_1V5_MGTVCCAUX__label)
    V_1V5_MGTVCCAUX__string = rail[V_1V5_MGTVCCAUX__start: V_1V5_MGTVCCAUX__end]

    V_1V5_MGTVCCAUX__list = V_1V5_MGTVCCAUX__string.split(",")
    for i in range(len(V_1V5_MGTVCCAUX__list)):
        V_1V5_MGTVCCAUX__list[i] = float(V_1V5_MGTVCCAUX__list[i])

    V_1V5_MGTVCCAUX__v_list.append(V_1V5_MGTVCCAUX__list[0])

V_1V5_MGTVCCAUX = np.vstack((V_1V5_MGTVCCAUX__v_list, zeros, zeros, zeros, 
                             zeros, zeros, zeros, zeros))

# V_1V8_PSDDR
V_1V8_PSDDR__v_list = []
V_1V8_PSDDR__i_list = []
V_1V8_PSDDR__p_list = []
V_1V8_PSDDR__t1_list = []

for rail in monitor:
    V_1V8_PSDDR__label = rail.index("1V8_PSDDR")
    V_1V8_PSDDR__start = rail.index(":", V_1V8_PSDDR__label) + 1
    V_1V8_PSDDR__end = rail.index("  ", V_1V8_PSDDR__label)
    V_1V8_PSDDR__string = rail[V_1V8_PSDDR__start: V_1V8_PSDDR__end]

    V_1V8_PSDDR__list = V_1V8_PSDDR__string.split(",")
    for i in range(len(V_1V8_PSDDR__list)):
        V_1V8_PSDDR__list[i] = float(V_1V8_PSDDR__list[i])

    for i in range(len(V_1V8_PSDDR__list)):
        if i == 0:
            V_1V8_PSDDR__v_list.append(V_1V8_PSDDR__list[i])
        if i == 1:
            V_1V8_PSDDR__i_list.append(V_1V8_PSDDR__list[i])
        if i == 2:
            V_1V8_PSDDR__p_list.append(V_1V8_PSDDR__list[i])
        if i == 3:
            continue
        if i == 4:
            continue
        if i == 5:
            V_1V8_PSDDR__t1_list.append(V_1V8_PSDDR__list[i])
        if i == 6:
            continue
        if i == 7:
            continue

V_1V8_PSDDR = np.vstack((V_1V8_PSDDR__v_list, V_1V8_PSDDR__i_list, V_1V8_PSDDR__p_list, V_1V8_PSDDR__t1_list, 
                         zeros, zeros, zeros, zeros))

# V_3V3_LMK1
V_3V3_LMK1__v_list = []

for rail in monitor:
    V_3V3_LMK1__label = rail.index("3V3_LMK1")
    V_3V3_LMK1__start = rail.index(":", V_3V3_LMK1__label) + 1
    V_3V3_LMK1__end = rail.index("  ", V_3V3_LMK1__label)
    V_3V3_LMK1__string = rail[V_3V3_LMK1__start: V_3V3_LMK1__end]

    V_3V3_LMK1__list = V_3V3_LMK1__string.split(",")
    for i in range(len(V_3V3_LMK1__list)):
        V_3V3_LMK1__list[i] = float(V_3V3_LMK1__list[i])

    V_3V3_LMK1__v_list.append(V_3V3_LMK1__list[0])

V_3V3_LMK1 = np.vstack((V_3V3_LMK1__v_list, zeros, zeros, zeros, 
                         zeros, zeros, zeros, zeros))

# V_3V3_LMK2
V_3V3_LMK2__v_list = []

for rail in monitor:
    V_3V3_LMK2__label = rail.index("3V3_LMK2")
    V_3V3_LMK2__start = rail.index(":", V_3V3_LMK2__label) + 1
    V_3V3_LMK2__end = rail.index("  ", V_3V3_LMK2__label)
    V_3V3_LMK2__string = rail[V_3V3_LMK2__start: V_3V3_LMK2__end]

    V_3V3_LMK2__list = V_3V3_LMK2__string.split(",")
    for i in range(len(V_3V3_LMK2__list)):
        V_3V3_LMK2__list[i] = float(V_3V3_LMK2__list[i])

    V_3V3_LMK2__v_list.append(V_3V3_LMK2__list[0])

V_3V3_LMK2 = np.vstack((V_3V3_LMK2__v_list, zeros, zeros, zeros, 
                         zeros, zeros, zeros, zeros))

# V_3V3_PERIPH
V_3V3_PERIPH__v_list = []

for rail in monitor:
    V_3V3_PERIPH__label = rail.index("3V3_PERIPH")
    V_3V3_PERIPH__start = rail.index(":", V_3V3_PERIPH__label) + 1
    V_3V3_PERIPH__end = rail.index("  ", V_3V3_PERIPH__label)
    V_3V3_PERIPH__string = rail[V_3V3_PERIPH__start: V_3V3_PERIPH__end]

    V_3V3_PERIPH__list = V_3V3_PERIPH__string.split(",")
    for i in range(len(V_3V3_PERIPH__list)):
        V_3V3_PERIPH__list[i] = float(V_3V3_PERIPH__list[i])

    V_3V3_PERIPH__v_list.append(V_3V3_PERIPH__list[0])

V_3V3_PERIPH = np.vstack((V_3V3_PERIPH__v_list, zeros, zeros, zeros, 
                         zeros, zeros, zeros, zeros))

# V_3V3_STANDBY
V_3V3_STANDBY__v_list = []

for rail in monitor:
    V_3V3_STANDBY__label = rail.index("3V3_STANDBY")
    V_3V3_STANDBY__start = rail.index(":", V_3V3_STANDBY__label) + 1
    V_3V3_STANDBY__end = rail.index("  ", V_3V3_STANDBY__label)
    V_3V3_STANDBY__string = rail[V_3V3_STANDBY__start: V_3V3_STANDBY__end]

    V_3V3_STANDBY__list = V_3V3_STANDBY__string.split(",")
    for i in range(len(V_3V3_STANDBY__list)):
        V_3V3_STANDBY__list[i] = float(V_3V3_STANDBY__list[i])

    V_3V3_STANDBY__v_list.append(V_3V3_STANDBY__list[0])

V_3V3_STANDBY = np.vstack((V_3V3_STANDBY__v_list, zeros, zeros, zeros, 
                         zeros, zeros, zeros, zeros))

# V_3V75_INTERMEDIATE
V_3V75_INTERMEDIATE__v_list = []
V_3V75_INTERMEDIATE__i_list = []
V_3V75_INTERMEDIATE__p_list = []

for rail in monitor:
    V_3V75_INTERMEDIATE__label = rail.index("3V75_INTERMEDIATE")
    V_3V75_INTERMEDIATE__start = rail.index(":", V_3V75_INTERMEDIATE__label) + 1
    V_3V75_INTERMEDIATE__end = rail.index("  ", V_3V75_INTERMEDIATE__label)
    V_3V75_INTERMEDIATE__string = rail[V_3V75_INTERMEDIATE__start: V_3V75_INTERMEDIATE__end]

    V_3V75_INTERMEDIATE__list = V_3V75_INTERMEDIATE__string.split(",")
    for i in range(len(V_3V75_INTERMEDIATE__list)):
        V_3V75_INTERMEDIATE__list[i] = float(V_3V75_INTERMEDIATE__list[i])

    for i in range(0, 3):
        if i == 0:
            V_3V75_INTERMEDIATE__v_list.append(V_3V75_INTERMEDIATE__list[i])
        if i == 1:
            V_3V75_INTERMEDIATE__i_list.append(V_3V75_INTERMEDIATE__list[i])
        if i == 2:
            V_3V75_INTERMEDIATE__p_list.append(V_3V75_INTERMEDIATE__list[i])

V_3V75_INTERMEDIATE = np.vstack((V_3V75_INTERMEDIATE__v_list, V_3V75_INTERMEDIATE__i_list, V_3V75_INTERMEDIATE__p_list, zeros, 
                         zeros, zeros, zeros, zeros))


all_rails = np.stack((V_0V8_CORE, V_0V92_MGTVCC, V_12V0, V_1V1_DDR, 
                      V_1V2_MGTVTT, V_1V5_AUX, V_1V5_IO, V_1V5_MGTVCCAUX, 
                      V_1V8_PSDDR, V_3V3_LMK1, V_3V3_LMK2, V_3V3_PERIPH, 
                      V_3V3_STANDBY, V_3V75_INTERMEDIATE), axis=0)

rail_labels = ["0V8_CORE", "0V92_MGTVCC", "12V0", "1V1_DDR", 
               "1V2_MGTVTT", "1V5_AUX", "1V5_IO", "1V5_MGTVCCAUX", 
               "1V8_PSDDR", "3V3_LMK1", "3V3_LMK2", "3V3_PERIPH", 
               "3V3_STANDBY", "3V75_INTERMEDIATE"]

'''Done with Rails!! Yay!!'''

'''Optics!!!'''
list__optics = []
for o in range(len(monitor)):
    optics__label = monitor[o].index("optics")
    optics__start = monitor[o].index(":", optics__label) + 1
    optics__string = monitor[o][optics__start:]
    optics__stripped = optics__string.strip("\n ,")
    optics__list = optics__stripped.split(",")

    for i in range(len(optics__list)):
        optics__list[i] = float(optics__list[i])
    
    nOptics = int(len(optics__list) / 7)
    optics__array = np.array(optics__list)
    optics__array_all = optics__array.reshape((nOptics, 7, 1))
    optics__list_all = optics__array_all.tolist()

    for optic in optics__list_all:
        optic.pop(0)

    for i in range(nOptics):
        for j in range(6):
            if o == 0:
                list__optics = optics__list_all
            else:
                list__optics[i][j].append(optics__list_all[i][j][0])

all_optics = np.array(list__optics)

optic_labels = ["Cage 0", "Cage 1", "Cage 2", "Cage 3", "Cage 4", "Cage 5", "Cage 6", "Cage 7", 
                "Cage 8", "Cage 9", "Cage 10", "Cage 11", "Cage 12", "Cage 13", "Cage 14", "Cage 15", 
                "Cage 16", "Cage 17", "Cage 18", "Cage 19", "Cage 20", "Cage 21", "Cage 22", "Cage 23", 
                "Cage 24", "Cage 25", "Cage 26", "Cage 27", "Cage 28", "Cage 29"]

'''Links!'''
list__links = []
for l in range(len(monitor)):
    links__label = monitor[l].index("links")
    links__start = monitor[l].index(",", links__label) + 1
    links__end = monitor[l].index("optics", links__label) - 1
    links__string = monitor[l][links__start: links__end]
    links__list = links__string.split(",")

    for i in range(len(links__list)):
        links__list[i] = int(links__list[i])

    binary_vector = np.vectorize(np.binary_repr)
    links__list_binary = binary_vector(links__list)

    for i in range(len(links__list)):
        if len(links__list_binary[i]) == 9:
            links__list_binary[i] = '0'
        else:
            links__list_binary[i] = links__list_binary[i][0:-9]

    for i in range(len(links__list_binary)):
        links__list[i] = int(links__list_binary[i], 2)

    nLinks = int(len(links__list))
    links__array = np.array(links__list)
    links__array_all = links__array.reshape((nLinks, 1))
    links__list_all = links__array_all.tolist()

    for i in range(nLinks):
        if l == 0:
            list__links = links__list_all
        else:
            list__links[i].append(links__list_all[i][0])

all_links = np.array(list__links)

'''Plotting!'''
with plt.ioff():
    fig, ax = plt.subplots()
ax.set_xticks(timestamps)
ax.set_xticklabels(timestamps_labels_6hr, size=5, rotation=35, ha='right', rotation_mode='anchor')
ax.set_xlabel("Timestamp")
disconnect_zoom = zoom_factory(ax)
pan_handler = panhandler(fig)

rVoltage = 0
rCurrent = 1
rPower = 2
rTemperature = 3

oVoltage = 0
oTemperature = 1
oPower = 2

parameter_labels = [["Voltage (V)", "Current (I)", "Power (W)", "Temperature (C)"], 
                    ["Voltage (V)", "Temperature (C)", "Power (W)"], 
                    ["Errors"]]

def plot(mode, parameter):
    if mode == "Rails" and parameter == "Voltage":
        parameter = 0
        for rail in range(len(all_rails)):
            if all_rails[rail][parameter][0] == 0.:
                continue
            else:
                ax.plot(timestamps, all_rails[rail][parameter], label=optic_labels[rail])
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[0][parameter])
        ax.set_title("Rail Voltage vs Time")
        plt.show()

    if mode == "Rails" and parameter == "Current":
        parameter = 1
        for rail in range(len(all_rails)):
            if all_rails[rail][parameter][0] == 0.:
                continue
            else:
                ax.plot(timestamps, all_rails[rail][parameter], label=rail_labels[rail])
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[0][parameter])
        ax.set_title("Rail Current vs Time")
        plt.show()

    if mode == "Rails" and parameter == "Power":
        parameter = 2
        for rail in range(len(all_rails)):
            if all_rails[rail][parameter][0] == 0.:
                continue
            else:
                ax.plot(timestamps, all_rails[rail][parameter], label=rail_labels[rail])
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[0][parameter])
        ax.set_title("Rail Power vs Time")
        plt.show()

    if mode == "Rails" and parameter == "Temperature":
        parameter = 3
        for rail in range(len(all_rails)):
            j=1
            for i in range(parameter, 7):
                if all_rails[rail][i][0] == 0.:
                    continue
                else:
                    ax.plot(timestamps, all_rails[rail][i], label=rail_labels[rail] + "_T{j}".format(j=j))
                    j+=1
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[0][parameter])
        ax.set_title("Rail DCDC Converter Temperatures vs Time")
        plt.show()

    if mode == "Optics" and parameter == "Voltage":
        parameter = 0
        for optic in range(len(all_optics)):
            ax.plot(timestamps, all_optics[optic][parameter], label=optic_labels[optic])
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ybound(3.2, 3.4)
        ax.set_ylabel(parameter_labels[1][parameter])
        ax.set_title("All Optics Voltage vs Time")
        plt.show()

    if mode == "Optics" and parameter == "Temperature":
        parameter = 1
        for optic in range(len(all_optics)):
            ax.plot(timestamps, all_optics[optic][parameter], label=optic_labels[optic])
        ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[1][parameter])
        ax.set_title("All Optics Temperature vs Time")
        plt.show()

    if mode == "Optics" and parameter == "Power":
        parameter = 2
        for optic in range(len(all_optics)):
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[optic][i], label=optic_labels[optic] + "_P{j}".format(j=j))
                j+=1
        ax.legend(loc='lower right', fontsize=5, ncols=15)
        ax.set_ybound(0.2, 1.2)
        ax.set_ylabel(parameter_labels[1][parameter])
        ax.set_title("All Optics RX Power vs Time")
        plt.show()



def plot_quads(quads, parameter):
    if quads == "Q202-205":
        c = 0
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q202-205 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q202-205 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q202-205 Optics RX Power vs Time")
            plt.show()

    if quads == "Q206-209":
        c = 2
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q206-209 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q206-209 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q206-209 Optics RX Power vs Time")
            plt.show()

    if quads == "Q210-213":
        c = 4
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q210-213 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q210-213 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q210-213 Optics RX Power vs Time")
            plt.show()

    if quads == "Q216-219":
        c = 6
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q216-219 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q216-219 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q216-219 Optics RX Power vs Time")
            plt.show()

    if quads == "Q220-223":
        c = 8
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q220-223 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q220-223 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q220-223 Optics RX Power vs Time")
            plt.show()

    if quads == "Q122-124, 224":
        c = 10
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q122-124, 224 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q122-124, 224 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q122-124, 224 Optics RX Power vs Time")
            plt.show()

    if quads == "Q112, 115-117":
        c = 12
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q112, 115-117 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+1][parameter], label=optic_labels[c+1])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.plot(timestamps, all_optics[c+16][parameter], label=optic_labels[c+16])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q112, 115-117 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+1][i], label=optic_labels[c+1] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+16][i], label=optic_labels[c+16] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q112, 115-117 Optics RX Power vs Time")
            plt.show()

    if quads == "Q109-110":
        c = 14
        if parameter == "Voltage":
            parameter = 0
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ybound(3.2, 3.4)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q109-110 Optics Voltage vs Time")
            plt.show()
        if parameter == "Temperature":
            parameter = 1
            ax.plot(timestamps, all_optics[c][parameter], label=optic_labels[c])
            ax.plot(timestamps, all_optics[c+15][parameter], label=optic_labels[c+15])
            ax.legend(loc='upper right', fontsize=6)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q109-110 Optics Temperature vs Time")
            plt.show()
        if parameter == "Power":
            parameter = 2
            j=1
            for i in range(parameter, 6):
                ax.plot(timestamps, all_optics[c][i], label=optic_labels[c] + "_P{j}".format(j=j))
                ax.plot(timestamps, all_optics[c+15][i], label=optic_labels[c+15] + "_P{j}".format(j=j))
                j+=1
            ax.legend(loc='lower right', fontsize=6, ncols=4)
            ax.set_ybound(0.2, 1.2)
            ax.set_ylabel(parameter_labels[1][parameter])
            ax.set_title("Q109-110 Optics RX Power vs Time")
            plt.show()



def plot_links(mode):
    if mode == "All Errors":
        for link in range(len(all_links)):
            ax.plot(timestamps, all_links[link]) #, label=optic_labels[rail]
        #ax.legend(loc='upper right', fontsize=6)
        ax.set_ylabel(parameter_labels[2][0])
        ax.set_title("Link Errors vs Time")
        plt.show()

    if mode == "Significant Errors":
        for link in range(len(all_links)):
            if all_links[link][0] == 0 or all_links[link][0] == 4294967295:
                continue
            else:
                ax.plot(timestamps, all_links[link]) #, label=optic_labels[rail]
        #ax.legend(loc='lower right', fontsize=6)
        ax.set_ylabel(parameter_labels[2][0])
        ax.set_title("Link Errors vs Time")
        plt.show()

    if mode == "Zero Errors":
        for link in range(len(all_links)):
            if all_links[link][0] != 0:
                continue
            else:
                ax.plot(timestamps, all_links[link]) #, label=optic_labels[rail]
        #ax.legend(loc='lower right', fontsize=6)
        ax.set_ylabel(parameter_labels[2][0])
        ax.set_title("Link Errors vs Time")
        plt.show()

    if mode == "Max Errors":
        for link in range(len(all_links)):
            if all_links[link][0] != 4294967295:
                continue
            else:
                ax.plot(timestamps, all_links[link]) #, label=optic_labels[rail]
        #ax.legend(loc='lower right', fontsize=6)
        ax.set_ylabel(parameter_labels[2][0])
        ax.set_title("Link Errors vs Time")
        plt.show()

plot("Rails", "Voltage")
#plot("Rails", "Current")
#plot("Rails", "Power")
#plot("Rails", "Temperature")

#plot("Optics", "Voltage")
#plot("Optics", "Temperature")
#plot("Optics", "Power")

#plot_quads("Q202-205", "Voltage")
#plot_quads("Q202-205", "Temperature")
#plot_quads("Q202-205", "Power")

#plot_quads("Q206-209", "Voltage")
#plot_quads("Q206-209", "Temperature")
#plot_quads("Q206-209", "Power")

#plot_quads("Q210-213", "Voltage")
#plot_quads("Q210-213", "Temperature")
#plot_quads("Q210-213", "Power")

#plot_quads("Q216-219", "Voltage")
#plot_quads("Q216-219", "Temperature")
#plot_quads("Q216-219", "Power")

#plot_quads("Q220-223", "Voltage")
#plot_quads("Q220-223", "Temperature")
#plot_quads("Q220-223", "Power")

#plot_quads("Q122-124, 224", "Voltage")
#plot_quads("Q122-124, 224", "Temperature")
#plot_quads("Q122-124, 224", "Power")

#plot_quads("Q112, 115-117", "Voltage")
#plot_quads("Q112, 115-117", "Temperature")
#plot_quads("Q112, 115-117", "Power")

#plot_quads("Q109-110", "Voltage")
#plot_quads("Q109-110", "Temperature")
#plot_quads("Q109-110", "Power")

plot_links("All Errors")
#plot_links("Significant Errors")
#plot_links("Zero Errors")
#plot_links("Max Errors")