
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
# print("Current Time =", current_time)
#
# dates = ['2020-01-01', '2020-01-02', '2020-01-03']
# urls = ['www.abc.com', 'www.cnn.com', 'www.nbc.com']
#
# csv_file_patch = 'sensor_report_' + current_time + '.csv'
#
# with open(csv_file_patch, 'w') as fout:
#     csv_file = csv.writer(fout, delimiter=';', lineterminator='\n')
#     result_array = zip(dates, urls)
#     csv_file.writerows(result_array)
