file = open('путь до файла')
# закрытие потока обязательно при такой записи
file.close()

with open(r'путь до файла') as file:
    #считывает одну строку из файла . взвращает str
    data = file.readline()
    #считывает все строки из файла. вовращаает list
    data = file.readlines()