import cx_Oracle
import csv


username = 'MYONLINEEDU'
password = 'oracle'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

# ------------------------------------------------------------------------------
def unique_values(some_list):
    new_list = []
    new_list.append(some_list[0])
    for element in some_list:
        if element not in new_list:
            new_list.append(element)
    return new_list
# ---------------------------------------------------------------------------------

file = open('911.csv')
file.readline()  # зчитує перший рядок
reader = csv.reader(file)
all_lines = []
towns = []
for line in reader:
    if line[6] != '':  # більше нулових значень у файлі немає
        all_lines += [[line[6]] + [line[7]] + [line[5]] + [line[4]]]
        towns += [line[6]]
file.close()


print(len(all_lines))
print()


tables = ['accident', 'place', 'town']  # у зворотньому порядку відносно заповнення таблиць
for table in tables:
    cursor.execute('''delete from ''' + table)


i = 1
UniqueTown = unique_values(towns)[:15]  # лише 15 міст зі штату
UniqueTown_1 = []
UniqueTwpAddr = []
UniqueIdTime = []
help_dict = {}
for row in all_lines:
    town = row[0]
    address = row[1]
    timestamp = row[2]
    tit = row[3].split(': ')[1]
    title = tit.split(' -')[0]
    if town in UniqueTown:
        if town not in UniqueTown_1:
            UniqueTown_1 += [town]
            query = '''insert into town(town) values(:town)'''
            cursor.execute(query, town=town)

        if [town, address] not in UniqueTwpAddr:
            UniqueTwpAddr += [[town, address]]
            help_dict[town, address] = i
            query = '''insert into place(place_id, address, town_town) values(:id, :addr, :town)'''
            cursor.execute(query, id=i, addr=address, town=town)

        if [help_dict[town, address], timestamp] not in UniqueIdTime:
            UniqueIdTime += [[help_dict[town, address], timestamp]]
            query = '''insert into accident(timestamp, title, place_place_id) 
            values(TO_TIMESTAMP(:timestamp,'yyyy-mm-dd HH24:MI:SS'), :title, :id)'''
            cursor.execute(query, timestamp=timestamp, title=title, id=help_dict[town, address])
            print('inserted3')
        i += 1

connection.commit()
cursor.close()
connection.close()
