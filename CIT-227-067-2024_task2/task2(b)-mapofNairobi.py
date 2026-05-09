#@Danny Ngatia CIT-227-067-2024 Task 2 (b) - Map of Nairobi
# %%
# The 17 sub-counties of Nairobi the variables of the problem
regions = [
    'Westlands', 'Dagoretti_North', 'Dagoretti_South', 'Langata', 'Kibra',
    'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi_South', 'Embakasi_North',
    'Embakasi_Central', 'Embakasi_East', 'Embakasi_West', 'Makadara',
    'Kamukunji', 'Starehe', 'Mathare'
]

# need to use MINIMUM number of colours so starting with 3 and increase until a solution is found
colors = ['Red', 'Blue', 'Green']

# the Real bordering of each subcounty based on Nairobi's IEBC map
adjacencies = [
    ('Westlands', 'Dagoretti_North'),
    ('Westlands', 'Roysambu'),
    ('Westlands', 'Kasarani'),
    ('Dagoretti_North', 'Dagoretti_South'),
    ('Dagoretti_North', 'Kibra'),
    ('Dagoretti_North', 'Starehe'),
    ('Dagoretti_South', 'Langata'),
    ('Dagoretti_South', 'Kibra'),
    ('Langata', 'Kibra'),
    ('Langata', 'Embakasi_South'),
    ('Kibra', 'Starehe'),
    ('Kibra', 'Embakasi_West'),
    ('Roysambu', 'Kasarani'),
    ('Roysambu', 'Ruaraka'),
    ('Roysambu', 'Mathare'),
    ('Kasarani', 'Ruaraka'),
    ('Kasarani', 'Embakasi_North'),
    ('Ruaraka', 'Mathare'),
    ('Ruaraka', 'Embakasi_North'),
    ('Embakasi_South', 'Embakasi_West'),
    ('Embakasi_South', 'Embakasi_East'),
    ('Embakasi_North', 'Embakasi_Central'),
    ('Embakasi_North', 'Embakasi_East'),
    ('Embakasi_Central', 'Embakasi_West'),
    ('Embakasi_Central', 'Embakasi_East'),
    ('Embakasi_Central', 'Makadara'),
    ('Embakasi_West', 'Makadara'),
    ('Makadara', 'Kamukunji'),
    ('Makadara', 'Starehe'),
    ('Kamukunji', 'Starehe'),
    ('Kamukunji', 'Mathare'),
    ('Starehe', 'Mathare'),
]
print("\nSuccessfully defined the variables(subcounties), the domain (colors) and the constraints (adjacencies) for the Nairobi map coloring problem.")

#%%
# Check if assigning a color to a subcounty is valid
def is_valid(assignment, region, color):
    for (r1, r2) in adjacencies:
        if r1 == region and r2 in assignment:
            if assignment[r2] == color:
                return False
        if r2 == region and r1 in assignment:
            if assignment[r1] == color:
                return False
    return True

#%%
# Backtracking search to assign colours to subcounties while respecting the constraints
def backtrack(assignment, colors):
    if len(assignment) == len(regions):
        return assignment
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]
    for color in colors:
        if is_valid(assignment, region, color):
            assignment[region] = color
            result = backtrack(assignment, colors)
            if result is not None:
                return result
            del assignment[region]
    return None

# %%
# Automatically find the minimum number of colors needed
def find_minimum_colors():
    num_colors = 3           # start with 3 colors
    while num_colors <= 17:     # worst case: one color per region
        colors = ['Red', 'Blue', 'Green', 'Yellow','Purple', 'Orange'][:num_colors]
        print(f"Trying with {num_colors} colour(s)...")
        result = backtrack({}, colors)
        if result is not None:
            return num_colors, result, colors
        num_colors += 1
    return None, None, None

# %%
# Run the minimum color finder
num_colors, solution, colors_used = find_minimum_colors()

# Print the result
if solution:
    print(f"\n Solution found using {num_colors} colors!")
    print(f" Colors used: {colors_used}")
    print("-" * 35)
    for region, color in solution.items():
        print(f"  {region.replace('_', ' '):<20} --> {color}")
else:
    print("No solution found.")
# %%
