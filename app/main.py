lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

sorted_variables = {
    "mutable": [],
    "immutable": []
}


def is_mutable(test_variable: any) -> bool:
    return (type(test_variable) is list or type(test_variable) is dict
            or type(test_variable) is set)


all_variables = [lucky_number, pi, one_is_a_prime_number, name,
                 my_favourite_films, profile_info, marks, collection_of_coins]

for test_variable in all_variables:
    if is_mutable(test_variable):
        sorted_variables["mutable"].append(test_variable)
    else:
        sorted_variables["immutable"].append(test_variable)
print(sorted_variables)
