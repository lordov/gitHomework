import random


class Ball:
    counter = 0
    total_weight = 0

    def __init__(self, weight):
        self.weight = weight
        Ball.total_weight += self.weight
        Ball.counter += 1


ball_list = []
while Ball.counter < 1000 and Ball.total_weight < 350:
    ball_list.append(Ball(random.uniform(0.2, 0.5)))
   

print('A limit has been reached. The order details:')
print("# of balls:", Ball.counter)
print('total weight:', round(Ball.total_weight, 2))
for  n, i in enumerate(ball_list):
    print(f'N {n + 1} {round(i.weight, 2)}')


if __name__ == '__main__':
    print('home_work_12_1.py запущена сама по себе')
else:
    print('home_work_12_1.py импортирована')  
