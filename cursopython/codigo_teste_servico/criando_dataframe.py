import pandas as pd

fruit_dict = {
    # 3: 'apple',
    # 2: 'banana',
    # 6:'mango',
    # 4:'apricot',
    # 1:'kiwi',
    'date': {
       '2021-09-25'
    }
}

print(pd.DataFrame(list(fruit_dict.items()),
                   columns=['Quantity', 'FruitName', 'Date']))
