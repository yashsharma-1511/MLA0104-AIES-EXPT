# MLA0104 - Artificial Intelligence and Expert Systems (AIES) Experiments

This repository contains implementations of core AI search and game-playing algorithms completed as part of the MLA0104 - AIES course.

---

## 1. Breadth First Search (BFS)

```
BFS(graph, start, goal):
    queue = [start]
    visited = {start}

    while queue is not empty:
        node = queue.dequeue()
        if node == goal: return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
```

---

## 2. Depth First Search (DFS)

```
DFS(graph, node, goal, visited = {}):
    visited.add(node)
    if node == goal: return True

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, goal, visited)
```

---

## 3. Uniform Cost Search (UCS)

```
UCS(graph, start, goal):
    PQ = [(0, start)]     // (cost, node)
    visited = {}

    while PQ not empty:
        cost, node = PQ.pop_min()
        if node == goal: return cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                PQ.insert((cost + edge_cost, neighbor))
```

---

## 4. Water Jug Problem

```
WaterJug(cap1, cap2, target):
    queue = [(0, 0)]
    visited = {(0,0)}

    while queue not empty:
        j1, j2 = queue.dequeue()
        if j1 == target or j2 == target: return solved

        states = [(cap1,j2), (j1,cap2), (0,j2), (j1,0),
                  pour(j1->j2), pour(j2->j1)]

        for s in states:
            if s not in visited:
                visited.add(s)
                queue.enqueue(s)
```

---

## 5. A* Search Algorithm

```
A_Star(graph, start, goal, h):
    OPEN = [(h[start], start)]
    g = {start: 0}

    while OPEN not empty:
        f, node = OPEN.pop_min()
        if node == goal: return path

        for neighbor, cost in graph[node]:
            temp_g = g[node] + cost
            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                OPEN.insert((temp_g + h[neighbor], neighbor))
```

---

## 6. Alpha-Beta Pruning

```
AlphaBeta(node, depth, alpha, beta, isMax):
    if depth == 0 or node is terminal: return evaluate(node)

    if isMax:
        best = -INF
        for child in node.children:
            best = max(best, AlphaBeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = +INF
        for child in node.children:
            best = min(best, AlphaBeta(child, depth-1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha: break
        return best
```

---

## 7. Minimax Algorithm

```
Minimax(node, depth, isMax):
    if depth == 0 or node is terminal: return evaluate(node)

    if isMax:
        return max(Minimax(child, depth-1, False) for child in node.children)
    else:
        return min(Minimax(child, depth-1, True) for child in node.children)
```

---

## 8. Greedy Best First Search (GBFS)

```
GBFS(graph, start, goal, h):
    PQ = [(h[start], start)]
    visited = {}

    while PQ not empty:
        _, node = PQ.pop_min()
        if node == goal: return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                PQ.insert((h[neighbor], neighbor))
```

---

---
---


---
---

# MLA0105 - Prolog Programming Experiments

This section contains Prolog program pseudocode for AI/logic programming lab experiments.

---

## 1. Sum of Integers from 1 to n

```prolog
sum(0, 0).
sum(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum(N1, Sum1),
    Sum is Sum1 + N.

% Query: ?- sum(5, S).
```

---

## 2. DB with Name, DOB

```prolog
person(john, date(12, 5, 2000)).
person(mary, date(23, 8, 1999)).
person(alex, date(1, 1, 2001)).

% Query: ?- person(john, DOB).
% Query: ?- person(Name, date(_, _, 2000)).
```

---

## 3. STUDENT-TEACHER-SUB-CODE

```prolog
teaches(mr_smith, cs101).
teaches(mr_smith, cs102).
teaches(mrs_jones, cs201).

studies(john, cs101).
studies(mary, cs201).

taughtBy(Student, Teacher) :-
    studies(Student, Sub),
    teaches(Teacher, Sub).

% Query: ?- taughtBy(john, Teacher).
```

---

## 4. PLANETS DB

```prolog
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).

distanceFromSun(Planet, Position) :-
    planet(Planet, Position).

% Query: ?- planet(earth, Pos).
% Query: ?- planet(Planet, 3).
```

---

## 5. Towers of Hanoi

```prolog
hanoi(0, _, _, _) :- !.
hanoi(N, Source, Target, Aux) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, Source, Aux, Target),
    write('Move disk from '), write(Source), write(' to '), write(Target), nl,
    hanoi(N1, Aux, Target, Source).

% Query: ?- hanoi(3, left, right, middle).
```

---

## 6. Bird - Can Fly or Not

```prolog
bird(sparrow).
bird(penguin).
bird(eagle).

cannotFly(penguin).

canFly(Bird) :-
    bird(Bird),
    \+ cannotFly(Bird).

% Query: ?- canFly(sparrow).
% Query: ?- canFly(penguin).
```

---

## 7. Family Tree

```prolog
female(pam). female(liz). female(ann). female(pat).
male(tom). male(bob). male(jim).

parent(tom, bob). parent(tom, liz).
parent(pam, bob). parent(pam, liz).
parent(bob, ann). parent(bob, jim).
parent(pat, ann). parent(pat, jim).

mother(M, C)      :- parent(M, C), female(M).
father(F, C)      :- parent(F, C), male(F).
grandfather(GF, C):- father(GF, P), parent(P, C).
grandmother(GM, C):- mother(GM, P), parent(P, C).

sister(S, C) :- female(S), parent(P, S), parent(P, C), S \== C.
brother(B, C):- male(B),   parent(P, B), parent(P, C), B \== C.

% Query: ?- mother(pam, bob).
% Query: ?- grandfather(tom, ann).
```

---

## 8. Diet Suggestion System based on Disease

```prolog
diet(diabetes, 'Low sugar, high fiber diet').
diet(hypertension, 'Low sodium diet').
diet(obesity, 'Low calorie, high protein diet').
diet(anemia, 'Iron rich diet').

suggestDiet(Disease, Diet) :-
    diet(Disease, Diet).

% Query: ?- suggestDiet(diabetes, D).
```

---

## 9. Monkey Banana Problem

```prolog
% State: state(MonkeyPos, MonkeyOnBox, BoxPos, HasBanana)

move(state(middle, onbox, middle, has),
     grasp,
     state(middle, onbox, middle, has)).

move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

move(state(P1, onfloor, P1, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

move(state(P1, onfloor, B, H),
     walk(P1, P2),
     state(P2, onfloor, B, H)).

canGet(state(_, _, _, has)).
canGet(State1) :-
    move(State1, _, State2),
    canGet(State2).

% Query: ?- canGet(state(atdoor, onfloor, atwindow, hasnot)).
```

---

## 10. Fruit and its Color using Backtracking

```prolog
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, green).
fruit(orange, orange).

findFruit(Color, Fruit) :-
    fruit(Fruit, Color).

% Query: ?- findFruit(red, F).
% Backtrack with ';' to find all matches:
% Query: ?- fruit(F, C).
```

---

## 11. Best First Search Algorithm

```prolog
% Facts: edge(Node1, Node2, Cost). heuristic(Node, H).

bestFirstSearch(Start, Goal, Path) :-
    bfSearch([[Start]], Goal, Path).

bfSearch([[Goal | Rest] | _], Goal, [Goal | Rest]).
bfSearch([Path | OtherPaths], Goal, SolutionPath) :-
    Path = [Node | _],
    findall([NextNode | Path],
            (edge(Node, NextNode, _), \+ member(NextNode, Path)),
            NewPaths),
    append(OtherPaths, NewPaths, AllPaths),
    sortByHeuristic(AllPaths, SortedPaths),
    bfSearch(SortedPaths, Goal, SolutionPath).

% Query: ?- bestFirstSearch(a, g, Path).
```

---

## 12. Medical Diagnosis

```prolog
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).

disease(flu, [fever, cough, headache]).
disease(measles, [fever, rash, cough]).
disease(migraine, [headache]).

diagnose(Symptoms, Disease) :-
    disease(Disease, DiseaseSymptoms),
    subset(Symptoms, DiseaseSymptoms).

subset([], _).
subset([H|T], L) :- member(H, L), subset(T, L).

% Query: ?- diagnose([fever, cough], D).
```

---

## 13. Forward Chaining

```prolog
% Facts and rules
fact(bird(tweety)).
rule(has_feathers(X) :- bird(X)).
rule(can_fly(X) :- bird(X), \+ penguin(X)).

forwardChain(Facts, Rules, NewFacts) :-
    findall(Head,
            ( member((Head :- Body), Rules),
              call(Body),
              \+ member(Head, Facts) ),
            Derived),
    ( Derived == [] -> NewFacts = Facts
    ; append(Facts, Derived, UpdatedFacts),
      forwardChain(UpdatedFacts, Rules, NewFacts) ).

% Query: ?- forwardChain([bird(tweety)], [has_feathers(tweety):-bird(tweety)], Facts).
```

---

## 14. Backward Chaining

```prolog
% Facts
bird(tweety).
mammal(cat).

% Rules
canFly(X) :- bird(X), \+ penguin(X).
hasFur(X) :- mammal(X).

% Backward chaining is Prolog's native resolution strategy:
% Goal is proved by matching against facts/rules, recursively
% proving each sub-goal in the rule body (right to left).

% Query: ?- canFly(tweety).
% Prolog backtracks through the rule body: bird(tweety) -> true,
% \+ penguin(tweety) -> true => canFly(tweety) succeeds.
```

---

## Author

**Yash Sharma**
SIMATS Engineering
Course: MLA0104 / MLA0105 - Artificial Intelligence, Expert Systems & Logic Programming
