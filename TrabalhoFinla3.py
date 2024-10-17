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
        "tipo": "Long Red",
        "diâmetro": "6.20 x 4.60 mm",
        "pressão": 25,
        "taxa_de_fluxo": 2.88,
        "espaçamento": "18x18",
        "intensidade": 20.06
    },
    "vegetais": {
        "tipo": "Long Green",
        "diâmetro": "5.00 x 4.60 mm",
        "pressão": 25,
        "taxa_de_fluxo": 2.17,
        "espaçamento": "12x18",
        "intensidade": 10.05
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
            "Profundidade da Raiz (m)": info["profundidade_da_raiz"],
            "f": info["f"],
            "kc": info["kc"]
        }
    else:
        return {"Mensagem": "Cultura não encontrada."}

# Função principal para executar o programa
def main():
    crop, crop_type = choose_crop()
    if crop is None:
        return  # Sair se nenhuma cultura válida foi escolhida
    
    # Obter e imprimir informações sobre a cultura selecionada
    info = get_crop_info(crop)
    print(info)
    
    # Obter e imprimir informações sobre o melhor aspersor
    aspersor = aspersores[crop_type]
    print(f"Informações do aspersor escolhido: {aspersor}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
