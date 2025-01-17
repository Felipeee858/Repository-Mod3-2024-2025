#Felipe Silva nº6 10ºT
# Exercício de Funções em Python

def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    dobro=valor*2
    print(dobro)
	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    média=(n1+n2+n3)/3
    return média

	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    Fatorial=1
    for nº in range(1,numero+1):
        Fatorial=Fatorial *nº
    return Fatorial


	
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    Fahrenheit=(celsius*9/5)+32
    print (Fahrenheit)

def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    Use pi = 3.14159

    """
    pi=3.14159
    área=pi * (raio*raio)
    return área

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range (inicio,-1,-1):
        print(i)


def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    mensagem=""
    for i in range(len(texto),-1,-1,-1):
        mensagem=mensagem+texto[i]
    return mensagem
                #ou
    """
    texto_invertido=""
    for letra in texto:
        texto_invertido=letra + texto_invertido
    return texto_invertido2"""



def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    if a%b == 0:
        print("É divisível")
    else:
        print("Não é divisível")


def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    #2 π r ‍
    pi=3.14159
    perímetro=2*pi*raio
    return perímetro

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    minutos=segundos//60
    #segundos restam=segundos%60
    #return f"{minutos}:{segundos_restam}
    return minutos

def gerar_saudacao_periodo():
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    import datetime
    #datetime.datetime.now())
    data=datetime.datetime.now().hour
    if data <12:
        mensagem="Bom dia!"
        return mensagem
    elif data >= 12 and data <=18:
        mensagem="Boa tarde!"
        return mensagem
    elif data > 18:
        print("Boa noite!")

	

def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    percentagem=100-percentual
    preço_desconto=preco*percentagem/100
    return preço_desconto
    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    v_m=distancia/tempo
    return v_m

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """
    resultado=palavra==inverter_string(palavra)
    return resultado
    