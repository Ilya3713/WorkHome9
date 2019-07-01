
import datetime
import timeit
import pprint

class MyOpen:
  def __init__(self, path, mode = 'rt'):
    self.files = open(path, mode)
    self.timeStart = datetime.datetime.today()
    self.start = timeit.default_timer()
    print(f'Время начала работы {datetime.datetime.strftime(self.timeStart, "%d/%m/%Y %H:%M:%S")}')

  def __enter__(self):
    return self.files

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.files.close()
    self.timeFinish = datetime.datetime.today()
    self.stop = timeit.default_timer()
    print(f'Время конца работы {datetime.datetime.strftime(self.timeFinish, "%d/%m/%Y %H:%M:%S")}')
    print('Время выполнения кода: ', self.stop - self.start)



dicts = dict()
with MyOpen('Cook.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            name = f.readline().strip()
            dicts.setdefault(name, list())
        else:
            counts = line.strip()
            count = 0
            while count < int(counts):
                stri = f.readline().strip().split('|')
                info_cook = {"ingridient_name": stri[0], "quantity": stri[1], "measure": stri[2]}
                dicts[name].append(info_cook)
                count += 1
print(dicts)



cook_dict = dict()
def get_shop_list_by_dishes(dishes, person_count):
  for cook_name in dishes:
    if cook_name in dicts.keys():
        for items_list in dicts.keys():
            if cook_name == items_list:
                for item in dicts[items_list]:
                    for key, value in item.items():
                            if key == 'quantity':
                                values = int(value)
                                item[key] = values * 5         
                    for key, value in item.items():
                      if key == 'ingridient_name':
                        name = value
                        cook_dict.setdefault(value, dict())
                      elif key == 'measure':
                        cook_dict[name].setdefault(key,value.strip())
                      elif key == 'quantity':
                        cook_dict[name].setdefault(key,value)
    else:
      return('Нет блюда: ' + cook_name)
  return cook_dict
  


dis = list()
count_cook = int(input('\n\n Введите количество вводимых блюд: \n'))
person = int(input('Введите количество персон: '))
for i in range (count_cook):
    x=input("Введите наименования блюда: \n")
    dis.insert(i,x)
    i+=1
pprint.pprint(get_shop_list_by_dishes(dis, person))


