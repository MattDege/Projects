#Matthew DiGirolamo
#Structify Take Home Question 


def count_intersections(points, identifiers):
    intersections = 0
    active_chords = 0

    combined_points = sorted(zip(points, identifiers), key=lambda x: x[0])

    for point, chord_type in combined_points:
        if chord_type[0] == 's':
            active_chords += 1
            intersections += active_chords - 1  # Add intersections with existing chords
        else:
            active_chords -= 1

    return intersections

# Example usage using numbers from the first example in the document. 
points = [0.78, 1.47, 1.77, 3.92]
identifiers = ["s_1", "s_2", "e_1", "e_2"]

result = count_intersections(points, identifiers)
print(f"Number of intersections: {result}")
