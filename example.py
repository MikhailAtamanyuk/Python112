from jinja2 import Template, Environment, FileSystemLoader


# per = {'name': "Игорь", 'age': 28}

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)

# data = "{% raw %}Строка, с названием {{ name }}. Со значением {% endraw %}"
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
#
# print(msg)

# link = "<a href='#'>Ссылка</a>"
#
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]

# link = """<select name="cities">
#     {% for c in cities -%}
#     {% if c.id > 3 -%}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.ctiy == "Москва" -%}
#         <option>{{ c['city'] }}</option>
#     {% else -%}
#         {{ c['city'] }}
#     {% endif %}
#     {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# data = [
#     {'href': 'index', 'title':'Главная'},
#     {'href': 'news', 'title':'Новости'},
#     {'href': 'about', 'title':'О компании'},
#     {'href': 'shop', 'title':'Магазин'},
#     {'href': 'contacts', 'title':'Контакты'},
# ]
#
# d = "class = 'active'"
# link = """
# <ul>
# {% for di in data -%}
#     {% if di.href=="index" -%}
#         <li><a href="/{{di.href}} {{d}}>{{di.title}}</a></li>
#     {% else -%}
#         <li><a href="/{{di.href}}>{{di.title}}</a></li>
#     {% endif -%}
# {% endfor -%}
# </ul>
# """
# tm = Template(link)
# msg = tm.render(data=data, d=d)
# print(msg)
#
# lst = [1, 2, 3, 4, 5, 6]
#
# tpl = "Сумму: {{ cs | sum }}"
# tm = Template(tpl)
# msg = tm.render(cs=lst)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300},
# ]
#
# # tpl = "Сумму: {{ (cs | min(attribute='price')).model }}"
# # tpl = "Автомобиль: {{ cs | random }}"
# tpl = "Автомобиль: {{ cs | replace('model', 'brand') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# person = [
#     {'name': "Алексей", 'year': 18, 'weight': 78.5},
#     {'name': "Никита", 'year': 28, 'weight': 82.3},
#     {'name': "Виталий", 'year': 33, 'weight': 94.0}
# ]
#
# tpl = """
# {%- for u in users -%}
# {% filter string %} {{ u.name }} - {{ u.weight }} {% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=person)
#
# print(msg)

# html = '''
# {% macro input (name, value='', type='text', size='20') -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
# {%- endmacro %}
#
# <p>{{ input('username') }}</p>
# <p>{{ input('email', type='email') }}</p>
# <p>{{ input('password') }}</p>
# '''

# html = '''
#     {% macro input(name, placeholder, type='text') -%}
#         <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
#     {%- endmacro %}
#
#     <p>{{ input(name='firstname', placeholder='Имя') }}</p>
#     <p>{{ input(name='lastname', placeholder='Фамилия') }}</p>
#     <p>{{ input(name='address', placeholder='Адрес') }}</p>
#     <p>{{ input(type='tel', name='phone', placeholder='Телефон') }}</p>
#     <p>{{ input(type='email', name='email', placeholder='Почта') }}</p>
# '''
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# person = [
#     {'name': "Алексей", 'year': 18, 'weight': 78.5},
#     {'name': "Никита", 'year': 28, 'weight': 82.3},
#     {'name': "Виталий", 'year': 33, 'weight': 94.0}
# ]
#
# html = """
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor %}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>{{ user.year }}</li>
#         <li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=person)
#
# print(msg)
