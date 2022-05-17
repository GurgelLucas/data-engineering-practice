import requests
import os
from zipfile import ZipFile

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # your code here
    try:
        os.mkdir('./downloads')
        print("Diretório 'downloads' foi criado")
    except OSError:
        print("Diretório já existente")
        
    for i in download_uris:
        # Captura o nome dos arquivos
        file_name = [name for name in i.split("/")]
        
        try:
            # Realiza a requisição
            res = requests.get(i)
            if (res.status_code == 200):
                # Etapa de Salvar o arquivo no diretorio criado anteriormente
                with open(f'./downloads/{file_name[-1]}', 'wb') as file:
                    file.write(res.content) 

                # Etapa de extrair os arquivos Zip que foram salvos
                with ZipFile(f'./downloads/{file_name[-1]}', 'r') as fileZip:
                    fileZip.extractall("downloads")

                # Etapa de remover os arquivos zip 
                os.remove(f'./downloads/{file_name[-1]}')
        
        # Caso ocorra uma excessão na requisição.
        except requests.RequestException:
            print("Erro no download do arquivo")

if __name__ == '__main__':
    main()
