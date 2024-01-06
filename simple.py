# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += 5
        sd.circle(center_position=point, radius=radius, width=2)


# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):


# Нарисовать 10 пузырьков
# TODO здесь ваш год
for _ in range(100):
        point = sd.random_point()
        bubble(point=point, step=5)


sd.pause()
# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш год

