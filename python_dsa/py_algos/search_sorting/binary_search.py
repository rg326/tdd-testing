# BINARY SEARCH (Team Teehouse and freeCodeCamp)

# Steps

# We determine the middle pos of the sorted list
# We compare the element in middle pos to the target element
# If the elements match we return the middle pos and end
# If not, we check whether the element in the middle pos is smaller than the target element. If it is smaller, we go back to step two with a new list that ranges from the middle of the current list to the end of the current list
# If the element in the middle pos is greater than the target element, then we go back to step 2, with a new list that ranges to the start of the current list to the middle of the position of the current list
# We continue until the target element is found, or until the sublist contains only one element
# If that single sublist does not contain the target element, then we end the algorithm, indicating that the target element does not exist in the list.

# GUIDELINES
# - List must be sorted
