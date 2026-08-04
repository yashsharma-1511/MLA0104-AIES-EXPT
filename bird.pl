bird(sparrow).
bird(pigeon).
bird(penguin).

% rule: birds can fly except penguin
can_fly(X) :-
    bird(X),
    X \= penguin.