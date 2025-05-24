# 📸 Detecção de Vagas em Estacionamento com OpenCV

Este projeto utiliza a biblioteca OpenCV para detectar e contar automaticamente o número de vagas de estacionamento disponíveis em um vídeo.

## 🧠 Visão Geral

O sistema permite que o usuário selecione manualmente as regiões correspondentes às vagas em uma imagem estática, e depois utiliza esse mapeamento para analisar um vídeo e identificar, em tempo real, quais vagas estão ocupadas ou livres com base em processamento de imagem.


## 🛠 Funcionalidades

* Seleção manual de regiões das vagas
* Detecção em tempo real de vagas livres e ocupadas
* Contador dinâmico sobre o vídeo

## 📷 Exemplo Visual
![Demonstração](media/2025-05-24-00-02-00.gif)

## 📌 Observações

* O limite de 69 vagas está definido fixamente no código, mas pode ser ajustado conforme sua necessidade.
* O limiar de contagem de pixels (750) para considerar uma vaga ocupada pode precisar de ajuste conforme a qualidade do vídeo.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
