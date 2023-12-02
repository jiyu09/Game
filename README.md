# Game
프로그래밍 실습 test
# 게임 설명

**주사위** 굴리는 게임입니다.

player는 총 **2명**입니다. (혼자서 해도 되지만 같이 하는 것이 재밌을 거에요😀)

게임을 시작하기 전에 **내기**라도 걸어보시길.. 행운이 기다리고 있을 것입니다 🍀

이제 게임을 시작하기 전, 간단한 설명을 하겠습니다 !

각자 6번의 턴 안에 **5개**의 주사위를 가지고 나온 주사위 눈으로 **점수**를 따서 

총 점이 큰 사람이 이기는 아주 쉬운 게임입니다.

하지만 주사위를 다시 굴릴 수 있는 chance가 2번이나 있다는 점에 주목하세요 !

원하는 점수 방식을 유도할 수 있거든요. (점수 방식에 대해서는 아래에서 설명할 것입니다)

## 주사위 굴리기

아쉬운 주사위 눈을 골라서 다시 굴릴 수 있는 기회가 한 try 당 총 2번 있습니다.

![스크린샷 2023-12-01 183351.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b5be55d2-21fd-4abe-972b-f04fbb6062f6/e33f2a3c-1037-4b8e-9116-7bdd9f405f2d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-12-01_183351.png)

만약 주사위 눈이 위의 사진처럼 [4], [5], [3], [5], [1] 나왔을 때

player가 1번째 주사위인 [4]와 2번째 주사위인 [5]를 다시 돌리고 싶다면, 1과 2를 공백으로 구분하여 입력해주세요.

if 처음에 나온 주사위 눈들이 모두 완벽하다면 ?

0을 입력하여 점수를 계산해보세요.

if 공백으로 구분하지 않고 12를 입력한다면 ?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b5be55d2-21fd-4abe-972b-f04fbb6062f6/716a629c-303b-4a3e-ac6b-2bfc46b55e80/Untitled.png)

에러 문구가 뜨고 다시 입력하도록 해줍니다.

if  ‘1 2        ‘를 입력한다면 ?

걱정하지 마세요. strip()이 당신을 도와줄 것입니다.

다시 굴린 주사위 눈을 보고 아직 player 마음에 안 든다면 기회는 1번이 더 남아있습니다.

그렇게 다시 주사위를 굴린다면 이제는 남은 기회는 없습니다.

점수 계산하러 가볼까요?

## 점수 계산

당신은 이제 더 이상 주사위를 바꿀 수 없습니다.

주사위 눈은 마음에 드시나요?

tip 점수 계산 방식에 무엇이 있는지 알면 점수 획득에 더 유리합니다. (더 전략적으로 플레이 할 수 있겠죠)

### 상단 스코어 계산 방식

- **ones** : 당신이 가진 주사위 중에 [1]이 있다면 [1]의 합 계산

      (ex [1] [2] [1] [2] [4] = 2점 획득)

- **Twos** : 당신이 가진 주사위 중에 [2]가 있다면 [2]의 합 계산

      (ex [3] [4] [2] [4] [2] = 4점 획득)

- **Threes** : 당신이 가진 주사위 중에 [3]이 있다면 [3]의 합 계산

      (ex [3] [4] [2] [6] [3] = 6점 획득)

- **Fours** : 당신이 가진 주사위 중에 [4]이 있다면 [4]의 합 계산

      (ex [1] [3] [4] [6] [4] = 8점 획득)

- **Fives** : 당신이 가진 주사위 중에 [5]이 있다면 [5]의 합 계산

      (ex [2] [3] [5] [6] [5] = 10점 획득)

- **Sixes** : 당신이 가진 주사위 중에 [6]이 있다면 [6]의 합 계산

      (ex [2] [4] [5] [6] [6] = 12점 획득)

깨달았겠지만, 주사위 눈이 높을수록 유리합니다.

그리고 재밌는 룰이 존재하는데, 상단 스코어의 총 합이 63점 이상이면, bonus score 35점이 추가됩니다 !

밑에 나오는 하단 스코어가 특별하지만, 상단 스코어를 공략해서 보너스 점수를 얻는 것도 추천합니다 !

### 하단 스코어 계산 방식

- **Choice** : 주사위 눈 5개의 총합

      (무엇이든지 총합을 계산해주는 무적의 계산 방식이기 때문에 아껴두는 것을 추천해요 !)

- **Four_of_a_kind** : 같은 주사위 눈이 4개 이상일 때, 주사위 눈 5개의 총합

      (ex [2] [3] [2] [2] [2] = 11점)

- **Full_House** : 같은 주사위 눈이 각각 2개, 3개일 때, 주사위 눈 5개의 총합

      (ex [2] [5] [5] [2] [2] = 16점)

- **Little_Straight** : 이어지는 주사위 눈이 4개 이상일 때, 고정 15점

      (ex [1] [2] [3] [4] [n]  /  [2] [3] [4] [5] [n]  /  [3] [4] [5] [6] [n] 일 경우 다 가능)

- **Big_Straight** : 이어지는 주사위 눈이 5개일 때, 고정 30점

      (ex [1] [2] [3] [4] [5]  /  [2] [3] [4] [5] [6] 일 때 가능)

- **Yacht** : 동일한 주사위 눈이 5개일 때, 고정 50점

      (ex [4] [4] [4] [4] [4] = 50점, 이 게임의 하이라이트)

하지만 이 점수 계산 방식들은 단 한번 밖에 사용할 수 없다는 점 유의하세요 !

# 게임 실행
주소 복사 후 터미널에서 실행
     git clone https://github.com/jiyu09/Game.git

     pip install pandas

     python main.py
