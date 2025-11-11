import random

# Banco de jogadas e emojis correspondentes
jokens = ["pedra", "papel", "tesoura"]
emojis = ["🪨", "📄", "✂️"]

# Escolhendo modo de jogo
def modo_game():
    """Escolhe o modo de jogo"""
    while True:
        modo = input("""
                    \nEscolha um modo de jogo:\n
                    1) Player VS Player
                    2) Player VS PC
                    > """)
        if modo == "1":
            print("👤 Player VS Player 👤")
            return "pvp"
        elif modo == "2":
            print("👤 Player VS PC 🖥️")
            return "pc"
        else:
            print("❌ Opção inválida! Tente novamente.")

# Modo player vs player
def player_player():
    """Modo Player VS Player"""
    while True:
        print("\n=== 👊 JOKENPÔ 👊 ===")
        print("1) Pedra 🪨\n2) Papel 📄\n3) Tesoura ✂️")
        
        # Captura e valida opções dos jogadores
        p1 = input("\n👤 Player 1, escolha: ")
        p2 = input("👤 Player 2, escolha: ")

        if p1 not in ["1", "2", "3"] or p2 not in ["1", "2", "3"]:
            print("❌ Opção inválida! Tente novamente.")
            continue

        player1 = jokens[int(p1)-1]
        player2 = jokens[int(p2)-1]

        print(f"\nPlayer 1 escolheu {player1.capitalize()} {emojis[int(p1)-1]}")
        print(f"Player 2 escolheu {player2.capitalize()} {emojis[int(p2)-1]}")

        # Resultado
        if player1 == player2:
            print("\n👀 Empatou!\n")
        elif (player1 == "pedra" and player2 == "tesoura") or \
             (player1 == "papel" and player2 == "pedra") or \
             (player1 == "tesoura" and player2 == "papel"):
            print("\n🎉 Player 1 ganhou!\n")
        else:
            print("\n🎉 Player 2 ganhou!\n")
        break


def player_pc():
    """Modo Player VS Computador"""
    while True:
        op = input("""
                    \nDigite a opção desejada:\n
                    1) Pedra
                    2) Papel
                    3) Tesoura
                    > """)
        
        if op not in ["1", "2", "3"]:
            print("\n❌ Opção inválida, tente novamente!")
            continue

        opcao = jokens[int(op) - 1]
        emoji_jogador = emojis[int(op) - 1]

        joken_pc = random.choice(jokens)
        emoji_pc = emojis[jokens.index(joken_pc)]

        print(f"\nVocê escolheu {opcao.capitalize()} {emoji_jogador}")
        print(f"O computador escolheu {joken_pc.capitalize()} {emoji_pc}")

        # Resultado
        if opcao == joken_pc:
            print("\n👀 Empatou!\n")
        elif (opcao == "pedra" and joken_pc == "tesoura") or \
             (opcao == "papel" and joken_pc == "pedra") or \
             (opcao == "tesoura" and joken_pc == "papel"):
            print("\n🎉 Você ganhou!\n")
        else:
            print("\n💀 Você perdeu - GAME OVER!\n")
        break


def main():
    modo = modo_game()  # chama o modo e guarda o retorno
    if modo == "pvp":
        player_player()
    else:
        player_pc()


main()
