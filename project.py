#класс, определение и вызов функций генерации тегов и последующего объединения в готовый файл.
#name-название тега,  border-cкобки, позволяющие добавлять другие теги внутрь главного, content-то что будет написано, href-ссылки, классы и т д
#функция generate пока тэг в границах тега выводим res повторяем функцию
#функция генерации файла открывает файл page только для записи в него функции генерации тегов и закрывает файл.
class Tag:
    def __init__(self):
        self.name = "name"
        self.content = ""
        self.href = ""
        self.border = []
       
        
    def Generate(self):
        res = "<"+self.name+" "+self.href+">"+self.content+" \n"
        for tag in self.border:
            res = res+tag.Generate()
        res = res+"</"+self.name+"> \n"
        return res
#экземпляры класса
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
#3 <title>
class Title(Tag):
    def __init__(self,text):
        Tag.__init__(self)
        self.name = "title"
        self.content = text
    pass
#4 <body>
class Body(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "body"
        self.border = data
    pass
#5 <div>
class Div(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "div"
        self.border = data
    pass
#6 <header>
class Header(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "header"
        self.border = data
    pass
#7 <footer>
class Footer(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "footer"
        self.border = data
    pass
#8 <span>
#
#9 <link>
# class Link(Tag):
#     def __init__(self, href):
#         Tag.__init__(self)
#         self.name = "link"
#         self.href = href
#     pass
#10 <a>
class A(Tag):
    def __init__(self,text, href):
        Tag.__init__(self)
        self.name = "a"
        self.content = text
        self.href = href
    pass
#11 <style>
class Style(Tag):
    def __init__(self, text, href):
        Tag.__init__(self)
        self.name = "style"
        self.content = text
        self.href = href
    pass
#12 <br/>
class Br(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.name = "br"
#13 <hr/>
class Hr(Tag):
    def __init__(self):
        Tag.__init__(self)
        self.name = "hr"
#13 <center>
class Center(Tag):
    def __init__(self, data):
        Tag.__init__(self)
        self.name = "center"
        self.border = data
    pass
#создание самой страницы.
ht = Html([
           Head([
                   Title(" "),
                  Style(" ", " ")
                   ]),
             Body([
                   Div([
                        Header([
                        A(" ", " "),
                       
                              A(" ", " "),
                              
                       
                              A(" ", " "),
                         
                        
                              A(" ", " ")
                          
                        ]),
                        Div([Br()]),
                        Center([
                                Div([Hr()]),
                                Div([
                                     A(" ", " "),
                                     A(" ", " "),
                                     A(" ", " "),
                                    A(" ", " ")
                                     ])
                                ])
                        ]),
                   Footer([
                           A(" ", " ")
                           ])
                    ])
              ])
print(ht.Generate())          
                                     
                        
            
             
