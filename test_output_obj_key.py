exec(open('f_output_obj_key.py').read())
print("Running test case for 'Example_A.json' file and key 'a/b/c'.  Result should be 'd'.")
print_obj_key("Example_A.json","a/b/c")
print("Running test case for 'Example_X.json' file and key 'x/y/z'.  Result should be 'a'.")
print_obj_key("Example_X.json","x/y/z")