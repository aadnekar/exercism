FACTOR_OF_THREE = 'Pling'
FACTOR_OF_FIVE = 'Plang'
FACTOR_OF_SEVEN = 'Plong'

def raindrops(number):
    result = ''
    if number % 3 == 0:
        result += FACTOR_OF_THREE
    if number % 5 == 0:
        result += FACTOR_OF_FIVE
    if number % 7 == 0:
        result += FACTOR_OF_SEVEN
    result = result if len(result) > 0 else str(number)
    return result    
