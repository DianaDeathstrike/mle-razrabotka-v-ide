import pandas as pd

#Класс для вывода отчета о датафрейме
class DataFrameReporter:
    #Инициализация класса
    #float_format - формат для чисел с плавающей точкой
    #percent_format - формат для процентов
    #include_all - включать ли все столбцы в отчет
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all
    
    #Вывод отчета о датафрейме
    #df - датафрейм
    #title - заголовок отчета
    def show_report(self, df, title=None):
        if title:
            print(title)
        print('Количество столбцов:', df.shape[1])
        num_rows = df.shape[0]
        print('Количество строк:', num_rows)
        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)
        print('Доля дубликатов:', format(duplicates / num_rows, self.percent_format))
        print(df.describe(include='all' if self.include_all else None))
        print('Количество пропусков:', df.isna().sum(axis=None))
        print('Доля пропусков:', format(df.isna().mean(axis=None), self.float_format))