def calcular_area(comprimento, largura):
    # Cálculo da área em hectares
    return (comprimento * largura) / 10000  # ha

def calcular_turno_rega(DRA, ET_m, kc):
    # Cálculo do Turno de Rega (TR)
    TR = DRA / (ET_m * kc)
    return TR

def calcular_lamina_liquida_irrigacao(ET_m, TR, kc):
    # Cálculo da Lâmina Líquida de Irrigação (LL)
    LL = ET_m * kc * TR
    return LL

def calcular_lamina_bruta_irrigacao(LL, Ea):
    # Cálculo da Lâmina Bruta de Irrigação (LB)
    LB = LL / (Ea / 100)  # Converte a eficiência para fração
    return LB

def calcular_tempo_irrigacao(LB, qe):
    # Cálculo do Tempo de Irrigação (Ti)
    Ti = LB / (qe * 1000 / 3600)  # Convertendo de m³/h para mm/h
    return Ti

def calcular_numero_posicoes(area, LL):
    # Cálculo do Número de Posições a Serem Irrigadas
    return area * 10000 / LL  # em m²

def calcular_numero_aspersores(area, qe):
    # Cálculo do Número de Aspersores Necessários
    return area * 10000 / (qe * 1000 / 3600)  # em m²

def calcular_vazao_linha_lateral(num_aspersores, qe):
    # Cálculo da Vazão Total da Linha Lateral
    return num_aspersores * qe  # m³/h

def calcular_diametro_comercial(vazao):
    # Cálculo simplificado do diâmetro comercial com base na vazão
    # A fórmula real deve ser baseada nas normas de hidráulica
    # Aqui, apenas um exemplo genérico (ajustar conforme necessário)
    return (4 * vazao / 3.14)**0.5  # mm

def calcular_comprimento_linha_lateral(comprimento):
    # Para simplificação, suponha que o comprimento da linha lateral é igual ao comprimento da parcela
    return comprimento  # m

def calcular_potencia_bomba(vazao, HMT, eficiencia):
    # Cálculo da Potência da Bomba (cv)
    potencia_cv = (vazao * HMT * 1000) / (75 * eficiencia)
    return potencia_cv

def main():
    # Entradas do usuário
    comprimento = float(input("Digite o comprimento da parcela (m): "))
    largura = float(input("Digite a largura da parcela (m): "))
    z = float(input("Digite a profundidade da raiz (cm): "))
    Ucc = float(input("Digite a capacidade de campo do solo (%): "))
    Upmp = float(input("Digite o ponto de murcha permanente (%): "))
    kc_critico = float(input("Digite o coeficiente cultural crítico (Kc): "))
    Ea = float(input("Digite a eficiência do sistema de irrigação (%): "))
    jornada_trabalho = float(input("Digite a jornada de trabalho por dia (horas): "))
    Eto_max = float(input("Digite a evapotranspiração máxima (mm/dia): "))
    ds = float(input("Digite a densidade do solo (g/cm³): "))
    VIB = float(input("Digite a taxa de infiltração do solo (mm/h): "))
    qe = float(input("Digite a taxa de fluxo do aspersor (m³/h): "))
    pressao_servico = float(input("Digite a pressão de serviço (mca): "))
    perda_pressao_permitida = float(input("Digite a perda de pressão máxima permitida (mca): "))
    
    # Cálculos
    area = calcular_area(comprimento, largura)  # Área em hectares
    # Calcular DRA (Depleção de Água Disponível)
    DRA = (Ucc - Upmp) * ds * z * 0.1  # f é considerado como 0.1 para simplificação
    TR = calcular_turno_rega(DRA, Eto_max, kc_critico)  # Turno de Rega
    LL = calcular_lamina_liquida_irrigacao(Eto_max, TR, kc_critico)  # Lâmina Líquida
    LB = calcular_lamina_bruta_irrigacao(LL, Ea)  # Lâmina Bruta
    Ti = calcular_tempo_irrigacao(LB, qe)  # Tempo de Irrigação
    NPT = calcular_numero_posicoes(area, LL)  # Número de Posições
    num_aspersores = calcular_numero_aspersores(area, qe)  # Número de Aspersores

    # Linha Lateral
    vazao_linha_lateral = calcular_vazao_linha_lateral(num_aspersores, qe)
    diametro_linha_lateral = calcular_diametro_comercial(vazao_linha_lateral)
    comprimento_linha_lateral = calcular_comprimento_linha_lateral(comprimento)

    # Linha Principal
    # Supondo que a linha principal tem as mesmas características da linha lateral para simplificação
    vazao_linha_principal = vazao_linha_lateral
    diametro_linha_principal = diametro_linha_lateral
    comprimento_linha_principal = comprimento

    # Cálculo da Potência da Motobomba
    potencia_cv = calcular_potencia_bomba(vazao_linha_principal, pressao_servico, 0.7)  # 0.7 é a eficiência padrão

    # Saídas
    print("\n--- Resumo do Sistema de Irrigação ---")
    print(f"Área da Parcela: {area:.2f} ha")
    print(f"Tempo de Irrigação (Ti): {Ti:.2f} horas")
    print(f"Número de Posições a Serem Irrigadas: {NPT:.2f}")
    print(f"Número de Aspersores Necessários: {num_aspersores:.2f}")
    
    print("\n--- Linha Lateral ---")
    print(f"Vazão: {vazao_linha_lateral:.2f} m³/h")
    print(f"Diâmetro Comercial: {diametro_linha_lateral:.2f} mm")
    print(f"Comprimento: {comprimento_linha_lateral:.2f} m")

    print("\n--- Linha Principal ---")
    print(f"Vazão: {vazao_linha_principal:.2f} m³/h")
    print(f"Diâmetro Comercial: {diametro_linha_principal:.2f} mm")
    print(f"Comprimento: {comprimento_linha_principal:.2f} m")

    print("\n--- Dimensionamento da Motobomba ---")
    print(f"Potência da Motobomba: {potencia_cv:.2f} cv")

if __name__ == "__main__":
    main()
