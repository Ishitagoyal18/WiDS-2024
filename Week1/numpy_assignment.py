import numpy as np

def main():
    # Example matrix
    mat = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Original Matrix:")
    print(mat)

    # Number of rotations
    k = 2  # Rotate 90 degrees clockwise two times

    # Call your function
    rotated_matrix = rotate_matrix(mat, k)

    print(f"\nMatrix after {k} rotations:")
    print(rotated_matrix)

# Task: Write this function
def rotate_matrix(mat, k):
    """
    Rotates a 2D matrix 90 degrees clockwise k times.

    Args:
        mat (ndarray): The 2D NumPy array to rotate.
        k (int): The number of 90-degree clockwise rotations.

    Returns:
        ndarray: The rotated 2D NumPy array.
    """
    pass  # Replace this with your implementation

if _name_ == "_main_":
    main()
