#!/usr/bin/env python
# coding: utf-8

# ## Import libraries

# In[2]:


import pandas as pd
from os import listdir


# ## Demographic information

# In[31]:


def get_demographic_info(filename: str = None):
    """Get the demographic info of the text file.

    Args:
        filename (str, optional): The path of the demographic_info file. Defaults to None.

    Returns:
        df_demographic(pd.DataFrame): Contains demographic info about patients.
    """
    if not filename:
        filename = 'app/processing/data/Respiratory_Sound_Database/demographic_info.txt'

    column_names = [
        'Patient_number',
        'Age',
        'Sex',
        'Adult_BMI',
        'Child_Weight',
        'Child_Height'
    ]

    with open(filename) as f:
        df_demographic = pd.read_csv(f, delimiter=' ', names=column_names) # , index_col='Patient_number')
    
    df_demographic['email'] = 'p_' + df_demographic['Patient_number'].astype(str) + '@testmail.com'
    df_demographic['first_name'] = df_demographic['Patient_number'].astype(str)
    df_demographic['last_name'] = df_demographic['Patient_number'].astype(str)
    df_demographic['legal_id'] = (df_demographic['Patient_number'] + 1000 * df_demographic['Patient_number']).astype(int)
    df_demographic['password'] = 'patient_123'
    df_demographic = df_demographic.fillna(0)

    return df_demographic


# ### df_demographic DataFrame

# In[32]:


filename_demographic = 'app/processing/data/Respiratory_Sound_Database/demographic_info.txt'
df_demographic = get_demographic_info(filename_demographic)
# df_demographic.to_csv('app/processing/data/patients_table.csv')
# print(df_demographic.dtypes)
# df_demographic.head()


# ## Annotation details

# In[4]:


def get_annotations_details(path: str = None):
    """Get the annotation details for each audiofile.

    Args:
        path (str, optional): Path of audiofile's annotations. Defaults to None.

    Returns:
        df_annotation_info(pd.DataFrame) : Contains annotation details for each recording.
    """
    if not path:
        path = 'app/processing/data/Respiratory_Sound_Database/audio_and_txt_files'

    annotation_filenames = [
        f[:-4].split('_') + [f[:-4]]
        for f in listdir(path)
        if '.txt' in f
    ]

    column_names = [
        'Patient_number',
        'Recording_index',
        'Chest_location',
        'Acquisition_mode',
        'Recording_equipment',
        'Audiofile_name'
    ]

    df_annotation_info = pd.DataFrame(
        annotation_filenames,
        columns=column_names,
    )
    df_annotation_info['Patient_number'] = df_annotation_info['Patient_number'].astype('int')
    # df_annotation_info = df_annotation_info.set_index('Patient_number')

    return df_annotation_info


# ### df_annotation_info DataFrame

# In[5]:


path_audios = 'app/processing/data/Respiratory_Sound_Database/audio_and_txt_files'

df_annotation_info = get_annotations_details(path_audios)
df_annotation_info['Recording_equipment'] = df_annotation_info['Recording_equipment'].astype('category')
# print(df_annotation_info.dtypes)
# df_annotation_info


# ## Annotation data

# In[6]:


def get_annotation_data(df_files: pd.DataFrame = None):
    """Get the annotation data for each audiofile annotation.

    Args:
        df_files (pd.DataFrame, optional):  Data frame who has 'Patient_number', 
                                            'Recording_index', 'Audiofile_name'
                                            columns from df_annotation_info. 
                                            Defaults to None.

    Returns:
        df_annotation_data(pd.DataFrame):   Contains annotation data for each 
                                            audiofile annotation
    """
    if not df_files:
        path_audios = 'app/processing/data/Respiratory_Sound_Database/audio_and_txt_files'
        df_annotation_info = get_annotations_details(path_audios)
        df_files = df_annotation_info.copy()[[
            'Patient_number',
            'Recording_index',
            'Chest_location',
            'Audiofile_name'
        ]]
        df_files['Audiofile_path'] = path_audios + '/' + df_files['Audiofile_name'] + '.wav'
        df_files['Audiofile_path_txt'] = path_audios + '/' + df_files['Audiofile_name'] + '.txt'
        df_files
        
    column_names = [
        'Begin_cycle',
        'End_cycle',
        'Crackles',
        'Wheezes',
    ]
    
    df_each_file = []

    for patient, record, chest, file in df_files[
        ['Patient_number', 'Recording_index', 'Chest_location', 'Audiofile_path_txt']
    ].values:

        df_each_file.append(pd.read_csv(file, delimiter='\t', names=column_names))
        df_each_file[-1]['Patient_number'] = patient
        df_each_file[-1]['Recording_index'] = record
        df_each_file[-1]['Chest_location'] = chest
        
    df_annotation_data = pd.concat(df_each_file, ignore_index=True)
    # df_annotation_data = df_annotation_data.set_index('Patient_number')

    return df_annotation_data


# ### df_files Dataframe

# In[7]:


# df_files = df_annotation_info.copy()[[
#     'Patient_number',
#     'Recording_index',
#     'Chest_location',
#     'Audiofile_name',
#     'Recording_equipment',
#     'Acquisition_mode',
#     ]]
# df_files['Audiofile_name'] = path_audios + '/' + df_files['Audiofile_name'] + '.txt'
# df_files
df_files = df_annotation_info.copy()[[
            'Patient_number',
            'Recording_index',
            'Chest_location',
            'Audiofile_name',
            'Recording_equipment',
            'Acquisition_mode',
        ]]
df_files['Audiofile_path'] = path_audios + '/' + df_files['Audiofile_name'] + '.wav'
df_files['Audiofile_path_txt'] = path_audios + '/' + df_files['Audiofile_name'] + '.txt'
        # df_files


# ### df_annotation_data Dataframe

# In[8]:


df_annotation_data = get_annotation_data()
# df_annotation_data


# ## Merging dataframes

# ### df_annotation Dataframe

# In[9]:


df_annotation = pd.merge(
    df_annotation_data,
    df_annotation_info,
    on=[
        'Patient_number',
        'Recording_index',
        'Chest_location'
    ]
)

# df_annotation


# ### df_patients Dataframe

# In[10]:


df_patients = pd.merge(df_demographic, df_annotation, on=['Patient_number'])
# df_patients


# ## Export general file

# In[11]:


# df_patients.to_csv('app/processing/data/general_table.csv')

df_excel = pd.read_excel('app/processing/data/base_ds4a_4ntables.xlsx',sheet_name='base_ds4a_4')
df_excel = df_excel[
    [
        'Begin_cycle',
        'End_cycle',
        'B',
        'Patient_number',
        'Chest_location',
        'Acquisition_mode',
        'Numestdo',
        'Status',
        'Variance',
        'Range',
        'SMA_coarse',
        'Spectre_AVG',
        'SMA_fine',
        'Age',
        'Sex',
        'Diagnosis',
        'Child_Height',
        'Child_Weight',
        'Child_Height',
    ]
]

df_total = pd.merge(
    df_patients,
    df_excel,
    on=[
        'Patient_number',
        'Chest_location',
        'Acquisition_mode',
        'Age', 
        'Sex',
        'Begin_cycle',
        'End_cycle',
    ],
)

# df_excel


