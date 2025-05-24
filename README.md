# 📸 Detecção de Vagas em Estacionamento com OpenCV

Este projeto utiliza a biblioteca OpenCV para detectar e contar automaticamente o número de vagas de estacionamento disponíveis em um vídeo.

## 🧠 Visão Geral

O sistema permite que o usuário selecione manualmente as regiões correspondentes às vagas em uma imagem estática, e depois utiliza esse mapeamento para analisar um vídeo e identificar, em tempo real, quais vagas estão ocupadas ou livres com base em processamento de imagem.

## 📁 Estrutura do Projeto

```
.
├── media/
│   ├── estacionamento.png  # Imagem usada para capturar as regiões das vagas
│   └── video.mp4           # Vídeo do estacionamento para análise
├── vagas.pkl               # Arquivo gerado com as coordenadas das vagas
├── estacionamento.py       # Script principal
└── README.md
```

## 🚀 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual.

```bash
pip install opencv-python numpy
```

### 3. Configure as vagas

Execute o script e siga as instruções para selecionar manualmente as vagas:

```bash
python main.py
```

**Importante**: no código atual, a função `capturar_vagas()` deve ser chamada manualmente para executar essa etapa antes da contagem.

### 4. Inicie a contagem de vagas

Depois que o arquivo `vagas.pkl` for gerado, o script analisará o vídeo em tempo real:

```bash
python main.py
```

## 🛠 Funcionalidades

* Seleção manual de regiões das vagas
* Detecção em tempo real de vagas livres e ocupadas
* Contador dinâmico sobre o vídeo

## 📷 Exemplo Visual

Adicione aqui um GIF ou imagem de demonstração.

## 📌 Observações

* O limite de 69 vagas está definido fixamente no código, mas pode ser ajustado conforme sua necessidade.
* O limiar de contagem de pixels (750) para considerar uma vaga ocupada pode precisar de ajuste conforme a qualidade do vídeo.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
