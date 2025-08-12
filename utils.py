import pandas as pd


def resumen_tipos(df, TOP_VALUES=5):
    '''
    Genera un resumen de los tipos de datos y valores únicos en un DataFrame.
    
    Parámetros:
        df (pd.DataFrame): DataFrame a analizar.
        TOP_VALUES (int): Cantidad de valores más frecuentes a mostrar por columna.
    
    Retorna:
        pd.DataFrame: Resumen con tipo, nulos, vacíos, únicos y valores más comunes.
    '''
    if df.empty:
        return pd.DataFrame()
    resumen =  []
    # Recorrer las columnas del dataframe y obtener su tipos de datos, nulos, vacíos y únicos y los valores mas comunes
    for col in df.columns:
        type = df[col].dtype
        null_values = df[col].isnull().sum()
        empty_values = df[col].astype(str).str.strip().eq("").sum()
        
        unique_values = df[col].nunique()
        top_values = df[col].value_counts().head(TOP_VALUES)
        top_values_str = ', '.join([f"{val}" for val, count in top_values.items()])
        
        resumen.append({
            'Column': col,
            'Tipo': type,
            'Nulos': null_values,
            'Vacíos': empty_values,
            'Únicos': unique_values,
            f'Top {TOP_VALUES} Values': top_values_str
        })
    return pd.DataFrame(resumen)