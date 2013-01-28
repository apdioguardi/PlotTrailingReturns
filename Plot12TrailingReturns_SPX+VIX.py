# Plot SPX and VIX (or two data sets in of comma delimited data in general)

import matplotlib.pyplot as plt
import numpy

filename1 = 'SPX_tr12mo_data.txt'
filename2 = 'VIX_tr12mo_data.txt'
curve1name = 'SPX'
curve2name = 'VIX'
plot_title_str = 'SPX and VIX 12 Month Trailing Returns'
save_file_str = 'SPX_and_VIX_Trailing_Returns'
x_label_str = 'Years'
y_label_str = 'Trailing Returns (%)'
#legend_location_str = 'upper left' # will output error with possible values if you guess wrong adam


# Read the file.
bulkfile1 = open(filename1, 'r')

# initialize some variable to be lists:
SPX_tr_date_12 = []
SPX_tr_perc_12 = []

# scan the rows of the file stored in bulk file
# and put the values into some variables.
# leave and blank lines out:
for line in bulkfile1:
    p = line.split(', ')
    SPX_tr_date_12.append(float(p[0]))
    SPX_tr_perc_12.append(float(p[1]))

bulkfile1.close()

bulkfile2 = open(filename2, 'r')

# initialize some variable to be lists:
VIX_tr_date_12 = []
VIX_tr_perc_12 = []

# scan the rows of the file stored in bulk file
# and put the values into some variables.
# leave and blank lines out:
for line in bulkfile2:
    p = line.split(', ')
    VIX_tr_date_12.append(float(p[0]))
    VIX_tr_perc_12.append(float(p[1]))

bulkfile2.close()

# create arrays for ploting w/ numpy
SPX_tr_perc_array_12 = numpy.array(SPX_tr_perc_12)
SPX_tr_date_array_12 = numpy.array(SPX_tr_date_12)
VIX_tr_perc_array_12 = numpy.array(VIX_tr_perc_12)
VIX_tr_date_array_12 = numpy.array(VIX_tr_date_12)

# now, plot the data:
#plt.plot(SPX_tr_date_array_12, SPX_tr_perc_array_12, label=curve1name, color='black', linewidth=0.5)

#plt.plot(VIX_tr_date_array_12, VIX_tr_perc_array_12, label=curve2name, color='red', linewidth=0.5)

#plt.ylabel(y_label_str)
#plt.xlabel(x_label_str)
#plt.legend(loc=legend_location_str)
#plt.xlim([min(VIX_tr_date_12), max(VIX_tr_date_12)])
#plt.title(plot_title_str)
#plt.fill_between(tr_date_array_12, 0, tr_perc_array_12, facecolor='blue', alpha=0.4)
#plt.fill_between(tr_date_array_3, 0, tr_perc_array_3, facecolor='red', alpha=0.75)

fig = plt.figure()
left_ax = fig.add_subplot(111)
left_ax.plot(SPX_tr_date_array_12, SPX_tr_perc_array_12, label=curve1name, color='black', linewidth=0.5)
left_ax.set_xlabel(x_label_str)
left_ax.set_ylabel(y_label_str, color='black')
for tl in left_ax.get_yticklabels():
    tl.set_color('black')
right_ax = left_ax.twinx()
right_ax.plot(VIX_tr_date_array_12, VIX_tr_perc_array_12, label=curve2name, color='red', linewidth=0.5)
right_ax.set_ylabel(y_label_str, color='red')
for tl in right_ax.get_yticklabels():
    tl.set_color('red')
left_ax.set_ylim([-100,350])
right_ax.set_ylim([-100,350])
left_ax.legend(loc='upper left')
right_ax.legend(loc='upper right')
plt.xlim([min(VIX_tr_date_12), max(VIX_tr_date_12)])
plt.title(plot_title_str)


plt.savefig(save_file_str + '.pdf')
print "Plot saved as " + "'" + save_file_str + "'"

#plt.show()
# doesn't work w/ my backend in linux...:
