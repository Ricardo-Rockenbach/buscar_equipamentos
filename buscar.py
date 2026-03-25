import pandas as pd

def carregar_dados():
    df = pd.read_excel('informacoes_computadores.xlsx')
    return df.astype(str)

def buscar_dados(df, buscar):
    #busca Exata
    resultado = df[df
        (df['IP'] == buscar) |
        (df['Setor'] == buscar) |
        (df['Nome da Máquina'] == buscar) |
        (df['Número de Patrimônio'] == buscar) |
        (df['Especificação do processador'] == buscar) |
        (df['Tipo de Memória'] == buscar) |
        (df['Versão do Windows'] == buscar)
    ]
    
    # Busca Parcial
    if resultado.empty:
        resultado = df[
            df['IP'].str.contains(buscar, case=False) |
            df['Setor'].str.contains(buscar, case=False) |
            df['Nome da Máquina'].str.contains(buscar, case=False) |
            df['Número de Patrimônio'].str.contains(buscar, case=False) |
            df['Especificação do processador'].str.contains(buscar, case=False) |
            df['Tipo de Memória'].str.contains(buscar, case=False) |
            df['Versão do Windows'].str.contains(buscar, case=False)
        ]   
    return resultado

def main():
    df = carregar_dados()
    buscar = input("Digite o termo de busca: ")
    resultado = buscar_dados(df, buscar)
    
    if resultado.empty:
        print("\n❌ Nenhum resultado encontrado\n")
    else:
        print("\n✅ Resultado:\n")
        print(resultado)

if __name__ == "__main__":
 main()