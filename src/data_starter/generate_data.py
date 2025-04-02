import random
import os 
import pandas as pd
from faker import Faker


def create_dataframe():
    """
    Generate data for testing.

    type: df: pd.DataFrame
    """
    
    faker = Faker("pt_BR")

    departments = [
        "Recursos Humanos",
        "Financeiro",
        "Marketing",
        "TI",
        "Vendas",
        "Operações",
        "Jurídico",
        "Engenharia",
        "Atendimento ao Cliente",
        "P&D",
    ]
    reasons = [
        "Doença",
        "Problemas pessoais",
        "Consulta médica",
        "Viagem de negócios",
        "Outros",
    ]

    data = {
        "Colaborador_id": [faker.unique.random_number(digits=5) for _ in range(10)],
        "Colaborador_nome": [faker.name() for _ in range(10)],
        "Departamento": [faker.random_element(elements=departments) for _ in range(10)],
        "Motivo_da_ausência": [
            faker.random_element(elements=reasons) for _ in range(10)
        ],
        "Horas_de_ausência": [faker.random_int(min=1, max=8) for _ in range(10)],
        "Data_da_ausência": [
            faker.date_between_dates(
                date_start=pd.to_datetime("2023-06-01"),
                date_end=pd.to_datetime("2023-06-30"),
            )
            for _ in range(10)
        ],
        "Salário": [round(random.uniform(2500, 12500), 2) for _ in range(10)],
    }

    df = pd.DataFrame(data)
    df["Data_da_ausência"] = pd.to_datetime(df["Data_da_ausência"])

    return df

def generate_data(number:int, path:str) -> bool:

    aux_path = "absenteeism_data_"
    aux_extension = ".xlsx"
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(number):
        df = create_dataframe()
        file_name = f'{aux_path}{i}{aux_extension}'
        


