def sort_stack(input_stack):
    # Auxiliary stack to hold sorted elements
    helper_stack = []

    # Process each element in the input stack
    while input_stack:
        # Pop the top element from input_stack
        current = input_stack.pop()

        # While helper_stack is not empty and the top element is greater than current
        while helper_stack and helper_stack[-1] > current:
            # Move the elements from helper_stack back to input_stack
            input_stack.append(helper_stack.pop())

        # Push the current element onto the helper_stack
        helper_stack.append(current)

    # Transfer sorted elements back to input_stack
    while helper_stack:
        input_stack.append(helper_stack.pop())

    return input_stack
