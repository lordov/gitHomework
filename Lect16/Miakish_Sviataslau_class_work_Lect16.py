import requests
import socket
import json


# url = 'http://127.0.0.1/openserver/phpmyadmin/index.php'
# resp = requests.get(url)

# print(resp.status_code)


# server_addr = input('What server do you want to connect to?')
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# electron = 1.60212
# print(json.dumps(electron))

# comics = '"the meaning of life" by monty Pyhton\'s Flying Circus'
# print(json.dumps(comics))

# my_l = [1, 2.34, True, 'False', None, ['a', 0]]
# print(json.dumps(my_l))

# my_dict = {'me': 'Python', 'pi': 3.14}
# print(json.dumps(my_dict))

# class Who:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def encode_who(w):
#     if isinstance(w, Who):
#         return w.__dict__
#     else:
#         raise TypeError(w.__class__.__name__ + ' is not JSON serializable')


# class MyEncoder(json.JSONEncoder):
#     def default(self, w):
#         if isinstance(w, Who):
#             return w.__dict__
#         return super().default(self, w)


# def decode_who(w):
#     return Who(w['name'], w['age'])

# class MyDecoder(json.JSONDecoder):
#     def __init__(self):
#         json.JSONDecoder.__init__(self, object_hook=self.decode_who)

#     def decode_who(self, d):
#         return Who(**d)

# old_man = Who('jane Dohe', 23)
# json_str = json.dumps(old_man, cls=MyEncoder)
# new_man = json.loads(json_str, cls=MyDecoder)

# print(type(new_man))
# print(new_man.__dict__)

import requests

reply = requests.get('http://localhost:3000')

if reply.status_code == requests.codes.ok:
    print('ALL RIGHT!')
else:
    print('BAD!')


print(reply.status_code)
print(reply.headers)
print(reply.headers['Content-Type'])

print()
print(requests.codes.__dict__)
