#Function to narrow down locations
def amend_location(df):
    
    hallway_list = ['the hallway of monicas building','the hallway',
    'hallway between the apartments',
    'hallway outside chandler and joeys apartment',
    'later on in the hallway between the apartments',
    'the hallway after the party',
    'hallway',
    'the hallway between the two apartments',
    'the hallway between the apartments',
    'the hallway and stairs outside chandler and monicas apartment',
    'the hallway]']

    ross_apartment = ['rosss apartment',
    'ross apartment',
    'ross',
    'rosss bedroom',
    'ross’s bedroom',
    'ross’s kitchen',
    'ross’s',
    'ross’s apartment',
    'rosss now empty apartment',
    'rosss new apartment',
    'rosss buildings lobby', 'the lobby of rosss building',
    'rosss building', 'the lobby in rosss building',
    'looking through rosss window', 'ross and rachels room',
    'ross and rachel’s apartment',
    'ross and carols',
    'ross’s building', 
    'ross and…rachel’s…i guess i have to call it that now',
    'ross and rachel’s',
    'ross and rachels',
    'outside ross and rachels',
    'ross and rachels apartment]',
    'ross and rachel�s',
    'outside ross and rachel�s',
    'ross and rachels apartment',
    'ross and rachels kitchen',
    'rosss place',
    'ross]',
    'ross�]',
    'rosss apartment: ross is doing something on his laptop when chandler walks in]',
    'ross apartment]',
    'rosss room',
    'rosss apartment the next morning']

    chandler_joey_apartment = ['chandler and joeys',
    'chandler and joeys chandler is talking with his mom',
    'chandlers bedroom',
    'joeys bedroom',
    'joeys apartment',
    'at chandler and joeys',
    'back in chandler and joeys apartment',
    'chandler and joeys apartment',
    'chandler',
    'chandler and eddies apartment',
    'chandler and joeys]',
    'chandler and joey’s',
    'chandler’s',
    'chandler’s bedroom',
    'chandler and joey’s bathroom: chandler is watching the duck swim in the bathtub',
    'chandler and joeys erm',
    'joey’s bedroom',
    'chandler and joeys bathroom',
    'joeys room',
    'joeys apartment]',
    'chandler arrives home from work',
    'joey and rachels apartment]',
    'joeys room: joey is sitting on his bed reading dool transcript when rachel walks in]',
    'joey and charlies room]',
    'rachel and joeys apartment',
    'joey and rachels]',
    'rachel and joeys',
    'chandler walks into joeys apartment]',
    'joeys place',
    'joey and janines', 
    'joey and janine’s',
    'joey and janine’s apartment', 
    'joey’s apartment',
    'joey and now rachels apartment', 
    'joey and rachels apartment',
    'joey and rachels',
    'joey and rachel’s',
    'joey’s']

    monica_apartment = ['monicas apartment',
    'monica and rachels',
    'monica and rachels apartment',
    'monicas bedroom',
    'monica and rachels balcony',
    'monica and rachel’s',
    'at monica and rachels',
    'rachel and monicas apartment',
    'monica',
    'in a tv commercial that the gang is watching at monica and rachels',
    'back at monica and rachels apartment',
    'monica and chandlers apartment',
    'outside monica and rachels apartment',
    'monicas party',
    'rachel and monicas',
    'monica and rachels: everyone is there and they are watching an info-mercial that stars joey',
    'monica and rachel’s bathroom',
    'monica and phoebe’s',
    'monica’s',
    'monica’s bedroom',
    'monica and rachel',
    'monica and rachels erm',
    'the girls apartment',
    'monica and phoebes',
    'monica and chandler’s new apartment',
    'monica and chandler’s',
    'chandler’s and monica’s apartment',
    'monica and chandlers',
    'monica and chandler’s apartment',
    'monica and chandler’s bedroom',
    'monica and chandlers kitchen', 
    'monica and chandlers bedroom',
    'monica and joey’s',
    'monica and chandler’s bathroom',
    'chandler and monica’s',
    'chandler and monica’s bathroom',
    'chandler and monicas apartment]',
    'chandler arrives home and monicas got a video of sharks ready for chandler',
    '� monica and chandlers apartment',
    'chandler and monicas]', 
    'monica and chandlers]',
    'monica and chandlers aparment',
    'chandler and monicas apartment',
    'monica and chandlers apartment]',
    'monica and chandlers apartement',
    'monicas apartment]',
    'chandler and monicas apartement',
    'monica and chandlers room',
    'chandler and monicas room',
    'chandler and monicas'
    'monica’s apartment', 
    'monica and chandlers hotel room',
    'monicas living room',
    'monicas apartment continued']


    hallway = '|'.join(hallway_list)
    ross = '|'.join(ross_apartment)
    chandler_joey = '|'.join(chandler_joey_apartment)
    monica = '|'.join(monica_apartment)
    
    df.loc[df['location'].str.contains('perk'), 'location'] = 'Central Perk'
    df.loc[df['location'].str.contains(hallway), 'location'] = 'The Hallway'
    df.loc[df['location'].str.contains(ross), 'location'] = "Ross's Apartment"
    df.loc[df['location'].str.contains(chandler_joey), 'location'] = "Chandler and Joey's"
    df.loc[df['location'].str.contains(monica), 'location'] = "Monica's Apartment"

    #Narrow down locations
    location_list = ['Central Perk', 'The Hallway', "Ross's Apartment", "Chandler and Joey's", "Monica's Apartment"]
    df.loc[(~df.location.isin(location_list),'location')] = 'Other'
 




