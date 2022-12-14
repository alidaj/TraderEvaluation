from pandas import read_csv , DataFrame , Timestamp
from os import listdir

# TODO: Complete the notes

class Preparation:

    def __init__(self,folder_path:str)-> None:

        self.__folder_path = folder_path
        self.__csvfile_list = self.__read_folder(self.__folder_path)
                    

    @property
    def Get(self)-> DataFrame:

        return self.__read_csv(
            self.__folder_path +'/'+ self.__csvfile_list.pop()
        )


    @staticmethod
    def __read_folder(path_folder:str)-> list:

        csvfile_names = []
        for asset in listdir(path_folder):
            if asset.find('csv') != -1 : csvfile_names.append(asset)
        if len(csvfile_names) == 0 :
            raise TypeError (
                'this class defined for find and read csv file in floder path '
            )
        return csvfile_names
        
    @staticmethod
    def __read_csv(csv_name:str)-> DataFrame:


        data_dict , data = {} , read_csv(csv_name)
        if data.shape[1] != 1 :
            raise TypeError(
                'this class defined for read csv whith shape (n,1)'
            )
        for line in data.index:
            data_dict[line] = data.iloc[line,0].split(';') 
        return DataFrame(
            DataFrame(
                data_dict , index=data.columns.values[0].split(';')
            ).transpose().sort_index(ascending=False).values,
            columns = data.columns.values[0].split(';')
        ).applymap(lambda x : float(x.replace(' ','')) if x.replace(' ','').replace('.','').isdigit() else x).applymap(
            lambda x : 0 if (type(x) == str and len(x) == 0) else x
        ).applymap(lambda x : Timestamp(x) if (type(x) == str and ':' in x) else x).applymap(
            lambda x : float(x.replace(' ','')) if (type(x) == str and x.replace(' ','').replace('-','').replace('.','').isdigit()) else x 
        )