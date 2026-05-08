#@Danny Ngatia
# Part (a) - the Australlian map
# %%
regions=['WA','NT','SA','Q','NSW'] # defining the variables - regions of australia to be colored
"""Key:
WA - Western Australia
NT - Northern Territory
SA - South Australia
Q - Queensland
NSW - New South Wales
"""
colors = ['blue','red','green'] # defining the domain - the colors to be used for coloring the regions
# using an adjaceny list to represent the contraints: bordering regions
border_regions ={
    ('WA','NT'),
    ('WA','SA'),
    ('NT','SA'),
    ('NT','Q'),
    ('SA','Q'),
    ('SA','NSW'),
    ('Q','NSW')
}
""" OR you can use a dictionary to represent the constraints:
border_regions = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q"]
}
"""

# %%
#check if assigning a color to a region is valid based on the constraints
def valid(region, color, regions_colors): # regions_colors is a dictionary that holds the current color assignment for each region
    for (r1, r2) in border_regions:
        if r1 == region and r2 in regions_colors:
            if regions_colors[r2]==color:
                return False
        if r2 == region and r1 in regions_colors:
            if regions_colors[r1]==color:
                return False
    return True

#%%
# The backtracking search function to assign colors to regions while respecting the constraints
def backtrack(regions_colors):
    # Base case: if all regions are assigned, we are done
    if len(regions_colors) == len(regions):
        return regions_colors
    
    # Pick the next unassigned region
    unassigned_region = [r for r in regions if r not in regions_colors]
    curr_region = unassigned_region[0] # current unassigned region to try to assign a color to

    # Try each colour for this region
    for color in colors:
        if valid(curr_region, color, regions_colors):
            # Assign the colour
            regions_colors[curr_region] = color
            
            # Recurse - try to assign the rest
            result = backtrack(regions_colors)
            if result is not None:
                return result
        
            # If it didn't work, remove and try next colour
            del regions_colors[curr_region]
    
    # No colour worked, return None to trigger backtracking
    return None

#%%
# Start the backtracking search with an empty assignment
final_colors = backtrack({})
# Print the result
if final_colors:
    print("\nSolution found!\nColoring now")
    for region, color in final_colors.items():
        print(f"  {region} --> {color}")
else:
    print("No solution exists.Cannot color the map with the given constraints and colors.")



# %%
