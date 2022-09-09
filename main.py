from Game import *
from Player import *
from random import choices

def set_starting_player_grub():
    print("Bem vindo ao jogo 21!!!")

    while True:
        try:
            starting_player = int(input("\nQuem vai começar o jogo?\n  0 - NPC\n  1 - Player\n>> "))

            if input_is_valid(starting_player):
                return starting_player
        except:
            print("Digite apenas números!!")


def main():
    game = Game()
    player = Player("Player", game.get_card())
    npc = Player("NPC", game.get_card())
    starting_player = set_starting_player_grub()

    if starting_player:
        player_game(player, game)
        npc_game(npc, game)
    else:
        npc_game(npc, game)
        print(f"\nO {npc.name} jogou, agora é a sua vez!!!")
        player_game(player, game)

    print(f"""
{player}
==========================
{npc}
""")
    print(game.winner(player, npc))

def player_game(player, game):
    while True:
        print(f"\n{player}")
        
        while True:
            try:
                action = int(input("\nVocê quer continuar?\n  0 - Não\n  1 - Sim\n>> "))
                if input_is_valid(action):
                    break
            except:
                print("Digite apenas números!!")

        game.round(player) if action else player.stop_playing()

        if not player.is_playing:
            break

def npc_game(npc, game):    
    while True:
        if npc.points <= 11:
            probability = (100, 0)
        elif npc.points >= 15:
            probability = (20, 80)
        else:
            probability = (50, 50)

        action = choices((True, False), weights=probability)[0]
        game.round(npc) if action else npc.stop_playing()

        if not npc.is_playing:
            break

def input_is_valid(input):
    if not 0 <= input <= 1:
        print("Número inválido!! Digite apenas 0 ou 1")
        return False
    return True

main()
