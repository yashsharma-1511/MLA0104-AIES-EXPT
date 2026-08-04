% known facts
fact(a).
fact(b).

% rule
fact(c) :-
    fact(a),
    fact(b).