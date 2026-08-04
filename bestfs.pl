% graph edges
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, e).
edge(d, f).
edge(e, f).

% best first search (simple path search)
bestfs(Start, Goal) :-
    path(Start, Goal, [Start]).

% goal reached
path(Goal, Goal, _) :-
    write('Reached Goal: '), write(Goal), nl.

% explore neighbours
path(Current, Goal, Visited) :-
    edge(Current, Next),
    \+ member(Next, Visited),
    write('Visiting: '), write(Next), nl,
    path(Next, Goal, [Next|Visited]).