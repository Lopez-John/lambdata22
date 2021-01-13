I like the way you handled the `split_dates` method by using the `datetime` module. 
Also, your docstrings are nice and descriptive so I can understand the method's behavior.
I would consider assigning `(int(len(df) * frac))` to a variable with a descriptive name such as `cutoff` and use that variable in
both `train_split` and `test_split` at lines 65 & 66 to improve readability of the `train_test_split` method.
