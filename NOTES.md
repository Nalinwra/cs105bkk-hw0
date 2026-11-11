# HW0 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
I tried to implement the three functions: add_item(), total_items(), and running_low() in inventory.py. I used dictionary methods, loops, and sorted() to complete the tasks.

## What broke, and how did you fix it?
At first, the functions had raise NotImplementedError, so they could not work. I replaced them with the correct code. I also used .copy() in add_item() to make sure the original inventory did not change.

## What would you do differently next time?
Next time, I would read the instructions more carefully, understand the expected output, and test each function separately before running python -m pytest.