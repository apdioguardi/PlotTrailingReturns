# PlotTrailingReturns

import matplotlib.pyplot
import numpy


filename = 'SPX_File.txt'
plot_title_str = 'SPX Trailing 12 Month Returns'
save_file_str = 'SPX_Trailing_12_Month_Returns.pdf'
start_date = '1960/01/04'
Delta = 252
# 12 month returns
# 3 month returns

# Read the file.
bulkfile = open(filename, 'r')
# read the whole file into a single variable, which is a list of every row of the file.
#lines = bulkfile.readlines()

# initialize some variable to be lists:
decimal_date = []
opening_price = []
daily_high_price = []
daily_low_price = []
daily_close_price = []
share_volume = []
analog_date = []


# scan the rows of the file stored in lines,
# and put the values into some variables.
# leave and blank lines out:
#for line in lines:
for line in bulkfile:
    p = line.split()
    decimal_date.append(float(p[0]))
    opening_price.append(float(p[1]))
    daily_high_price.append(float(p[2]))
    daily_low_price.append(float(p[3]))
    daily_close_price.append(float(p[4]))
    share_volume.append(float(p[5]))
    analog_date.append(str(p[6]))

bulkfile.close()

tr_perc = []
tr_date = []
tr_analog_date = []
tr_start = analog_date.index(start_date)

for i in range(tr_start + Delta, len(decimal_date)):
    tr_perc.append(100*((daily_close_price[i] - daily_close_price[i - Delta])/daily_close_price[i - Delta]))
    #if Delta == 21:
    tr_date.append(decimal_date[i])
    tr_analog_date.append(analog_date[i])
    #else:
    #    tr_date.append((decimal_date[i] - decimal_date[tr_start]))

largest_drawdown = min(tr_perc)
largest_drawdown_date = tr_analog_date[tr_perc.index(largest_drawdown)]
print largest_drawdown
print largest_drawdown_date

# create arrays for ploting w/ numpy
#decimal_date_array = numpy.array(decimal_date)
#daily_close_price_array = numpy.array(daily_close_price)
tr_perc_array = numpy.array(tr_perc)
tr_date_array = numpy.array(tr_date)

# now, plot the data:
#matplotlib.pyplot.plot(decimal_date_array, daily_close_price_array)
matplotlib.pyplot.plot(tr_date_array, tr_perc_array)

matplotlib.pyplot.ylabel('Trailing Returns (%)')
#if Delta == 21:
#    x_label_str = 'Months after ' + start_date
#else:
#    x_label_str = 'Years after ' + start_date
x_label_str = 'Year'
matplotlib.pyplot.xlabel(x_label_str)
xaxis_max = decimal_date[int(len(decimal_date) - 1)]
xaxis_min = decimal_date[tr_start + Delta]
matplotlib.pyplot.xlim([xaxis_min, xaxis_max])
matplotlib.pyplot.title(plot_title_str)
matplotlib.pyplot.fill_between(tr_date_array, 0, tr_perc_array, facecolor='blue', alpha=0.5)

# xticks
#locs,labels = matplotlib.pyplot.xticks()
#matplotlib.pyplot.xticks(locs, map(lambda x: "%g" % x, locs))

# ytikcs
#locs,labels = matplotlib.pyplot.yticks()
#matplotlib.pyplot.yticks(locs, map(lambda x: "%.1f" % x, locs))

matplotlib.pyplot.savefig(save_file_str)

#matplotlib.pyplot.show()
# doesn't work w/ my backend in linux...

