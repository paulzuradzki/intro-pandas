import os
import zipfile

import requests
import pandas as pd
import seaborn as sns

def prep_example_data():
    '''Generates sample data from seaborn'''
    if not os.path.exists('data'):
        os.mkdir('data')

    print('Getting CSV files from seaborn in ./data/ directory')

    for dataset in sns.get_dataset_names():
        file_path = './data/{}.csv'.format(dataset)
        print(file_path)
        df = sns.load_dataset(dataset)
        df.to_csv(file_path, index=False)


def download_zip(url=None, zip_name=None):
    '''Downloads zipfile using requests module.'''

    print(f'Downloading...\n{url}')
    response = requests.get(url, stream=True)

    with open(zip_name, "wb") as handle:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)

def process_url_zip(url=None, zip_name=None, target_path=None):
    '''Downloads zip, extracts contents, and deletes zip.'''

    download_zip(url, zip_name)

    # extract contents from .zip file to ./data
    print('Extracting...')
    with zipfile.ZipFile(zip_name) as zip_obj:
        zip_obj.extractall(target_path)
        zip_contents = zip_obj.namelist()[0]

    print(f'Contents {zip_contents} \nextracted at: {target_path}.\nRemoving {zip_name}.')
    os.remove(zip_name)

    # if not CSV, re-name to CSV
    if not zip_contents.endswith('.csv'):
        os.rename(os.path.join(target_path, zip_contents), os.path.join(target_path, f'{zip_contents}.csv'))

if __name__ == '__main__':
    prep_example_data()

    url = 'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip'
    target_path = './data/divvy2019q4.zip'
    download_zip(url, target_path)
