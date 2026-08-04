% symptoms
symptom(fever).
symptom(cough).
symptom(headache).

% diseases
disease(flu) :-
    symptom(fever),
    symptom(cough).

disease(migraine) :-
    symptom(headache).