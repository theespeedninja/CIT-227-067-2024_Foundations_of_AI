### Family Members

| Member  | Role                        | Gender |
|---------|-----------------------------|--------|
| Daniel  | Grandfather (paternal)      | Male   |
| Grace   | Grandmother (paternal)      | Female |
| James   | Grandfather (maternal)      | Male   |
| Mary    | Grandmother (maternal)      | Female |
| Peter   | Parent / Son of Daniel & Grace | Male   |
| Anne    | Parent / Daughter of Daniel & Grace | Female |
| Kevin   | Son of James & Mary         | Male   |
| Susan   | Daughter of James & Mary    | Female |
| Brian   | Grandchild / Son of Peter   | Male   |
| Linda   | Grandchild / Daughter of Peter | Female |
| Eric    | Grandchild / Son of Anne    | Male   |
| Rose    | Grandchild / Daughter of Anne | Female |

---

## Facts Defined

### Gender Facts
```prolog
male(daniel).   female(grace).
male(james).    female(mary).
male(peter).    female(anne).
male(kevin).    female(susan).
male(brian).    female(linda).
male(eric).     female(rose).
```

### Parent Facts
```prolog
parent(daniel, peter).    parent(james, kevin).
parent(daniel, anne).     parent(james, susan).
parent(grace, peter).     parent(mary, kevin).
parent(grace, anne).      parent(mary, susan).
parent(peter, brian).     parent(anne, eric).
parent(peter, linda).     parent(anne, rose).
```

---

## Rules Defined

| Rule | Meaning |
|------|---------|
| `father(X, Y)` | X is the father of Y if X is a male parent of Y |
| `mother(X, Y)` | X is the mother of Y if X is a female parent of Y |
| `child(X, Y)` | X is a child of Y if Y is a parent of X |
| `sibling(X, Y)` | X and Y are siblings if they share a common parent |
| `grandparent(X, Y)` | X is a grandparent of Y if X is a parent of Y's parent |
| `grandchild(X, Y)` | X is a grandchild of Y if Y is a grandparent of X |
| `uncle(X, Y)` | X is an uncle of Y if X is a male sibling of Y's parent |
| `aunt(X, Y)` | X is an aunt of Y if X is a female sibling of Y's parent |
| `cousin(X, Y)` | X and Y are cousins if their parents are siblings |

---

## Sample Queries

### Fathers and Mothers
```prolog
?- father(daniel, peter).       % true
?- mother(grace, anne).         % true
?- father(peter, X).            % X = brian ; X = linda
```

### Grandparents and Grandchildren
```prolog
?- grandparent(daniel, brian).  % true
?- grandparent(X, rose).        % X = daniel ; X = grace
?- grandchild(X, daniel).       % X = brian ; X = linda ; X = eric ; X = rose
```

### Siblings
```prolog
?- sibling(peter, anne).        % true
?- sibling(brian, X).           % X = linda
```

### Uncles and Aunts
```prolog
?- uncle(peter, eric).          % true
?- aunt(anne, brian).           % true
?- aunt(X, brian).              % X = anne
```

### Cousins
```prolog
?- cousin(brian, X).            % X = eric ; X = rose
?- cousin(X, Y).                % lists all cousin pairs
```

### All Grandparent Relationships
```prolog
?- grandparent(X, Y).           % lists every grandparent-grandchild pair
```

---

## Relationship Summary

| Relationship | Members |
|---|---|
| Grandparents | Daniel, Grace, James, Mary |
| Parents | Peter, Anne, Kevin, Susan |
| Grandchildren | Brian, Linda, Eric, Rose |
| Siblings | Peter & Anne / Kevin & Susan / Brian & Linda / Eric & Rose |
| Uncle | Peter is uncle to Eric and Rose |
| Aunt | Anne is aunt to Brian and Linda |
| Cousins | Brian & Linda are cousins to Eric & Rose |

---

## Author
@CIT-227-067/2024 - Danny Ngatia
Demonstrates Constraint Logic Programming using SWI-Prolog.