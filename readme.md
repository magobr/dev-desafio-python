# Desafio de Desenvolvimento: Jogo Pedra, Papel e Tesoura

## 🎯 Objetivo
Desenvolver um jogo simples de **Pedra, Papel e Tesoura** em Python, onde o usuário possa jogar contra o computador.

## 📋 Descrição do Jogo
Pedra, Papel e Tesoura é um jogo clássico onde:
- **Pedra** vence **Tesoura** (amassa)
- **Tesoura** vence **Papel** (corta)
- **Papel** vence **Pedra** (embrulha)

## 🎮 Funcionalidades Esperadas

### Funcionalidades Básicas (Obrigatórias)
1. **Menu inicial** com opções para jogar ou sair
2. **Entrada do usuário** para escolher entre Pedra, Papel ou Tesoura
3. **Geração aleatória** da jogada do computador
4. **Lógica do jogo** para determinar o vencedor
5. **Exibição do resultado** de cada rodada
6. **Contador de placar** (vitórias, derrotas, empates)

### Funcionalidades Extras (Opcionais)
1. **Validação** da entrada do usuário
2. **Histórico** de partidas
3. **Múltiplas rodadas** em uma mesma execução
4. **Interface mais amigável** com ASCII art
5. **Diferentes níveis de dificuldade**

## 🛠️ Requisitos Técnicos

### Tecnologias
- **Linguagem**: Python 3.x
- **Bibliotecas permitidas**: 
  - `random` (para jogada do computador)
  - `time` (para delays, se desejar)

## 📝 Instruções de Desenvolvimento

### Passo a Passo
1. **Configuração Inicial**
   ```bash
   # Crie um novo arquivo Python
   touch jogo_pedra_papel_tesoura.py
   ```

2. **Implemente as funções básicas**:
   - Comece pela lógica principal do jogo
   - Implemente a geração da jogada do computador
   - Crie a função para determinar o vencedor

3. **Adicione validações**:
   - Garanta que o usuário só possa inserir jogadas válidas
   - Trate possíveis erros de entrada

4. **Melhore a experiência**:
   - Adicione mensagens claras
   - Inclua um placar
   - Formate a saída para melhor legibilidade

### Exemplo de Entrada/Saída
```
=== Pedra, Papel e Tesoura ===

Escolha sua jogada:
1 - Pedra
2 - Papel
3 - Tesoura
4 - Sair

Sua escolha: 2

Você escolheu: Papel
Computador escolheu: Pedra

🎉 Você venceu! Papel embrulha Pedra

Placar:
Vitórias: 1 | Derrotas: 0 | Empates: 0
```

## 🧪 Testes Sugeridos

Teste seu jogo com os seguintes cenários:
- ✅ Vitória do usuário
- ✅ Vitória do computador
- ✅ Empate
- ✅ Entrada inválida do usuário
- ✅ Opção de sair do jogo

## 💡 Dicas para Iniciantes

1. **Comece simples**: Implemente a funcionalidade básica primeiro
2. **Teste frequentemente**: Verifique cada função individualmente
3. **Use comentários**: Documente seu código para facilitar o entendimento
4. **Divida o problema**: Resolva uma parte de cada vez
5. **Não se preocupe com erros**: Eles são parte do aprendizado!

## 📤 Entrega

1. Adicione seu codigo em uma pasta dentro da pasta referente ao seu nome
2. Inclua um README com:
   - Instruções para executar o jogo
   - Funcionalidades implementadas
   - Dificuldades encontradas (se houver)
   - Possíveis melhorias

## 🚀 Bônus (Para Desafio Extra)

Se quiser ir além, você pode:
- Adicionar as variações **Pedra, Papel, Tesoura, Lagarto, Spock**
- Criar uma interface gráfica simples com `tkinter`
- Implementar um sistema de ranking
- Adicionar sons e animações

---

**Boa sorte e divirta-se programando!** 🎮🐍