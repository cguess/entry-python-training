def format_as_percentage(nominator, denominator):
    division_result = int(nominator)*100 / (int(denominator))
    rounded_division_result = round(division_result, 3)
    print(rounded_division_result, '%')

format_as_percentage('2', '4')
format_as_percentage('1', '3')
