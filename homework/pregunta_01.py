"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    df=pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';', index_col='Unnamed: 0')

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df[['dia','mes','año']]=df['fecha_de_beneficio'].str.split('/',expand=True)
    mascara=df['año'].str.len()<4
    df.loc[mascara,['dia','año']]=df.loc[mascara,['año','dia']].values
    df['fecha_de_beneficio']=df['año']+'/'+df['mes']+'/'+df['dia']
    
    df['sexo'] = df['sexo'].str.lower().str.strip()
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower().str.strip()
    df['idea_negocio']=df['idea_negocio'].str.lower().str.replace('[-_]', ' ', regex=True).str.strip()
    df['línea_credito']=df['línea_credito'].str.lower().str.replace('[-_]', ' ', regex=True).str.strip()
    df['barrio'] = df['barrio'].str.lower().str.replace('[-_]', ' ', regex=True)

    df['monto_del_credito'] = df['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip()
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce').fillna(0).astype(int)

    df.drop_duplicates(inplace=True)

    if not os.path.exists('files/output'):
        os.mkdir('files/output')
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';')

    return

pregunta_01()
