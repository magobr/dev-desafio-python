# Desafio de Desenvolvimento: Jogo da Forca

## 🎯 Objetivo
Desenvolver um jogo clássico da **Forca** em Python, onde o usuário tenta adivinhar uma palavra oculta letra por letra.

## 📋 Descrição do Jogo
O Jogo da Forca é um jogo de adivinhação onde:
- O computador escolhe uma palavra aleatória
- O jogador tenta adivinhar a palavra sugerindo letras
- A cada erro, uma parte do "boneco" é desenhada na forca
- O jogador vence se adivinhar a palavra antes de completar o boneco

## 🎮 Funcionalidades Esperadas

### Funcionalidades Básicas (Obrigatórias)
1. **Banco de palavras** com categorias (ex: frutas, animais, países)
2. **Seleção aleatória** de palavras
3. **Exibição da palavra oculta** com underscores (`_ _ _ _ _`)
4. **Entrada de letras** pelo usuário
5. **Validação** das letras inseridas (apenas letras, não repetidas)
6. **Contador de tentativas** (máximo 6 erros)
7. **Exibição progressiva da forca** a cada erro
8. **Verificação de vitória/derrota**
9. **Letras já tentadas**

### Funcionalidades Extras (Opcionais)
1. **Diferentes níveis de dificuldade** (fácil, médio, difícil)
2. **Dicas** para palavras difíceis
3. **Sistema de pontuação**
4. **Histórico de palavras jogadas**
5. **Interface colorida** no terminal
6. **Modo multiplayer** (um jogador escolhe a palavra)
7. **Salvar/recuperar progresso**

## 🛠️ Requisitos Técnicos

### Tecnologias
- **Linguagem**: Python 3.x
- **Bibliotecas permitidas**:
  - `random` (para escolher palavras)
  - `time` (para delays)
  - `os` (para limpar tela)

### Estrutura do Código Sugerida
```python
import random

# Banco de palavras por categoria
palavras = {
    "frutas": ["banana", "maca", "laranja", "uva", "morango"],
    "animais": ["gato", "cachorro", "elefante", "girafa", "panda"],
    "paises": ["brasil", "argentina", "canada", "japao", "australia"]
}

def escolher_palavra(categoria=None):
    # Escolher palavra aleatória
    pass

def mostrar_forca(erros):
    # Desenhar a forca baseado no número de erros
    pass

def mostrar_palavra_oculta(palavra, letras_corretas):
    # Mostrar _ _ _ _ com letras descobertas
    pass

def obter_letra_usuario(letras_tentadas):
    # Receber e validar letra do usuário
    pass

def verificar_letra(letra, palavra):
    # Verificar se letra está na palavra
    pass

def jogo_completo(palavra):
    # Verificar se todas as letras foram adivinhadas
    pass

def main():
    # Função principal do jogo
    pass

if __name__ == "__main__":
    main()
```

## 📝 Instruções de Desenvolvimento

### Passo a Passo
1. **Configuração Inicial**
   ```bash
   touch jogo_da_forca.py
   ```

2. **Implemente o núcleo do jogo**:
   - Crie o banco de palavras
   - Implemente a lógica de exibição da palavra oculta
   - Desenvolva a entrada e validação de letras

3. **Crie o sistema da forca**:
   - Desenhe os estágios da forca (0 a 6 erros)
   - Implemente a contagem de erros

4. **Adicione features**:
   - Sistema de categorias
   - Letras já tentadas
   - Mensagens de feedback

### Exemplo de Entrada/Saída
```
=== JOGO DA FORCA ===

Categorias disponíveis:
1 - Frutas
2 - Animais
3 - Países

Escolha uma categoria: 1

Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Letras tentadas: 

Digite uma letra: A

✅ Letra correta!

Palavra: _ A _ A _ A
Tentativas restantes: 6
Letras tentadas: A

Digite uma letra: B

❌ Letra incorreta!
  _______
  |     |
  |     O
  |
  |
  |
  |
  |

Palavra: _ A _ A _ A
Tentativas restantes: 5
Letras tentadas: A, B
```

## 🎨 Representação da Forca

Sugestão de desenho para 6 estágios:

```
Estágio 0:       Estágio 1:       Estágio 2:       Estágio 3:
  _______          _______          _______          _______
  |     |          |     |          |     |          |     |
  |                |     O          |     O          |     O
  |                |                |     |          |    /|
  |                |                |                |     
  |                |                |                |     
  |                |                |                |     
  |                |                |                |     

Estágio 4:       Estágio 5:       Estágio 6:
  _______          _______          _______
  |     |          |     |          |     |
  |     O          |     O          |     O
  |    /|\         |    /|\         |    /|\
  |    /           |    /           |    / \
  |                |                |     
  |                |                |     
  |                |                |     
```

## 🧪 Testes Sugeridos

Teste seu jogo com os seguintes cenários:
- ✅ Vitória (adivinhar todas as letras)
- ✅ Derrota (completar a forca)
- ✅ Letra repetida
- ✅ Entrada inválida (números, símbolos, mais de uma letra)
- ✅ Palavras com letras repetidas
- ✅ Diferentes categorias

## 💡 Dicas para Iniciantes

1. **Comece com ASCII simples**: Não precisa ser perfeito desde o início
2. **Use listas** para controlar letras corretas e tentadas
3. **Funções são suas amigas**: Divida o problema em funções menores
4. **Teste com palavras curtas** primeiro
5. **Use `.lower()`** para normalizar as entradas

## 📊 Sistema de Pontuação (Bônus)

Se implementar pontuação:
```
- Letra correta: +10 pontos
- Letra errada: -5 pontos
- Vitória: +100 pontos + (tentativas_restantes × 20)
- Dica usada: -30 pontos
```

## 📤 Entrega

1. Crie um repositório no GitHub
2. Adicione o arquivo `.py` com seu código
3. Inclua um README com:
   - Instruções para executar o jogo
   - Funcionalidades implementadas
   - Exemplo do jogo funcionando
   - Desafios encontrados e como superou
   - Possíveis melhorias futuras

## 🚀 Desafios Extras (Para Ir Além)

Se quiser se desafiar mais:
- 🔤 **Acentuação**: Suporte a palavras com acentos
- 🎨 **Cores**: Use biblioteca `colorama` para terminal colorido
- 💾 **Save/Load**: Salvar jogo em andamento em arquivo
- 🌐 **API**: Buscar palavras de API externa
- 🎵 **Sons**: Adicionar efeitos sonoros
- 🖥️ **GUI**: Interface gráfica com `tkinter` ou `pygame`

---

**Divirta-se criando seu jogo da forca! Lembre-se: o importante é aprender e se divertir no processo!** 🎮🐍📚