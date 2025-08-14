Script para Adicionar Múltiplos CNAEs Automaticamente

Este script em Python automatiza o processo de adicionar vários códigos CNAE (Classificação Nacional de Atividades Econômicas) em um sistema web, utilizando PyAutoGUI para interação com a interface gráfica.

Ele é ideal para casos em que há a necessidade de inserir um grande volume de CNAEs repetidamente, reduzindo o tempo gasto e evitando trabalho manual repetitivo.

📋 Funcionalidades

Leitura automática de lista de CNAEs pré-definidos.

Localização e clique em elementos da tela com base em imagens de referência.

Preenchimento automático do campo de pesquisa com o CNAE.

Clique no botão de pesquisa e, em seguida, no botão de adicionar.

Limpeza automática do campo após cada inserção.

Controle de tempo de espera entre etapas para garantir carregamento da página.

🚀 Tecnologias Utilizadas

Python

PyAutoGUI – Automação de mouse e teclado.

time – Controle de tempo entre ações.

os – Manipulação de diretórios e arquivos.

⚙️ Configuração
1. Instalar dependências
pip install pyautogui


Dica: Em alguns sistemas, pode ser necessário instalar também opencv-python para suporte ao parâmetro confidence:

pip install opencv-python

2. Estrutura de arquivos

No mesmo diretório do script, adicione as imagens de referência:

campo_pesquisa.png – Captura do campo onde será digitado o CNAE.

botao_pesquisar.png – Captura do botão de pesquisa.

botao_adicionar.png – Captura do botão de adicionar.

3. Configurações no código

No início do script, é possível ajustar:

tempo_carregamento → tempo de espera após clicar em "Pesquisar".

tempo_apos_adicionar → tempo de espera após adicionar o CNAE.

confianca → nível de similaridade para localizar imagens (padrão: 0.8).

▶️ Como Usar

Abra o sistema web onde os CNAEs serão inseridos.

Ajuste a tela de forma que todos os elementos estejam visíveis.

Execute o script:

python script.py


Após a mensagem:

Posicione a tela e aguarde 5 segundos...


coloque o mouse na posição correta da tela do sistema.
5. O script irá percorrer toda a lista de CNAEs automaticamente.

🛡️ Avisos Importantes

Este script simula ações humanas no computador; evite mexer no mouse/teclado durante a execução.

Funciona melhor em resolução e escala de tela fixas (não altere o zoom do navegador).

As imagens de referência devem ser capturadas exatamente como aparecem no seu sistema.

📄 Licença

Este projeto está sob a licença MIT.
