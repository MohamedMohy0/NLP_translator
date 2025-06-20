import dill 

with open("Source_Target.pkl", 'rb') as f:
    model = dill.load(f)

def translate_with_model(model, sentence):
    words = sentence.split()
    translated = []
    for word in words:
        if word in model.translation_table:
            probs = model.translation_table[word]
            best_word = max(probs, key=probs.get)
            translated.append(best_word)
        else:
            translated.append(word)  
    return ' '.join(translated)

# Example usage
sentence = "Text"
translation = translate_with_model(model, sentence)
print(translation)