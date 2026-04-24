from machine import Pin, ADC, PWM
import time

UMIDADE_MIN = 40
UMIDADE_MAX = 70
PH_MIN = 6.0
PH_MAX = 7.5
TEMP_MIN = 20
TEMP_MAX = 30

pwm_r = PWM(Pin(18))
pwm_g = PWM(Pin(5))
pwm_b = PWM(Pin(4))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

umidade_adc = ADC(Pin(14))
umidade_adc.atten(ADC.ATTN_11DB)
umidade_adc.width(ADC.WIDTH_12BIT)

ph_adc = ADC(Pin(12))
ph_adc.atten(ADC.ATTN_11DB)
ph_adc.width(ADC.WIDTH_12BIT)

temperatura_adc = ADC(Pin(13))
temperatura_adc.atten(ADC.ATTN_11DB)
temperatura_adc.width(ADC.WIDTH_12BIT)

def ler_umidade():
    return (umidade_adc.read() / 4095) * 100

def ler_ph():
    return (ph_adc.read() / 4095) * 14

def ler_temperatura():
    return (temperatura_adc.read() / 4095) * 100

def set_color(r, g, b):
    pwm_r.duty(int(r * 1023 / 100))
    pwm_g.duty(int(g * 1023 / 100))
    pwm_b.duty(int(b * 1023 / 100))

def definir_cor(u, p, t):
    if (UMIDADE_MIN <= u <= UMIDADE_MAX and 
        PH_MIN <= p <= PH_MAX and 
        TEMP_MIN <= t <= TEMP_MAX):
        return 0, 100, 0
    
    if u < UMIDADE_MIN:
        return 100, 0, 0
    if u > UMIDADE_MAX:
        return 100, 0, 100
    
    if p < PH_MIN:
        return 0, 0, 100
    if p > PH_MAX:
        return 50, 100, 50
    
    if t < TEMP_MIN:
        return 0, 100, 100
    if t > TEMP_MAX:
        return 100, 50, 0
    
    return 0, 0, 0

def gerar_status(u, p, t):
    if (UMIDADE_MIN <= u <= UMIDADE_MAX and 
        PH_MIN <= p <= PH_MAX and 
        TEMP_MIN <= t <= TEMP_MAX):
        return "SOLO PERFEITO"
    
    problemas = []
    if u < UMIDADE_MIN: problemas.append("Solo seco")
    elif u > UMIDADE_MAX: problemas.append("Solo encharcado")
    if p < PH_MIN: problemas.append("pH acido")
    elif p > PH_MAX: problemas.append("pH alcalino")
    if t < TEMP_MIN: problemas.append("Temp baixa")
    elif t > TEMP_MAX: problemas.append("Temp alta")
    
    return " | ".join(problemas)

def gerar_recomendacao(u, p, t):
    dicas = []
    if u < UMIDADE_MIN: dicas.append("Regar")
    elif u > UMIDADE_MAX: dicas.append("Drenar")
    if p < PH_MIN: dicas.append("Calcario")
    elif p > PH_MAX: dicas.append("Enxofre")
    if t < TEMP_MIN: dicas.append("Aquecer")
    elif t > TEMP_MAX: dicas.append("Resfriar")
    
    return " | ".join(dicas) if dicas else "OK"

while True:
    print("\033[2J\033[H", end="")
    u = ler_umidade()
    p = ler_ph()
    t = ler_temperatura()
    
    r, g, b = definir_cor(u, p, t)
    set_color(r, g, b)

    print("-----------------------Leitura do Solo-----------------------")
    print("-" * 40)
    print(f"Umidade: {u:.1f}%")
    print(f"pH: {p:.1f}")
    print(f"Temperatura: {t:.1f}C")
    print("-" * 40)
    print("Status:", gerar_status(u, p, t))
    print("Recomendacao:", gerar_recomendacao(u, p, t))
    print("-" * 40)
    
    time.sleep(0.5)