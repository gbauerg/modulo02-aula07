import pandas as pd
import numpy as np

# obtendo os dados
try:
    print("Obtendo os dados...")

    ENDEREÇO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

    #utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=";", encoding="cp1252")
    #print(df_ocorrencias)

    #Delimitando os dados
    df_roubo_veiculos = df_ocorrencias[["munic", "roubo_veiculo"]]
    #print(df_roubo_veiculos.head(30))
    #print(df_roubo_veiculos.tail(30))
    
    #totalizando os roubos por cidade (Variável qualitativa "munic" e Variavel quantitatival "roubo_veiculo")
    df_roubo_veiculos = df_roubo_veiculos.groupby("munic", as_index=False)["roubo_veiculo"].sum()

    #Ordenando os dados
    df_roubo_veiculos = df_roubo_veiculos.sort_values(
        by="roubo_veiculo", ascending=False
    )


    print(df_roubo_veiculos.tail(10))

except Exception as e:
    print(f"Erro ao obter os dados: {e}")

try:
    print(f"\nObtendo informações a cerca de roubos dos veículos...")
    array_roubo_veiculo = np.array(df_roubo_veiculos['roubo_veiculo'])

    print(f"\nMedidas de Tendência Central")
    
    media_roubo = np.mean(array_roubo_veiculo)
    print(f"Média: {media_roubo}")

    mediana_roubo = np.median(array_roubo_veiculo)
    print(f"Mediana: {mediana_roubo}")

    distancia = abs(
        (media_roubo - mediana_roubo) / mediana_roubo * 100
        )
    print(f"Distância: {distancia:.2f}%")


except Exception as i:
    print(f"Obtendo medidas - {i}")

try:

    q1 = np.quantile(array_roubo_veiculo, .25)
    q2 = np.quantile(array_roubo_veiculo, .50)
    q3 = np.quantile(array_roubo_veiculo, .75)

    print(f"\nMedidas de Posição")
    print(f"Q1: {q1}")
    print(f"Q2: {q2}")
    print(f"Q3: {q3}")

    df_roubo_veiculos_menores = df_roubo_veiculos[
        df_roubo_veiculos["roubo_veiculo"] < q1
    ]

    df_roubo_veiculos_maiores = df_roubo_veiculos[
        df_roubo_veiculos["roubo_veiculo"] > q3
    ]

    print(f"\nMunicipios com os Menores Roubos:")
    print(30*"=")
    print(df_roubo_veiculos_menores.sort_values(by="roubo_veiculo", ascending=True))
    df_roubo_veiculos_menores.to_csv("menores.csv", index=False, sep=";", encoding="cp1252")


    print(f"\nMunicipios com os Maiores Roubos:")
    print(30*"=")
    print(df_roubo_veiculos_maiores.sort_values(by="roubo_veiculo", ascending=False))
    df_roubo_veiculos_menores.to_csv("maiores.csv", index=False, sep=";", encoding="cp1252")

except Exception as j:
    print(f"Erro ao calcular os quartis {j}")