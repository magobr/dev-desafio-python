import random

# Banco de palavras por categoria
palavras = {
    "frutas": ["banana", "maca", "laranja", "uva", "morango"],
    "animais": ["gato", "cachorro", "elefante", "girafa", "panda"],
    "paises": ["brasil", "argentina", "canada", "japao", "australia"]
}
forca_estagios = ["""
     _______
      |     |
      |     
      |     
      |     
      |     
      |     
    """,
    """
      _______
      |     |
      |     O
      |     
      |     
      |     
      |     
    """,
    """
      _______
      |     |
      |     O
      |     |
      |     
      |     
      |     
    """,
    """
      _______
      |     |
      |     O
      |    /|
      |     
      |     
      |     
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |     
      |     
      |     
    """,
     """
      _______
      |     |
      |     O
      |    /|\\
      |    / 
      |     
      |     
    """,
    """
      _______
      |     |
      |     O
      |    /|\\
      |    / \\
      |     
      |
"""]

#criando controles de seleção
def escolher_palavra(categoria=None):
   
        while True:
            op = (input("""
                        Selecione o Tema desejado:
                        1) Fruta
                        2) Animais
                        3) Paises
                        """))
            
            if op.lower() == "1":
                categoria = "frutas"
                
            elif op.lower() == "2":
                categoria = "animais"
                
            elif op.lower() == "3":
                categoria = "paises"
                
            else:
                print("❌ Opção inválida! Tente novamente.")
                continue
            
            palavra = random.choice(palavras[categoria])
            print(f"\n🎯 Categoria escolhida: {categoria.capitalize()}")
        
          

            return palavra
        
#Guardar informações na variavel
palavra_secreta = escolher_palavra()
letras_descobertas = ["_"]  * len(palavra_secreta)
tentativas_maximas  = len(forca_estagios) - 1
erros = 0

print(f"A palavra tem {len(palavra_secreta)} letras.")
print("_".join(letras_descobertas))
print(forca_estagios[0])

#jogo começa

while "_" in letras_descobertas and erros < tentativas_maximas:
    letra = input("\nDigite uma letra: ").lower()

    if letra in palavra_secreta:
        print("✅ Letra encontrada!")
        # Revelar as posições certas das letras
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        erros += 1
        print("❌ Essa letra não existe na palavra.")
        print(forca_estagios[erros]) #Mostrar boneco da vez

    print(" ".join(letras_descobertas))

if "_" not in letras_descobertas:
     print("\n🎉 Parabéns! Você descobriu a palavra:", palavra_secreta)
else:
    print(forca_estagios[-1])
    print("\n💀 Você foi enforcado! A palavra era:", palavra_secreta)

