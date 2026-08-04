teacher(t1, math).
teacher(t2, physics).

student(s1, math).
student(s2, physics).

teaches(T, S) :-
    teacher(T, Sub),
    student(S, Sub).