#Function to retreive files from folder and output all file names accordingly
def raw_name(i):
    return 'transcripts/merged' + str(i) + '.csv'


#Function to rename header to text
def rename_col(df):
    df.rename(columns=({df.columns[0]: 'text'}), inplace=True)


#Function to create a NaN column to fill with location of scene
def scene_col(df):
    import numpy as np
    df['scene'] = np.nan
    df['scene'] = df[(df.text).str.startswith('[Scene:')]


#Function to fill each cell with the value of the preceeding cell
def scene_fill(df):
    df['scene'] = df['scene'].ffill(axis = 0)


#Function to split the scene column to isolate location
def location(df):
    new_col = df['scene'].str.split("," , expand = True)
    df['location'] = new_col[0].str.replace('\[Scene:', '').replace('\[ ', '').replace(';', '.').replace("'", '').replace("’", '').replace('\] ', '')
    df['location'] = df['location'].str.split('.').str[0]
    df['location'] = df['location'].str.split(';').str[0]
    df['location'] = df['location'].str.lower()
    df['location'] = df['location'].str.replace("'", '').replace("’", '').replace("´", '').replace("’", '').replace("’", '').replace("� ", '')
    df['location'] = df['location'].str.strip()


#Function to delete scene column
def drop_scene(df):
    df.drop(columns='scene', inplace = True)


#Function to create a character column
def character(df):
    character_list = ['Monica', 'Rachel', 'Phoebe', 'Ross', 'Chandler', 'Joey', 'MONICA', 'RACHEL', 'PHOEBE', 'ROSS', 'CHANDLER', 'JOEY']
    df['character'] = df['text'].str.split(':').str[0]
    df.loc[(~df.character.isin(character_list),'character')] = 'Other'
    df['character'] = df.character.str.capitalize()
 
  
#Function to finalise dataframe
def final_df(df):
    df = df[df.character != 'Other'].reset_index()
    df.drop('index', axis=1, inplace = True)
    return df
    
#Function to combine all dataframes in one
def concat_df(seasons_list):
    df1 = seasons_list[0]
    for df in seasons_list[1:]:
        df1 = df1.append(df)
        df1.drop_duplicates(inplace=True)
        df1 = df1.dropna()
    df1.reset_index()
    return df1

#Function to count words per line
def word_count(df):
    df['word_count'] = df['text'].str.count(' ')






