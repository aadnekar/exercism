def recite(start_verse, end_verse):
    return [day_string(verse) for verse in range(start_verse, end_verse+1)]


def day_string(number):
    all_verses = [
        {'number': 'first', 'text': ' and a Partridge in a Pear Tree.'},
        {'number': 'second', 'text': ' two Turtle Doves,'},
        {'number': 'third', 'text': ' three French Hens,'},
        {'number': 'fourth', 'text': ' four Calling Birds,'},
        {'number': 'fifth', 'text': ' five Gold Rings,'},
        {'number': 'sixth', 'text': ' six Geese-a-Laying,'},
        {'number': 'seventh', 'text': ' seven Swans-a-Swimming,'},
        {'number': 'eighth', 'text': ' eight Maids-a-Milking,'},
        {'number': 'ninth', 'text': ' nine Ladies Dancing,'},
        {'number': 'tenth', 'text': ' ten Lords-a-Leaping,'},
        {'number': 'eleventh', 'text': ' eleven Pipers Piping,'},
        {'number': 'twelfth', 'text': ' twelve Drummers Drumming,'}
    ]
    if number == 1:
        return 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.'
    text = [verse['text'] for verse in all_verses][:number]
    text.reverse()
    return 'On the {} day of Christmas my true love gave to me:{}'.format(all_verses[number-1]['number'], ''.join(text))
