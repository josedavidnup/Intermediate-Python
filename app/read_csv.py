import csv


def read_cvs(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    # print(header)
    data = []
    for row in reader:
      iterable = zip(header, row)
      # print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      # print(country_dict)
      data.append(country_dict)
    return data
    # print('***' * 5)
    # print(row)


if __name__ == '__main__':
  data = read_cvs('./app/data.csv')
  print(data[0])
