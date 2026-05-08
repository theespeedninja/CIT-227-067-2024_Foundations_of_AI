# Task 2 - Australian Map Coloring Using Constraint Satisfaction Problem (CSP)

## Overview
This project solves the classic **Graph Coloring Problem** using backtracking search to color the regions of Australia with the minimum number of colors such that no two adjacent regions share the same color.

## What Was Done

### 1. **Problem Definition**
   - **Regions**: 5 Australian regions defined:
     - WA (Western Australia)
     - NT (Northern Territory)
     - SA (South Australia)
     - Q (Queensland)
     - NSW (New South Wales)
   - **Domain**: 3 colors available (blue, red, green)
   - **Constraints**: Bordering regions cannot have the same color

### 2. **Constraint Representation**
   - Used an adjacency set to represent border relationships between regions
   - Defined 7 border constraints:
     - WA borders: NT, SA
     - NT borders: WA, SA, Q
     - SA borders: WA, NT, Q, NSW
     - Q borders: NT, SA, NSW
     - NSW borders: SA, Q

### 3. **Validity Check Function**
   - `valid()` function checks if assigning a color to a region is valid
   - Verifies that no bordering region has already been assigned the same color
   - Returns True if the assignment respects all constraints, False otherwise

### 4. **Backtracking Search Algorithm**
   - `backtrack()` function implements the backtracking search to solve the CSP
   - **Base case**: All regions are colored → return the solution
   - **Recursive case**: 
     - Pick an unassigned region
     - Try each available color
     - If valid, assign the color and recurse
     - If recursion succeeds, return the solution
     - If recursion fails, backtrack by removing the assignment and trying the next color
   - Returns None if no valid coloring exists

### 5. **Solution Finding & Output**
   - Starts the backtracking search with an empty assignment
   - Prints all regions with their assigned colors if a solution is found
   - Displays an error message if no valid coloring exists with the given constraints

## Key Concepts
- **Constraint Satisfaction Problem (CSP)**: Systematically solve problems with variables, domains, and constraints
- **Backtracking Search**: Efficiently explore the solution space by abandoning partial solutions that violate constraints
- **Graph Coloring**: Assign colors to nodes such that no adjacent nodes have the same color

## Technologies Used
- **Python**: Core implementation language
- **Data Structures**: Sets and dictionaries for constraint representation

## Files
- `task2.py`: Main Python script implementing the CSP solver
- `readme.md`: This file

---

**Copyright © 2024 @Danny Ngatia - CIT-227-067/2024 #theespeedninja**
