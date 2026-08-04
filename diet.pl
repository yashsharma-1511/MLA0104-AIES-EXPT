diet(diabetes, low_sugar).
diet(obesity, low_fat).
diet(anemia, iron_rich).

suggest(Disease, Diet) :-
    diet(Disease, Diet).