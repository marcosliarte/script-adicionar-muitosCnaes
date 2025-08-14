import pyautogui
import time
import os

# Configuração
pyautogui.PAUSE = 0.5
tempo_carregamento = 3
tempo_apos_adicionar = 3
confianca = 0.8

PASTA_IMAGENS = os.path.dirname(os.path.abspath(__file__))

cnaes = [
    "4923002", "3811400", "3812200", "3822000", "3831901", "3831999", "3832700", "3839401", "3839499", "4313400", "4399105", 
"4712100", "4781400", "4782201", "4783102", "4924800", "5022001", "5022002", "5620101", "5620102", "5620103", "4639701", 
"1412601", "2330302", "3313901", "3812200", "4120400", "4213800", "4221903", "4221904", "4221905", "4222701", "4222702", 
"4223500", "4292801", "4292802", "4299501", "4299599", "4311801", "4311802", "4312600", "4313400", "4321500", "4322301", 
"4322302", "4322303", "4329101", "4330401", "4330402", "4330403", "4330404", "4330405", "4330499", "4391600", "4399101", 
"4399103", "4399105", "4614100", "4616800", "4639702", "4644301", "4647801", "4649404", "4649409", "4673700", "4679699", 
"4742300", "4744099", "4753900", "4754701", "4755501", "4756300", "4763601", "4763602", "4772500", "4789007", "4923002", 
"4924800", "4930201", "4930204", "5012201", "5022001", "5022002", "5212500", "5223100", "5240199", "5620101", "5620102", 
"5620103", "6209100", "7020400", "7311400", "7420001", "7711000", "7719501", "7719599", "7721700", "7729202", "7729203", 
"7731400", "7732201", "7732202", "7733100", "7739003", "7739099", "8020001", "8121400", "8129000", "8130300", "8211300", 
"8220200", "8230001", "8599604", "9001906", "9329899", "9512600"
    # restante da lista
]

def localizar_e_clicar(nome_arquivo, descricao, tentativas=5, delay=1):
    caminho_imagem = os.path.join(PASTA_IMAGENS, nome_arquivo)
    if not os.path.isfile(caminho_imagem):
        print(f"[ERRO] Arquivo não encontrado: {caminho_imagem}")
        return False

    for i in range(tentativas):
        try:
            pos = pyautogui.locateCenterOnScreen(caminho_imagem, confidence=confianca)
            if pos:
                pyautogui.click(pos)
                return pos
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(delay)
    print(f"[ERRO] Não foi possível encontrar {descricao}")
    return False

print("Posicione a tela e aguarde 5 segundos...")
time.sleep(5)

# Localiza o campo de pesquisa inicialmente
campo_pesquisa_pos = localizar_e_clicar("campo_pesquisa.png", "campo de pesquisa")
if not campo_pesquisa_pos:
    print("Não foi possível localizar o campo de pesquisa. Abortando...")
    exit()

for cnae in cnaes:
    print(f"Inserindo CNAE: {cnae}")

    # Clica na posição salva do campo
    pyautogui.click(campo_pesquisa_pos)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.typewrite(cnae)

    # Botão pesquisar
    if not localizar_e_clicar("botao_pesquisar.png", "botão pesquisar"):
        print(f"[PULAR] CNAE {cnae} pulado.")
        continue

    time.sleep(tempo_carregamento)

    # Botão adicionar
    if not localizar_e_clicar("botao_adicionar.png", "botão adicionar"):
        print(f"[PULAR] CNAE {cnae} pulado.")
        continue

    # Aguarda antes de limpar
    time.sleep(tempo_apos_adicionar)

    # Limpa o campo usando a posição salva, **sem localizar a imagem de novo**
    pyautogui.click(campo_pesquisa_pos)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(0.5)

print("Processo finalizado.")
