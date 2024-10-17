# Dicionário contendo profundidade da raiz, f e valores de kc para cada cultura
crops = {
    "soja": {"profundidade_da_raiz": 1.25, "f": 0.35, "kc": 1.10},
    "milho": {"profundidade_da_raiz": 1.75, "f": 0.40, "kc": 1.15},
    "arroz": {"profundidade_da_raiz": 0.75, "f": 0.30, "kc": 1.15},
    "feijão": {"profundidade_da_raiz": 0.90, "f": 0.35, "kc": 1.00},
    "trigo": {"profundidade_da_raiz": 1.25, "f": 0.35, "kc": 0.95},
    "tomate": {"profundidade_da_raiz": 0.75, "f": 0.35, "kc": 1.00},
    "alface": {"profundidade_da_raiz": 0.30, "f": 0.25, "kc": 0.85},
    "cenoura": {"profundidade_da_raiz": 0.40, "f": 0.30, "kc": 0.90},
    "batata": {"profundidade_da_raiz": 0.50, "f": 0.30, "kc": 0.90},
    "cebola": {"profundidade_da_raiz": 0.40, "f": 0.30, "kc": 0.85}
}

# Listas de culturas
grains = ["milho", "soja", "feijão", "arroz"]
vegetables = ["tomate", "alface", "cenoura", "batata", "cebola"]

# Tipos de aspersores com suas especificações
aspersores = {
    "grãos": {
        "tipo": "Longo Vermelho",
        "raio_aspersor": 15.2,
        "pressao_servico": 25,
        "qe": 2.88,
        "espaçamento": "18x18",
        "intensidade": 20.00,
        "perda_pressao_permitida": 5
    },
    "vegetais": {
        "tipo": "Long Green",
        "raio_aspersor": 14.6,
        "pressao_servico": 25,
        "qe": 2.17,
        "espaçamento": "12x18",
        "intensidade": 10.00,
        "perda_pressao_permitida": 5
    }
}

# Função para escolher um tipo de cultura do usuário
def choose_crop():
    crop_type = input("Escolha um tipo (grãos ou vegetais): ").lower()
    
    # Validar tipo de cultura
    if crop_type not in ["grãos", "vegetais"]:
        print("Tipo não reconhecido. Por favor, tente novamente.")
        return None, None
    
    # Selecionar culturas disponíveis com base no tipo
    available_crops = grains if crop_type == "grãos" else vegetables
    print("Culturas disponíveis: ", ", ".join(available_crops))
    crop = input("Escolha uma cultura: ").lower()
    
    # Validar cultura escolhida
    if crop in available_crops:
        print(f"Você escolheu: {crop}")
        return crop, crop_type
    else:
        print("Cultura não encontrada.")
        return None, None

# Função para obter informações sobre a cultura selecionada
def get_crop_info(crop):
    info = crops.get(crop)
    if info:
        return {
            "Cultura": crop.capitalize(),
            "Profundidade da Raiz (m)": info.get("profundidade_da_raiz", 0),  # Default to 0 if key is missing
            "f": info.get("f", 0),  # Default value
            "kc": info.get("kc", 0)  # Default value
        }
    else:
        return {"Mensagem": "Cultura não encontrada."}


# Função principal para executar o programa
def var_padrao():
    crop, crop_type = choose_crop()
    if crop is None:
        return  # Sair se nenhuma cultura válida foi escolhida
    
    # Obter e imprimir informações sobre a cultura selecionada
    info = get_crop_info(crop)
    print("Informações sobre a cultura:", info)

    # Obter e imprimir informações sobre o melhor aspersor
    aspersor = aspersores[crop_type]
    return info["profundidade_da_raiz"], info["f"], info["kc"], aspersor["tipo"], aspersor["qe"], aspersor["raio_aspersor"], aspersor["pressao_servico"], aspersor["perda_pressao_permitida"], aspersor["espaçamento"]

def main():
    # Entradas do usuário
    comprimento = float(input("Digite o comprimento da parcela (m): "))
    largura = float(input("Digite a largura da parcela (m): "))
    Ucc = float(input("Digite a capacidade de campo do solo (%): "))
    Upmp = float(input("Digite o ponto de murcha permanente (%): "))
    Ea = float(input("Digite a eficiência do sistema de irrigação (%): "))
    jornada_trabalho = float(input("Digite a jornada de trabalho por dia (horas): "))
    Eto_max = float(input("Digite a evapotranspiração máxima (mm/dia): "))
    ds = float(input("Digite a densidade do solo (g/cm³): "))
    VIB = float(input("Digite a taxa de infiltração do solo (mm/h): "))

    profundidade_da_raiz, f, kc, tipo, qe, raio_aspersor, pressao_servico, perda_pressao_permitida, espacamento = var_padrao()
    if z is None:
        return  # Sair se não foi possível obter os valores padrão

    # Cálculos (exemplos)
    area = (comprimento * largura) / 10000  # Área em hectares
    print(f"Área da Parcela: {area:.2f} ha")
    # Outros cálculos podem ser adicionados aqui, como lâmina líquida e bruta, número de aspersores, etc.

if __name__ == "__main__":
    main()
