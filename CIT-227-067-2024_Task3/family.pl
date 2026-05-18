/* ── GENDER FACTS ─────────────────────────── */
male(daniel).
male(james).
male(peter).
male(kevin).
male(brian).
male(eric).

female(grace).
female(mary).
female(anne).
female(susan).
female(linda).
female(rose).

/* ── PARENT FACTS ─────────────────────────── */
/* parent(Parent, Child) */
parent(daniel, peter).
parent(daniel, anne).
parent(grace, peter).
parent(grace, anne).

parent(james, kevin).
parent(james, susan).
parent(mary, kevin).
parent(mary, susan).

parent(peter, brian).
parent(peter, linda).
parent(anne, eric).
parent(anne, rose).

/* ── BASIC RULES ──────────────────────────── */

% Father: a parent who is male
father(X, Y) :- parent(X, Y), male(X).

% Mother: a parent who is female
mother(X, Y) :- parent(X, Y), female(X).

% Child: Y is a child of X
child(X, Y) :- parent(Y, X).

% Sibling: two people who share the same parent
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

/* ── EXTENDED FAMILY RULES ────────────────── */

% Grandparent: a parent of a parent
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Grandchild: reverse of grandparent
grandchild(X, Y) :- grandparent(Y, X).

% Uncle: a male sibling of one's parent
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).

% Aunt: a female sibling of one's parent
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).

% Cousin: children of siblings
cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).