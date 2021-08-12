from os import stat
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go


df=pd.read_csv("NDProperties.csv")
writing_list=df["writing score"].to_list()
#fig=ff.create_distplot([df["writing(Inches)"].tolist()],["writing"],show_hist=True)
#fig.show()
h_mean=statistics.mean(writing_list)
h_mode=statistics.mode(writing_list)
h_median=statistics.median(writing_list)
h_sd=statistics.stdev(writing_list)

fig = ff.create_distplot([writing_list], ["writing score"], show_hist=False)
fig.show()


writing_first_std_deviation_start, writing_first_std_deviation_end = h_mean-h_sd, h_mean+h_sd
writing_second_std_deviation_start, writing_second_std_deviation_end = h_mean-(2*h_sd), h_mean+(2*h_sd)
writing_third_std_deviation_start, writing_third_std_deviation_end = h_mean-(3*h_sd), h_mean+(3*h_sd)

writing_list_of_data_within_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("Mean, Median,Mode And Standard Deviation of writing is {}, {}, {} And {} respectively".format(h_mean,h_median,h_mode,h_sd))
print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 2 standard deviation".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for writing lies within 3 standard deviation".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writing_list)))