
# Project is available in https://repl.it/@lastlost/boilerplate-probability-calculator#prob_calculator.py

import copy
import random

# Consider using the modules imported above.

class Hat :

    contents = list()

    def __init__(self, **kwargs) :
        contents = list()
        for color, key in kwargs.items() :
            for i in range(key) :
                contents.append(color)
        self.contents = contents

    def draw(self, num) :
        removed_balls = list()
        if len(self.contents) <= num :
            return self.contents
        else :
            for i in range(num) :
                random_ball_index = random.randint(0, len(self.contents)-1)
                random_ball = self.contents[random_ball_index]
                removed_balls.append(random_ball)
                del self.contents[random_ball_index]
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) :
    count = 0
    for num in range(num_experiments) :
        hat1 = copy.deepcopy(hat)
        draw_list = list()
        draw_dict = dict()
        flag = list()
        draw_list.append(hat1.draw(num_balls_drawn))
        for values in draw_list :
            for val in values :
                draw_dict[val] = draw_dict.get(val, 0) + 1
        for color, key in expected_balls.items() :
            if draw_dict.get(color, 0) >= expected_balls.get(color, 0) :
                flag.append(1)
        if flag.count(1) == len(expected_balls):
            count += 1
    probability = count/num_experiments
    return probability
