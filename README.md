# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

------

### 👤 Identificação do Candidato

- **Nome completo: Raphael Sousa Rabelo Rates**  

---

## 1️⃣ Visão Geral da Solução

O projeto consiste em um **sistema embarcado de monitoramento de solo** que mede três parâmetros fundamentais para o plantio: **umidade**, **pH** e **temperatura**. O sistema simula a leitura destes sensores via potenciômetros (no Wokwi) e fornece feedback visual através de um **LED RGB**, além de exibir no console o status do solo e recomendações de correção. O usuário interage observando as cores do LED e as mensagens no terminal serial.

---

## 2️⃣ Arquitetura do Sistema Embarcado

### Fluxo principal do programa:
1. **Inicialização** – Configuração dos pinos, PWM para o LED e ADCs para os sensores.
2. **Loop infinito** – Leitura contínua dos três sensores a cada 0,5 segundos.
3. **Processamento** – Verificação se os valores estão dentro das faixas ideais.
4. **Saída** – Atualização da cor do LED e exibição dos resultados no console.

### Estrutura do código:
- **Funções de leitura** (`ler_umidade`, `ler_ph`, `ler_temperatura`) – Convertem valores do ADC (0-4095) para escalas reais.
- **Função de controle do LED** (`set_color`) – Define intensidade PWM para cada canal RGB.
- **Função de lógica condicional** (`definir_cor`) – Mapeia parâmetros para cores específicas.
- **Funções de interface** (`gerar_status`, `gerar_recomendacao`) – Geram mensagens descritivas.
- **Loop principal** – Executa leituras, processa e atualiza saídas com temporização fixa.

### Interação entre componentes:
```
Sensor Umidade (ADC) → Leitura (%) → Lógica de decisão → LED RGB (PWM)
Sensor pH (ADC)      → Leitura (pH) → Lógica de decisão → Console Serial
Sensor Temp (ADC)    → Leitura (°C)  → Lógica de decisão → Mensagens
```

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | Pino | Função |
|------------|------|--------|
| **Placa** | ESP32 | Microcontrolador principal |
| **Potenciômetro Umidade** | GPIO 14 (ADC) | Simula sensor de umidade (0-100%) |
| **Potenciômetro pH** | GPIO 12 (ADC) | Simula sensor de pH (0-14) |
| **Potenciômetro Temperatura** | GPIO 13 (ADC) | Simula sensor de temperatura (0-100°C) |
| **LED RGB (Vermelho)** | GPIO 18 (PWM) | Indica solo seco ou problemas críticos |
| **LED RGB (Verde)** | GPIO 5 (PWM) | Indica solo perfeito |
| **LED RGB (Azul)** | GPIO 4 (PWM) | Indica pH ácido ou temperatura baixa |

---

## 4️⃣ Decisões Técnicas Relevantes

### Organização do código:
- **Modularização por funções** – Cada responsabilidade isolada (leitura, lógica, saída).
- **Constantes no início** – Limites dos parâmetros centralizados para fácil ajuste.
- **Nomes descritivos** – Funções autoexplicativas (`definir_cor`, `gerar_recomendacao`).

### Lógica de cores (prioridades):
O sistema adota **prioridade de alertas** na seguinte ordem:
1. Umidade (seca ou encharcada) – **Vermelho** ou **Roxo**
2. pH (ácido ou alcalino) – **Azul** ou **Verde claro**
3. Temperatura (baixa ou alta) – **Ciano** ou **Laranja**
4. Tudo OK – **Verde**

### Temporização:
- **Delay fixo de 0,5s** no loop principal – Atualizações periódicas e estáveis.
- Sem uso de timers ou interrupções – Projeto simplificado para simulação.

### PWM:
- **Frequência de 1 kHz** – Adequada para LED RGB.
- **Resolução de 10 bits (0-1023)** – Controle suave de intensidade.
- **Mapeamento 0-100% → 0-1023** – Facilita a lógica de cores.

---

## 5️⃣ Resultados Obtidos

### Comportamento final do sistema:

| Condição | LED | Status | Recomendação |
|----------|-----|--------|---------------|
| Tudo dentro dos limites | 🟢 Verde | SOLO PERFEITO | OK |
| Umidade < 40% | 🔴 Vermelho | Solo seco | Regar |
| Umidade > 70% | 🟣 Roxo | Solo encharcado | Drenar |
| pH < 6,0 | 🔵 Azul | pH ácido | Calcário |
| pH > 7,5 | 🟢 Verde claro | pH alcalino | Enxofre |
| Temperatura < 20°C | 🔷 Ciano | Temp baixa | Aquecer |
| Temperatura > 30°C | 🟠 Laranja | Temp alta | Resfriar |

### Requisitos atendidos:
- ✅ Leitura de 3 sensores analógicos via ADC
- ✅ Controle de LED RGB com PWM
- ✅ Exibição contínua de dados no console
- ✅ Geração de status e recomendações textuais
- ✅ Feedback visual por cores para diagnóstico rápido

### Resultado na simulação Wokwi:
O sistema executa em loop infinito, respondendo em tempo real às variações dos potenciômetros, alterando a cor do LED e atualizando as mensagens a cada 0,5 segundo.

---

## 6️⃣ Comentários Adicionais

### Dificuldades encontradas:
- Ajustar as escalas dos ADCs para representar corretamente as grandezas físicas (umidade 0-100%, pH 0-14, temperatura 0-100°C).
- Definir a ordem de prioridade das cores para que alertas mais críticos (ex: solo seco) sobressaiam sobre outros (ex: temperatura levemente alta).

### Limitações da solução:
- Simulação com potenciômetros não representa sensores reais (higrômetro, sonda de pH, termistor).
- Sem histerese – Pequenas oscilações podem causar mudanças rápidas de cor.
- Sem botão ou interface adicional – Apenas monitoramento passivo.

### Melhorias com mais tempo:
- Implementar médias móveis para suavizar leituras ruidosas.
- Adicionar botão para alternar entre modo automático e leitura única.
- Incluir display LCD/I2C para exibir dados sem necessidade de computador.
- Implementar calibração dos sensores via software.

### Principais aprendizados:
- Uso de PWM para controle de intensidade de LEDs.
- Conversão ADC → grandezas físicas reais.
- Lógica condicional com múltiplas prioridades.
- Organização de código embarcado em MicroPython.
- Importância de feedback visual claro para usuários finais.

---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
