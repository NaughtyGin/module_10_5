from datetime import datetime
from multiprocessing import Pool


all_data = []


def read_info(name):
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().rstrip('\n')
            if not line:
                break
            all_data.append(line.strip())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

start = datetime.now()

for name in filenames:
    read_info(name)

stop = datetime.now()
print(stop - start, '(линейный)')

# Многопроцессный
# if __name__ == '__main__':
#
#     start = datetime.now()
#
#     with Pool(processes=4) as pool:
#         all_data = pool.map(read_info, filenames)
#
#     stop = datetime.now()
#     print(stop - start, '(многопроцессный)')
