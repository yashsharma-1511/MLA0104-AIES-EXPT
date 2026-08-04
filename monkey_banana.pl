% initial state
state(at_door, on_floor, at_window, has_not).

% actions

move(state(at_door, on_floor, Box, Has),
     state(at_window, on_floor, Box, Has)).

push(state(at_window, on_floor, at_window, Has),
     state(at_middle, on_floor, at_middle, Has)).

climb(state(at_middle, on_floor, at_middle, Has),
      state(at_middle, on_box, at_middle, Has)).

grasp(state(at_middle, on_box, at_middle, has_not),
      state(at_middle, on_box, at_middle, has)).


% goal
can_get_banana :-
    state(A, B, C, D),
    move(state(A,B,C,D), S1),
    push(S1, S2),
    climb(S2, S3),
    grasp(S3, state(_,_,_,has)),
    write('Monkey got the banana!').