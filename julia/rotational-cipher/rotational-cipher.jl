
# All symbols in the alphabet: We only include lowerletters in this task.
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
LENGTH = length(SYMBOLS)
alphabet = Dict{Char, Int}()
for i in 1:LENGTH
    push!(alphabet, (SYMBOLS[i] => i))
end

function rotate(n::Integer, input::Union{String, Char})
    translated = ""
    input_type_char = typeof(input)==Char
    print("$input = $input_type_char")
    for symbol in input
        if !(lowercase(symbol) in SYMBOLS)
            # append the translated with symbol which is not part of the alphabet.
            translated *= symbol
        elseif lowercase(symbol) in SYMBOLS
            valueOfSymbol = alphabet[lowercase(symbol)]
            if valueOfSymbol + n > LENGTH
                position_alph = valueOfSymbol + n - LENGTH
            else
                position_alph = valueOfSymbol + n
            end
            if islowercase(symbol)
                translated *= SYMBOLS[position_alph]
            else
                translated *= uppercase(SYMBOLS[position_alph])
            end
        end
    end
    if input_type_char
        return translated[1]
    end
    translated
end
