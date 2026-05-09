# Task 2 - Map Coloring Using Constraint Satisfaction Problem (CSP)

## Overview
This project solves the classic **Graph Coloring Problem** using backtracking search to color geographical regions with the minimum number of colors such that no two adjacent regions share the same color.

### Part (a): Australia Map
Colors 5 Australian regions (WA, NT, SA, Q, NSW) with 3 colors.

### Part (b): Nairobi Map
Colors 17 sub-counties of Nairobi with automatically determined minimum colors based on the IEBC map.

## What Was Done

### 1. **Problem Definition**
   - **Regions** (Part b - Nairobi): 17 sub-counties
     - Westlands, Dagoretti North/South, Langata, Kibra, Roysambu, Kasarani, Ruaraka
     - Embakasi (South, North, Central, East, West), Makadara, Kamukunji, Starehe, Mathare
   - **Domain**: Variable number of colors (minimum finder starts with 3)
   - **Constraints**: Bordering regions cannot have the same color

### 2. **Constraint Representation**
   - Used an adjacency list to represent border relationships between regions
   - Defined 32 border constraints based on actual IEBC Nairobi map adjacencies
   - Each adjacency pair ensures that bordering sub-counties have different colors

### 3. **Validity Check Function**
   - `is_valid()` function checks if assigning a color to a region is valid
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

### 5. **Automatic Minimum Color Finder**
   - `find_minimum_colors()` function automatically determines the minimum colors needed
   - Starts with 3 colors and incrementally increases until a solution is found
   - Returns the solution using the minimum number of colors required
   - Displays progress as it tests different color counts

### 6. **Solution Finding & Output**
   - Automatically finds the minimum number of colors needed to color all regions
   - Prints all regions with their assigned colors and the number of colors used
   - Displays region names in readable format (underscores replaced with spaces)
   - Shows colored assignment clearly for verification

## Key Concepts
- **Constraint Satisfaction Problem (CSP)**: Systematically solve problems with variables, domains, and constraints
- **Backtracking Search**: Efficiently explore the solution space by abandoning partial solutions that violate constraints
- **Graph Coloring**: Assign colors to nodes such that no adjacent nodes have the same color
- **Optimization**: Finding the minimum number of colors (minimum chromatic number) needed for a valid coloring

## Technologies Used
- **Python**: Core implementation language
- **Data Structures**: Lists and dictionaries for constraint representation and assignments

## Files
- `task2(a)-mapofAustralia.py`: Australia map coloring solver
- `task2(b)-mapofNairobi.py`: Nairobi map coloring solver with automatic minimum color detection
- `readme.md`: This file

---

**Copyright © 2024 @Danny Ngatia - CIT-227-067/2024 #theespeedninja**
