import csv
from collections import namedtuple

def read_csv(csv_file):
  """
    A generator for the data in the csv. This is because the csv files can often contain millions of records and shouldn't be stored in memory all at once.

    :param csv_file:
        filename/location of the csv.

    :return:
        yields each row as a namedtuple.
  """

  user_record = namedtuple('UserRecord', 'userA, userB, affinity_score')

  with open(csv_file, 'r') as user_scores:
    reader = csv.DictReader(user_scores)
    for row in reader:
      yield user_record(**row)


if __name__ == '__main__':
  filename = './testData.csv'

  user_score_collection = {}

  for score_row in read_csv(filename):
    if score_row.userA not in user_score_collection:
      user_score_collection[score_row.userA] = score_row
    elif score_row.affinity_score > user_score_collection[score_row.userA].affinity_score :
      user_score_collection[score_row.userA] = score_row

for filtered_row in user_score_collection.values():
  print(filtered_row.userA, filtered_row.userB, filtered_row.affinity_score)
