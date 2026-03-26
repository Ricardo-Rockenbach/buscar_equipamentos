import pandas as pd

def carregar_dados():
    df = pd.read_excel('informacoes_computadores.xlsx')
    return df.astype(str)

def buscar_dados(df, buscar):

    colunas = [
        'IP',
        'Sufixo',
        'Setor',
        'Nome da Máquina',
        'Número de Patrimônio',
        'Especificação do processador',
        'Tipo de Memória',
        'Versão do Windows'
    ]

    #busca Exata
    busca_exata = False

    for coluna in colunas:
        busca_exata |= df[coluna].str.lower() == buscar.lower()

    resultado = df[busca_exata]

    # Busca Parcial
    if resultado.empty:
        busca_parcial = False
        for coluna in colunas:
            busca_parcial |= df[coluna].str.lower().str.contains(buscar.lower(), case=False, na=False)
        resultado = df[busca_parcial]
    
    return resultado

df = carregar_dados()

def executar_busca(buscar):   
    return buscar_dados(df, buscar)
    

def main():

    buscar = input("Digite o termo de busca: ").strip()

    resultado = executar_busca(buscar)

    if resultado.empty:
        print("\n❌ Nenhum resultado encontrado\n")
    else:
        print("\n✅ Resultado:\n")
        print(resultado)

if __name__ == "__main__":
 main()