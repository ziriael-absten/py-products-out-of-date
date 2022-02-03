# Products out of date

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write tests for `outdated_products` function, that takes list 
of dictionaries
`products` and returns list of names of products that are out 
of date (expiration
date < today date). 
```python
print(outdated_products([
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    }
]))
# ['duck']
```
Mock the `datetime.date.today()` to check different variants.