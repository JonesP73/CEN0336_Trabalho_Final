import tkinter as tk
from tkinter import messagebox

def calcular_area(comprimento, largura):
    return (comprimento * largura) / 10000  # ha

def calcular_turno_rega(DRA, ET_m, kc):
    TR = DRA / (ET_m * kc)
    return TR

def calcular_lamina_liquida_irrigacao(ET_m, TR, kc):
    LL = ET_m * kc * TR
    return LL

def calcular_lamina_bruta_irrigacao(LL, Ea):
    LB = LL / (Ea / 100)  # Converte a eficiência para fração
    return LB

def calcular_tempo_irrigacao(LB, qe):
    Ti = LB / (qe * 1000 / 3600)  # Convertendo de m³/h para mm/h
    return Ti

def calcular_numero_posicoes(area, LL):
    return area * 10000 / LL  # em m²

def calcular_numero_aspersores(area, qe):
    return area * 10000 / (qe * 1000 / 3600)  # em m²

def calcular_vazao_linha_lateral(num_aspersores, qe):
    return num_aspersores * qe  # m³/h

def calcular_diametro_comercial(vazao):
    return (4 * vazao / 3.14)**0.5  # mm

def calcular_comprimento_linha_lateral(comprimento):
    return comprimento  # m

def calcular_potencia_bomba(vazao, HMT, eficiencia):
    potencia_cv = (vazao * HMT * 1000) / (75 * eficiencia)
    return potencia_cv

def calcular_irrigacao():
    try:
        comprimento = float(entry_comprimento.get())
        largura = float(entry_largura.get())
        z = float(entry_profundidade.get())
        Ucc = float(entry_capacidade.get())
        Upmp = float(entry_ponto.get())
        kc_critico = float(entry_kc.get())
        Ea = float(entry_eficiencia.get())
        jornada_trabalho = float(entry_jornada.get())
        Eto_max = float(entry_evapotranspiracao.get())
        ds = float(entry_densidade.get())
        VIB = float(entry_infiltracao.get())
        qe = float(entry_fluxo.get())
        pressao_servico = float(entry_pressao.get())
        perda_pressao_permitida = float(entry_perda.get())
        
        area = calcular_area(comprimento, largura)  # Área em hectares
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
        vazao_linha_principal = vazao_linha_lateral
        diametro_linha_principal = diametro_linha_lateral
        comprimento_linha_principal = comprimento

        # Cálculo da Potência da Motobomba
        potencia_cv = calcular_potencia_bomba(vazao_linha_principal, pressao_servico, 0.7)  # 0.7 é a eficiência padrão

        # Exibir resultados
        result_text = (
            f"\n--- Resumo do Sistema de Irrigação ---"
            f"\nÁrea da Parcela: {area:.2f} ha"
            f"\nTempo de Irrigação (Ti): {Ti:.2f} horas"
            f"\nNúmero de Posições a Serem Irrigadas: {NPT:.2f}"
            f"\nNúmero de Aspersores Necessários: {num_aspersores:.2f}"
            f"\n\n--- Linha Lateral ---"
            f"\nVazão: {vazao_linha_lateral:.2f} m³/h"
            f"\nDiâmetro Comercial: {diametro_linha_lateral:.2f} mm"
            f"\nComprimento: {comprimento_linha_lateral:.2f} m"
            f"\n\n--- Linha Principal ---"
            f"\nVazão: {vazao_linha_principal:.2f} m³/h"
            f"\nDiâmetro Comercial: {diametro_linha_principal:.2f} mm"
            f"\nComprimento: {comprimento_linha_principal:.2f} m"
            f"\n\n--- Dimensionamento da Motobomba ---"
            f"\nPotência da Motobomba: {potencia_cv:.2f} cv"
        )
        messagebox.showinfo("Resultados", result_text)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira todos os valores corretamente.")

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Calculadora de Irrigação")

# Criando os campos de entrada
labels = [
    "Comprimento da Parcela (m):", 
    "Largura da Parcela (m):", 
    "Profundidade da Raiz (cm):", 
    "Capacidade de Campo do Solo (%):", 
    "Ponto de Murcha Permanente (%):", 
    "Coeficiente Cultural Crítico (Kc):", 
    "Eficiência do Sistema de Irrigação (%):", 
    "Jornada de Trabalho por Dia (horas):", 
    "Evapotranspiração Máxima (mm/dia):", 
    "Densidade do Solo (g/cm³):", 
    "Taxa de Infiltração do Solo (mm/h):", 
    "Taxa de Fluxo do Aspersor (m³/h):", 
    "Pressão de Serviço (mca):", 
    "Perda de Pressão Máxima Permitida (mca):"
]

entries = []

for label in labels:
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

(entry_comprimento, entry_largura, entry_profundidade, entry_capacidade, 
 entry_ponto, entry_kc, entry_eficiencia, entry_jornada, 
 entry_evapotranspiracao, entry_densidade, entry_infiltracao, 
 entry_fluxo, entry_pressao, entry_perda) = entries

# Botão para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_irrigacao)
btn_calcular.pack()

# Iniciar a interface
root.mainloop()
