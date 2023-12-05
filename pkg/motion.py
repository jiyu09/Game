# 박지유
import os # operating system 모듈 import
import time # time 모듈 import

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # 터미널 화면 지우는 함수
      # 현재 사용 중인 운영 체제의 이름이 nt이면(윈도우 경우), cls 사용
      # 현재 사용 중인 운영 체제의 이름이 nt가 아니라면(유닉스 계열), clear 사용

def draw_christmas_tree(tree, dice_position, dice_value): # 주사위 포함 트리 출력 함수
    for i, line in enumerate(tree):
        if i == 2:  # 트리의 3번째 줄에 주사위 변환이 놓여짐
            print(line[:dice_position] + str(dice_value) + line[dice_position + 1:])
        else:
            print(line)

def move_dice(tree_width, dice_position, speed): # 주사위 위치 지정 함수
    dice_position += speed
    if dice_position > tree_width - 1: # 주사위가 트리를 넘어가면 다시 주사위 포지션이 0으로 지정
        dice_position = 0
    return dice_position

def main():
    christmas_tree = [
        "         🌟         ",
        "       🎄 \\\        ",
        "       /   \\\🎁     ",
        "     🔔 🎅  \\\      ",
        "     /======🎄\\    ",
        "        |||         "
    ]

    tree_width = len(christmas_tree[0])
    dice_position = 0
    speed = 1

    for _ in range(8):
        clear_terminal()

        dice_position = move_dice(tree_width, dice_position, speed)
        draw_christmas_tree(christmas_tree, dice_position, _%6+1) # 1에서 6까지 숫자가 위치 바꿔가면서 트리와 함께 반환
        print('주사위 굴리는 중...')

        time.sleep(0.2) # 0.2초 동안 화면 유지 (즉 0.2x8 = 1.6초 동안 주사위 굴리는 화면 생성)