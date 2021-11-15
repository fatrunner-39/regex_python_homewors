from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

pattern = r"(8|\+7)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\-*)(\d{2})(\-*)(\d{2})(,*)(\s*)(\(*)(доб)*(\.*)(\s*)(\d{4})*(\)*)(,*)"
repl = r"+7(\4)\8-\10-\12 \16\17\19"
name_pattern = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
name_repl = r"\1\3\10\4\6\9\7\8"

contact_updated = list()
contact_list_updated = list()

for contact in contacts_list:
    contact_updated = list()
    for el in contact:
        formatted_number = re.sub(pattern, repl, str(el))
        contact_updated.append(formatted_number)
    contact_list_updated.append(contact_updated)

contact_list_updated_name = list()
for contact in contact_list_updated:
    contact_string = ','.join(contact)
    formatted_contact = re.sub(name_pattern, name_repl, contact_string)
    contact_as_list = formatted_contact.split(',')
    contact_list_updated_name.append(contact_as_list)

for i in contact_list_updated_name:
    for j in contact_list_updated_name:
        if i[0] == j[0] and i[1] == j[1] and i != j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

contaсts_dict = dict()
for contact in contact_list_updated_name:
    if tuple(contact[:2]) not in contaсts_dict:
        contaсts_dict[tuple(contact[:2])] = contact[2:]

finish_conract_list = list()
for key, item in contaсts_dict.items():
    cont = list(key)
    cont += item
    finish_conract_list.append(cont)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(finish_conract_list)
print("Форматирование завершено.")