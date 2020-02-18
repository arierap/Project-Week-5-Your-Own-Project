#Function to narrow down locations
def catch_phrase(df):
    
    joey = ["How're you doing?", 
    "Hey, how you doin’?", 
    "Hey, how you doin’?",
    "How you doin’?",
    "How you doin?",
    "How you doin'?",
    "How you doin'?",
    "how you doin'?",
    "Hey! How you doin’?",
    "How you doin?",
    "Hey, (in the Joey voice) how you doin’?",
    "how you doin’?",
    "How you doin’?",
    "Hey, how you doin’?",
    "How you doing?"]

    ross_pattern = ['dinosaur',
    'dinosaurs',
    'palaeontology',
    'palaeontologist']

    break_pattern = ['on a break', 'ON a break', 'ON A BREAK']

    smelly_cat_pattern = ['smelly cat', 'SMELLY CAT', 'Smelly Cat', 'Smelly cat']

    phrase1 = '|'.join(joey)
    phrase2 = '|'.join(ross_pattern)
    phrase3 = '|'.join(break_pattern)
    phrase4 = '|'.join(smelly_cat_pattern)
    phrase5 = 'my god'

    df['catch_phrase'] = ''
    df.loc[(df['text'].str.contains(phrase1)) & (df['character'] == 'Joey'), 'catch_phrase'] = 'How you doin!'
    df.loc[df['text'].str.contains(phrase2), 'catch_phrase'] = 'Dinosaurs!'
    df.loc[df['text'].str.contains(phrase3), 'catch_phrase'] = 'We were on a break!'
    df.loc[df['text'].str.contains(phrase4), 'catch_phrase'] = 'Smelly Cat!'
    #Pizza
    df.loc[(df.text.str.contains('pizza')) & (df['character'] == 'Joey'), 'catch_phrase'] = 'Pizza!'
    df.loc[(df['text'].str.lower().str.contains(phrase5)), 'catch_phrase'] = 'OH MY GOD!'

 




