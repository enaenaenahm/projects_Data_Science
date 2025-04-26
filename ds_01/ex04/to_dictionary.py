def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    dict = {}
    for country, num in list_of_tuples:
        if num in dict:
            dict[num].append(country)
        else:
            dict[num] = [country]
    for num, countries in dict.items():
        for country in countries:
            print(f"'{num}' : '{country}'")

if __name__ == '__main__':
    to_dictionary()