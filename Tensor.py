# def tensor_creation(Z):
#   """
#   A function that creates various tensors.
#
#   Args:
#     Z: numpy.ndarray
#       An array of shape (3,4)
#
#   Returns:
#     A : Tensor
#       20 by 21 tensor consisting of ones
#     B : Tensor
#       A tensor with elements equal to the elements of numpy array Z
#     C : Tensor
#       A tensor with the same number of elements as A but with values ∼U(0,1)
#     D : Tensor
#       A 1D tensor containing the even numbers between 4 and 40 inclusive.
#   """
#   #################################################
#   ## TODO for students: fill in the missing code
#   ## from the first expression
#   raise NotImplementedError("Student exercise: say what they should have done")
#   #################################################
#   A = ...
#   B = ...
#   C = ...
#   D = ...
#
#   return A, B, C, D
#
#
# # numpy array to copy later
# Z = np.vander([1, 2, 3], 4)
#
# # Uncomment below to check your function!
# # A, B, C, D = tensor_creation(Z)
# # checkExercise1(A, B, C, D)