import json
import os




class LibraryManagementSystem:

    def __init__(self):
        self.db_json = 'db_library.json'
        self.there_data = True
    
    def write_book(self,*args):
        try:
            with open(self.db_json, 'w', encoding='utf-8') as file:
                json.dump(self.data_book, file, indent=2, ensure_ascii=False)
        except Exception as Er:
            return Er
        
    def first_write_book(self,*args):
        try:
            id =1
            dict_book =[{'id': id,
                        'title':self.title_book,
                        'author': self.author,
                        'year':self.year,
                        'status':'в наличии'
                        }
                    ]
            with open(self.db_json, 'w', encoding='utf-8') as file:
                json.dump(dict_book, file, indent=2,  ensure_ascii=False)
            self.there_data = True
            return
        except Exception as Er:
            return Er

    def add_book(self):
        while True:
            self.title_book = (input('Titel : ')).title()
            self.author = (input('Author : ')).title()
            self.year = input('Year  : ')
            if 0<=len(self.title_book) and 0<=len(self.author) and 4==len(self.year):
                print('Добавление книги')
                if int(self.year) >2024 or int(self.year) < 1450:
                    print(int(self.year), 'Ошибка')
                    continue       
                if 0==len(json.load(open(self.db_json))):
                    self.first_write_book(self)
                    print(f'Первая книга {self.title_book} добавленна')
                    if input('Добавить еще, y/n?: ') == 'y':
                        continue
                    else:
                        break
                try:
                    self.data_book = json.load(open(self.db_json))
                    id =self.data_book[-1]['id']+1
                    dict_book ={'id': id,
                                'title':self.title_book,
                                'author': self.author,
                                'year':self.year,
                                'status':'в наличии'
                                }
                    self.data_book.append(dict_book)
                    self.write_book(self)
                    print(f'Книга {self.title_book} добавленна')
                    self.title_book,self.author,self.year = [],[],[]
                except FileNotFoundError :
                    self.first_write_book(self)
                    print(f'Первая книга {self.title_book} добавленна')
                    continue
                except Exception as Er:
                    print("Ошибка: ", Er)
                    continue
            elif 0>=len(self.title_book) and 0>=len(self.author) and 4!=len(self.year):    
                print('Заполнены не все поля!')
            elif 0>=len(self.title_book) and 0>=len(self.author) and 4==len(self.year):    
                print('Заполнены не все поля!')

            if input('Добавить еще, y/n?: ') == 'y':
                continue
            else:
                break

    def delete_book(self):
        if not self.there_data or 0==len(json.load(open(self.db_json))):
            print()
            print('Данных в базе нет , создайте ее с помощью: add')
            print()
            return
        while True: 
            if 0==len(json.load(open(self.db_json))):
                print()
                print('Данных в базе нет , создайте ее с помощью: add')
                print()
                break  
            try:
                id =int(input( 'Удалить ID: '))
                self.data_book = []
                count=[]
                for i in json.load(open(self.db_json)):
                    count.append(i['id'])
                    if i['id'] ==id:
                        continue
                    self.data_book.append(i)
                if not id in count:
                    print(f"ID: {id} в базе нету")
                    continue
                else:
                    self.write_book(self.data_book)
                    print(f"Книга с id {id} удаленна  ")
                if input('Удалить еще, y/n? : ') == 'y':
                    continue
                else:
                    break
            except:
                print('ввели не допустимые символы')
                print("допустимые символы : 1,2,3,4,5,6,7,8,9,0")
                if input('Хотите продолжить y/n? : ') == 'y':
                    continue
                else:
                    break

    def search_book(self):
        if not self.there_data or 0==len(json.load(open(self.db_json))):
            print()
            print('Данных в базе нет , создайте ее с помощью: add')
            print()
            return
        search_dict = {
            't': 'title',
            'a': 'author',
            'y': 'year'
        }
        while True:
            self.search_respone = []
            search = (input('Поиск по: Title - t;\nAuthor - a;\nYear - y\n>>> ')).lower()
            search_more = (input('>>> ')).title()
            
            for i in json.load(open(self.db_json)):
                if i[search_dict[search]] in search_more:
                    self.search_respone.append(i)
            if len(self.search_respone) == 0:
                print("По вашему запросу ничего не найдено",search_more)
                if input('Хотите продолжить поиск y/n? ') == 'y':
                    continue
                else:
                    break
            for n in self.search_respone:
                print(n)
            if input('Хотите продолжить поиск y/n? ') == 'y':
                continue
            else:
                break

    def show_all_book(self):
        if not self.there_data or 0==len(json.load(open(self.db_json))):
            print()
            print('Данных в базе нет , создайте ее с помощью: add')
            print()
            return
        count = True
        for i in json.load(open(self.db_json)):
            if count:
                print('id--title--author--year--status')
                print()
                count = False
            print(f'{i['id']}--{i['title']}--{i['author']}--{i['year']}--{i['status']}')
            print()

    def status_book(self):
        if not self.there_data or 0==len(json.load(open(self.db_json))):
            print()
            print('Данных в базе нет , создайте ее с помощью: add')
            print()
            return
        while True:    
            try:
                self.data_book = []
                count=[]
                status_book_dict={
                    'y' : 'в наличии',
                    'n' : 'выдана'
                }
                id =int(input( ' ID: '))
                status_book = input("Измининть статуст на y = в наличии; n = выдана: ").lower()
                if status_book == 'y' or status_book =='n':
                    for i in json.load(open(self.db_json)):
                        count.append(i['id'])
                        if i['id'] ==id:
                            i['status']=status_book_dict[status_book]
                        self.data_book.append(i)
                    if not id in count:
                        print(f"ID: {id} в базе нету")
                        continue
                    else:
                        self.write_book(self.data_book)
                        print(f"Статус id {id} изменен на: {status_book_dict[status_book]}")
                        
                    if input('Измининть статуст еще, y/n? : ') == 'y':
                        continue
                    else:
                        break
                else:
                    print('ввели не допустимые символы')
                    print("допустимые символы:y = в наличии; n = выдана ")
                    continue
            except Exception as Er:
                print('ввели не допустимые символы', Er)
                print("допустимые символы : 1,2,3,4,5,6,7,8,9,0")
                if input('Хотите продолжить y/n? : ') == 'y':
                    continue
                else:
                    break  
    
    def examination_db(self):
        if not self.db_json in os.listdir('.'):
            with open(self.db_json, 'a') as file:
                json.dump([],file, indent=2, ensure_ascii=False )
            self.there_data = False
        return

    def run(self):
        self.examination_db()
        respone_dict = {
           'add': self.add_book,
           'delete': self.delete_book,
           'search': self.search_book,
           'show': self.show_all_book,
           'status': self.status_book
        }
        while True:
            print('Добавить книги = add:')
            print('Удалить книгу по ID = delete:')
            print('Поиск книги = search:')
            print('Отображение всех книг = show:')
            print('Изменение статуса по ID = status')
            print('Очистить консоль = clear')
            print('Выход = exit')
            try:
                respone=input('>>> ')
                respone_dict[respone]()
            except KeyError:
                if respone == "exit":
                    break
                elif respone == 'clear':
                    os.system('cls||clear')
                else:
                    print(f'такой функции нет: {respone}')
                    continue
            except Exception:
                print(f'такой функции нет: {respone}')
                continue




if __name__ == '__main__':
    Lib = LibraryManagementSystem()
    Lib.run()