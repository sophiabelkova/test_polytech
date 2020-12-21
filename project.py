#класс, определение и вызов функций генерации тегов и последующего объединения в готовый файл.
#name-название тега,  border-cкобки, позволяющие добавлять другие теги внутрь главного, content-то что будет написано, href-ссылки, классы и т д
#функция generate пока тэг в границах тега выводим res повторяем функцию
#функция генерации файла открывает файл file только для записи в него функции генерации тегов и закрывает файл.
class Tag:
    def __init__(self):
        self.name = "name"
        self.content = ""
        self.href = ""
        self.type = ""
        self.border = []
        self.rel = ""
       
        
    def Generate(self):
        res = "<"+self.name+" "+self.href+">"+self.content+" \n"
        for tag in self.border:
            res = res+tag.Generate()
        res = res+"</"+self.name+"> \n"
        return res
    def GenerateFile(self, file):
        file = open(file, "w")
        file.write(self.Generate())
        file.close()
    pass
#экземпляры класса использующие только атрибут дата
#1 <html>
class Html(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "html"
        self.border = data
    pass
#2 <head>
class Head(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "head"
        self.border = data
    pass
#3 <body>
class Body(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "body"
        self.border = data
    pass
#4 <center>
class Center(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "center"
        self.border = data
    pass
#5 <strong>
class Strong(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "strong"
        self.border = data
    pass
#6 <em>
class Em(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "em"
        self.border = data
    pass
#7 <ol>
class Ol(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "ol"
        self.border = data
    pass
#8 <ul>
class Ul(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "ul"
        self.border = data
    pass
#9 <li>
class Li(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "li"
        self.border = data
    pass
#10 <div>
class Div(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "div"
        self.border = data
    pass
#11 <header>
class Header(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "header"
        self.border = data
    pass
#12 <footer>
class Footer(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "footer"
        self.border = data
    pass
#экземпляры класса использующие только атрибут текст
#13,14,15 <h1,2,3>
class H1(Tag):
    def __init__(self,text, href, typ):
        Tag.__init__(self)
        self.name = "h1"
        self.content = text
        self.href = href
        self.type = typ
    pass
class H2(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.name = "h2"
        self.content = text
    pass
class H3(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.name = "h3"
        self.content = text
    pass
#16 <p>
class P(Tag):
    def __init__(self,text, href):
        Tag.__init__(self)
        self.name = "p"
        self.content = text
    pass
#17 <title>
class Title(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.name = "title"
        self.content = text
    pass
#экземпляры класса использующие только атрибут имя
#18 <br/>
class Br(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.name = "br"
#19 <hr/>
class Hr(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.name = "hr"

#экземпляры класса использующие много чего
#9 <link>

#20 <a>
class A(Tag):
    def __init__(self,text, href):
        Tag.__init__(self)
        self.name = "a"
        self.content = text
        self.href = href
    pass

#21 <style>
class Style(Tag):
    def __init__(self, text, href):
        Tag.__init__(self)
        self.name = "style"
        self.content = text
        self.href = href
    pass
#22 <img>
class Img(Tag):
    def __init__(self, href):
        Tag.__init__(self)
        self.name = "img"
        self.href = href
    pass

#создание самой страницы.
ht = Html([
           Head([
                   Title("Python"),
                  Style("center { text-align:left; }", "type='text/css'")
                   ]),
             Body([
                   Div([
                        Header([
                            H1("Python", "style='font-size:45px'", "align='center'")                          
                        ]),
                        Img("src='https://top10a.ru/wp-content/uploads/2019/06/3-2.png'"),
                        Center([
                                H2("Разделы"),
                                Hr(),
                                Div([
                                    Ol([
                                        Li([
                                            Strong([
                                                A("Базовый синтаксис Python","href='http://pythonicway.com/python-basic-syntax'")
                                                ])
                                            ]),
                                        Li([
                                            Strong([
                                                A("Условные операторы в Python","href='https://devpractice.ru/python-lesson-5-if-while-for-operators/'")
                                                ])
                                            ]),
                                        Li([
                                            Strong([
                                                A("Функции в Python","href='https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html'")
                                                ])
                                            ]),
                                        Li([
                                            Strong([
                                                A("Объектно-ориентированное программирование в Python","href='https://python-scripts.com/object-oriented-programming-in-python'")
                                                ])
                                            ]),
                                        Ul([
                                            Em([
                                                 Li([
                                                A("Классы и объекты","href='https://devpractice.ru/python-lesson-14-classes-and-objects/'")  
                                            ]),
                                                 Li([
                                                A("Методы","href='https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html'")  
                                            ]),
                                                 Li([
                                                A("Наследование,полиморфизм и инкапсуляция","href='http://pythonicway.com/education/python-oop-themes/21-python-inheritance'")  
                                            ])
                                                ])
                                            ])

                                    
                                     ])
                                   ])
                                ])
                        ]),
                   Footer([
                           H3("Просмотреть код данной страницы можно по следующей ссылке:"),
                           A("Репозиторий github","href='https://github.com/sophiabelkova/test_polytech.git'"),
                           Br(),
                           H3("Работу подготовила:"),
                           A("Белькова София Вадимовна, студентка 1 курса группы 3431101/00001","href='https://vk.com/sofia_belkova'"),
                           ])
                    ])
              ])
#генерация кода и вызов функции записывающей его в файл
print(ht.Generate())
ht.GenerateFile("file.html")
                                     
                        
            
             
