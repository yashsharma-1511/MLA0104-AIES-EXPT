fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).

find_color(Fruit, Color) :-
    fruit(Fruit, Color).