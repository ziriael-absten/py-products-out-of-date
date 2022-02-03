# Products out of date

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write tests for `outdated_products` function, that takes dictionary
`products` and returns list of names of products that are out 
of date (expiration
date < today date). Argument `products` is dictionary, where keys are
names of the products and values are their expiration dates.
```python
print(outdated_products(
    {
        "salmon": datetime.date(2022, 2, 10),
        "chicken": datetime.date(2022, 2, 5),
        "duck": datetime.date(2022, 2, 1)
    }
))
# ['duck']
```
Mock the `datetime.date.today()` to check different variants.