def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows):
        string = []
        for j in range(1, num_columns):
            string.append(str(operation(i,j)))
        print(" ".join(string))
        
print_operation_table(lambda x, y: x * y)