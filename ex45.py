from sys import exit
from random import randint
from textwrap import dedent

class 용사(object):

    def __init__(self):

        self.이름 = ""

        # 기본 스테이터스
        self.hp = 100             # 체력
        self.Attack_Damage = 30   # 공격력
        self.Defense_Rate = 10    # 방어력

        # 기타 
        self.Money = 50          # 돈
        self.Bomb = False        # 폭탄 -> False: 없음 True: 있음
        self.old_key = False     # 열쇠
        self.Exclibur = False    # 성검 -> True 변환시 공격력 60 상승
        self.Potion = 1          # 물약 -> 갯수만큼 사용가능, 
                            # 시작 시 1개 가지고 시작

class 상인(object):
    
    def sell(self):     # 판매
        
        while 1:

            print(dedent("""
                        |1. 물약           1개 20원|
                        |2. 폭탄      최대 1개 50원|
                        |3. 낡은 열쇠 최대 1개 30원|
                        |4. 나가기(숲으로)         |
                        """))
            
            select = input("무엇을 사실건가요? 1번 물약 | 2번 폭탄 | 3번 열쇠 | 4번 나가기 | "
            "> ")
            # 물약 판매
            if "1" in select or "물약" in select:

                if 주인공.Money >= 20:
                    주인공.Money -= 20
                    주인공.Potion += 1

                    print(f"\n[물약 1개를 획득했다! (현재 {주인공.Potion}개)]")

                else:
                    print("\n돈이 부족합니다!\n")
                    
            # 폭탄 판매
            elif "2" in select or "폭탄" in select:

                if 주인공.Money >= 50:
                    주인공.Money -= 50
                    주인공.Bomb = True
                else:
                    print("\n돈이 부족합니다!\n")

            # 열쇠 판매
            elif "3" in select or "열쇠" in select:
                
                if 주인공.Money >= 30:
                    주인공.Money -= 30
                    주인공.old_key = True
                else:
                    print("\n돈이 부족합니다!\n")

            # 끝내기 -> 반복문 탈출
            else:
                print("\n감사합니다. 또 와주세요!")
                return '숲속'
    
    # def enter(self):
    #     return '숲속'
   
class 악당(object):

    hp = 100
    Attack_Damage = 15   # 공격력
    Defense_Rate = 10    # 방어력

class 마왕(악당):
    
    def __init__(self):

        self.이름 = '마왕 바알'
        self.hp = 300
        self.Attack_Damage = 50
        self.Defense_Rate = 30

class 대왕거미(악당):

    def __init__(self):

        self.이름 = '타란튤라'
        self.hp = 150
        self.Attack_Damage = 60
        self.Defense_Rate = 0

class 스켈레톤(악당):

    def __init__(self):

        self.이름 = '스켈레톤'
        self.hp = 60
        self.Attack_Damage = 20
        self.Defense_Rate = 15
    
class 도적(악당):

    def __init__(self):

        self.이름 = '도적'
        self.hp = 70
        self.Attack_Damage = 15
        self.Defense_Rate = 10

class 허수아비(악당):
    
    def __init__(self):

        self.이름 = '허수아비'
        # override
        self.hp = 100
        self.Attack_Damage = 0
        self.Defense_Rate = 20

# 스테이지
class stage(object):
    
    def enter(self):
        print("Nothing has been written")
        print("Inherit to override \"def enter\"")
        exit(1)
    
class village(stage):
    
    def enter(self):
        print(dedent(f"""
                     여기는 마을입니다. 당신의 여정이 시작되는 곳입니다. 작은 마을이지만 
                     세상은 이곳에 크게 관심이 없는 듯 하군요. 당신은 용사를 자처하며 집 밖을 나갑니다.
                     
                     아버지: 세상과 싸우기로 택하다니... 밖은 많이 위험할 거다. 의지를 보아하니 말릴 수도
                            없겠구나
                     
                     어머니: 가겠다면 이거라도 챙겨 가렴. 
                     
                     어머니는 선반에서 무언가 작은 물병을 꺼내 건냅니다.
                     
                     {주인공.이름} : 이건...
                     
                     어머니: 이건 물약이란다. 앞으로 있을 험한 환경에 도움이 될거야
                     
                     [물약을 1개 획득했다!]
                     [Tip. 물약은 체력을 30만큼 회복시킵니다.]
                     
                     당신은 부모님과 몇몇 마을 사람들의 지지를 받으며 마을을 떠납니다.

                     마을을 떠나는 길에 밭에서 버려진 허수아비 하나가 덩그러니 서 있습니다.
                     여정을 떠나기 전, 허수아비를 상대로 몸풀기를 합니다.
                     """))
        
        # 전투 (방식 1) / battle.enter() 에서 return 한 값을 return 
        연습용_허수아비 = 허수아비()
        return battle(주인공, 연습용_허수아비).enter()

        # 전투 (방식 2) / 따로 battle 객체 생성 --> 객체 enter()의 return 값을 따로 변수로 지정 뒤 return 
        # battle_intstance = battle(주인공, 허수아비)
        # result = battle_instance.enter()
        # return result
        
class forest(stage):

    def enter(self):
        print(dedent("""
                     한참을 앞을 향해 걷다보니 깊은 숲속을 걷고 있습니다. 숲속은 나무들이
                     만든 그늘 아래 시간을 가늠하기 어려워집니다. 
                     
                     (부스럭)

                     인기척이 느껴집니다. 이 숲속에선 그다지 좋은 신호로 느껴지지 않습니다.
                     아니나 다를까 도적들이 그림자 사이에서 모습을 드러냅니다. 그들의 무딘 
                     칼날은 당신을 향하고 있습니다.

                     도적: 가진걸 전부 내놓는 다면 살려서 보내주마

                     당신은 딱히 그말에 신뢰가 가지 않습니다. 어짜피 전부 빼앗긴다면 여정을
                     시작하는 의미도 없고요. 아무래도 전투를 피할 수 없을 것 같습니다.

                     도적: 거절한다면 너도 이 곳의 망자가 되어라!
                     """))
        
        # 전투 (3명) --> for 문으로 해결 
        for _ in range(3):
            
            산적 = 도적()
            battle_instance = battle(주인공, 산적)
            result = battle_instance.enter()

            # 사망 시
            if result == '사망':
                return '사망'

        # 전투 승리 후(battle 객체에서 자연스럽게 내려옴)

        print(dedent("""
                     당신의 첫 전투는 성공적이었습니다! 당신의 검은 그들을 쫓아내기에 충분했습니다.
                     
                     도적: 쳇 도망가자!
                     
                     그들은 등장 했던 때와 마찬가지로 숲 그림자 아래로 사라집니다. 하지만 적어도 그들이
                     복수할 것 같지는 않습니다.
                     당신은 재정비를 하는 도중, 그들이 놓고 간 큰 상자 하나를 발견합니다. 보물상자입니다!
                     기대에 가득찬 당신은 서둘러 상자를 열어보려 합니다.
                     
                     (철컥)
                     
                     자물쇠 소리가 들립니다. 도적들 주제에 쓸데없이 큰 자물쇠로 보물상자를 잠가놨군요.
                     자물쇠는 다이얼 식이지만 옆에 열쇠를 위한 구멍또한 있습니다. 무한정 상자 앞에서 시간을
                     보내기엔 숲속은 짙은 밤을 맞이할 준비가 머지않았습니다. 숲속에는 당신을 노리는 괴물들의
                     시선이 느껴지기 시작합니다. 기회는 5번 밖에 없습니다.
                     """))
        
        자물쇠 = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"

        chance = 5

        while chance > 0:       # 5번 반복

            정답 = input("자물쇠 3자리 >>> ")

            if 자물쇠 == 정답:          # 자물쇠 번호를 맞춘 경우
                print(dedent("""
                             (덜그럭 덜그럭... 철컥!)
                             당신은 기적의 확률을 뚫고 자물쇠를 열었습니다! 그안에는 그 동안 그들이 약탈한
                             금은보화가 넘쳐납니다! 적어도 한동안은 굶어 죽을 걱정은 안해도 될 것 같군요.
                             """))
                
                주인공.Money += 200

                while(1):   # 다음 장면 이동

                    print(dedent("""
                             어디로 가시겠습니까?
                             1. 시장 2. 호수 3. 마왕성
                             """))

                    choose = input(">>> ")

                    if "1" in choose or "시장" in choose:
                        return '시장'
                    elif "2" in choose or "호수" in choose:
                        return '호수'
                    elif "3" in choose or "마왕성" in choose:
                        return '마왕성_하층'
                    else:
                        print("다시 선택해 주세요.")

            elif 주인공.old_key == True:        # 열쇠를 구매한 경우
                print(dedent("""
                             (철컥!) 당신은 시장에서 산 낡은 열쇠들로 자물쇠를 열었습니다. 이게 유용히 사용
                             될 줄 누가 알았겠습니까? 그안에는 그 동안 그들이 약탈한 금은보화가 넘쳐납니다! 
                             적어도 한동안은 굶어 죽을 걱정은 안해도 될 것 같군요.
                             """))
                
                주인공.Money += 200

                while(1):

                    print(dedent("""
                             어디로 가시겠습니까?
                             1. 시장 2. 호수 3. 마왕성
                             """))

                    choose = input(">>> ")

                    if "1" in choose or "시장" in choose:
                        return '시장'
                    elif "2" in choose or "호수" in choose:
                        return '호수'
                    elif "3" in choose or "마왕성" in choose:
                        return '마왕성_하층'
                    else:
                        print("다시 선택해 주세요.")

            else:           # 자물쇠 번호 틀린경우
                chance -= 1
                print(f"(덜그럭 덜그럭...) 답이 아닌 듯 하군요. {chance}번 남았습니다.")

        print(dedent("""
                     아쉽게도 상자의 자물쇠는 열리는 기미가 보이지 않습니다. 당신은 아쉬움을 뒤로 한채 숲을 
                     벗어납니다."""))
        
        while(1):

            print(dedent("""
                             어디로 가시겠습니까?
                             1. 시장 2. 호수 3. 마왕성
                             """))

            choose = input(">>> ")

            if "1" in choose or "시장" in choose:
                return '시장'
            elif "2" in choose or "호수" in choose:
                return '호수'
            elif "3" in choose or "마왕성" in choose:
                return '마왕성_하층'
            else:
                print("다시 선택해 주세요.")
                
class Market(stage):

    def enter(self):
        print(dedent(f"""
                     먼 길을 지나 마침내 근방의 도시에 도착했습니다. 성문을 지나서니 시장의 북적거림과
                     활기참입니다. 왠지 이곳에서 좋은 물건을 찾을 것 같다는 생각이 듭니다. 도심의 중심가로 가니
                     거대한 상회가 보입니다. 이곳에서라면 싸고 좋은 물건을 찾을 수 있겠군요. 당신의 직감은 틀리지
                     않았습니다. 상회 안 큰 시장을 둘러보며 물건을 고르고 있습니다.

                     ???: 어서오십쇼. 무엇을 찾고 계신가요? 

                     {주인공.이름}: 당신은...

                     ???: 아, 제 소개를 깜빡했군요. 제 이름은 고르고, 야펜 상회의 점원입니다.

                     {주인공.이름}: 여기선 뭘 살 수 있죠?

                     고르고(야펜 상회 점원): 여기로 오시죠. 

                     그는 당신을 가게로 안내합니다.
                     """))
        
        고르고 = 상인()         # 상인 객체 생성

        return 고르고.sell()           # 판매, 상인 클래스 함수에서 return '숲속'
                                       # sell() 파트에서 return된 값을 사용하려면 return을 해줘야 한다!!!!

class Lake(stage):
    
    def enter(self):

        print(dedent("""
                     깊은 숲속의 밤에서 당신은 불빛을 쫓아 마침내 호수에 다다르게 되었습니다.
                     호수에 가까이 가서 물을 마시던 당신은 괴물들이 무언가 둘러싸 있는걸 보았습니다.
                     자세히 보니 요정 하나가 그들에게 죽어가고 있군요. 그녀를 구할 사람은 현재 당신말고는
                     아무도 없는 것 같군요. 하지만 당신의 몸은 숲속의 전투로 말이 아닙니다. 신중하게 선택하세요.

                     그녀를 돕겠습니까? (Y/N)

                     """))
        
        선택 = input("> ")

        # 요정 돕기 Y
        if 선택 == 'Y' or 선택 == 'y':
            
            print("당신은 불의를 보고 참지 않았습니다! 당신의 살기가 적들의 시선을 돌렸습니다.")
            # 전투

            for _ in range(3):

                해골병사 = 스켈레톤()

                battle_instance = battle(주인공, 해골병사)
                result = battle_instance.enter()

                if result == '사망':
                    return '사망'
            

            print(dedent(f"""
                         당신은 괴물을 처치했습니다.요정은 나무 뒤에 숨어 이 상황을 지켜보다 안전해졌다싶어
                         나무 뒤에서 고개를 내밉니다. 

                         요정: 저기...

                         {주인공.이름}: ?

                         요정: 살려주셔서 감사합니다. 생명의 은인이세요.

                         당신은 멋쩍은 웃음을 지으며 대답합니다.

                         {주인공.이름}: 아닙니다. 용사라면 누구든 이런 상황에선 나섰을거에요.

                         요정: !

                         요정: 용사님이시군요! 마침 저에게 도움이 될만한 것이 있어요.

                         요정은 호수을 향해 알 수 없는 노래를 부릅니다. 노래는 마치 자장가 같이,
                         조용하고 감미로웠습니다. 노래가 끝날즘 호수가 빛나며 잔잔한 수면 아래에서 빛나는
                         물체가 떠오릅니다.

                         {주인공.이름}: 이건...!

                         요정: 이 검은 호수의 성검, 엑스칼리버입니다. 이게 용사님의 여정에 도움이 됬으면
                         좋겠서요.

                         {주인공.이름}: 저는 이걸 받을 자격이...

                         하지만 당신은 섣불리 그 검을 잡지 않았습니다. 단지 그 빛나는 기운에 하염없이 쳐다볼 뿐입니다.

                         요정: 검은 사람이 정하는게 아니라 검 자신이 정하는 겁니다. 용사님 이라면 이 검을 들
                         자격이 있을 거에요.

                         {주인공.이름}: 나는...

                         당신은 기대 반 걱정 반으로 검을 쥡니다. 그러자 검을 휘감던 빛이 당신을 향해 들어옵니다.
                         당신은 이 기운을 온전히 느끼고 있습니다.

                         요정: 검이 용사님을 인정했어요. 이 힘이 앞으로의 여정을 밝혀줬으면 좋겠습니다.

                         요정은 메아리같은 목소리만 남기며 서서히 모습을 감춥니다.
                         당신은 이 검을 허리에 매고 앞으로 향합니다.

                         [아이템 성검을 획득하였습니다! 공격력 +60]
                         """))
            
            # 성검 활성화
            주인공.Exclibur = True

        # 요정 돕기 N
        elif 선택 == 'N' or 선택 == 'n':
            
            print("당신은 제 코가 석자라 지나쳤습니다. 굳이 위험을 감수할 필요는 없죠!")
        
        # 그 외
        else:
            print("잘못 입력하였습니다. 다시 입력해 주세요.")
            return '호수'
        
        
        print(dedent("""
                     당신은 어두운 숲을 헤매다 불 빛을 발견합니다. 낡은 오두막이 보이는군요. 
                     아무도 쓰지 않는 빈집인 이곳을 당신은 하룻밤 휴식처로 쓰고자 합니다.

                     .......

                     창문 사이로 내리쬐는 햇살에 눈을 뜹니다. 다행히 침입의 흔적은 없습니다.
                     당신은 호숫가를 벗어납니다.
                     """))
        
        # 마왕성으로 return
        return '마왕성_하층'

class Castle_Lower(stage):
    
    def enter(self):
        print(dedent(f"""
                     당신은 길고도 험한 길을 가로지르며 마왕성에 도달하였습니다. 성은 높고 어두운 성벽으로 
                     당신을 압도하고 있습니다. 정문에는 많은 수의 마물 병사가 보초를 서고 있습니다.
                     단신으로 그곳을 뚫기엔 벅차보입니다.

                     {주인공.이름}: 분명히 샛길이 있을거야. 
                     
                     당신은 그들의 시선을 피해 성 근처를 둘러봅니다.
                     
                     성벽을 따라 걷다 당신은 어둡고 짙은 문이 보입니다. 하지만 문은 굳게 닫혀있습니다.
                     하지만 열쇠 구멍은 보입니다. 어쩌면 열수 있을지도? 

                     [문을 열어 보시겠습니까? (Y/N)]\n
                     """))
        
        선택 = input("> ")

        # 문따기 시도 O
        if 'Y' in 선택 or 'y' in 선택:

            print(dedent(f"""
                         당신은 열쇠 구멍을 유심히 살펴봅니다. 그리고 요리조리 만져가면 구조를 파악합니다.

                         {주인공.이름}: 좋아. 이제 꽂을 것만 있으면 되겠어.

                         구조를 파악한 당신은 가방에서 문을 열만한 도구를 찾습니다.\n
                         """))
            
            # 열쇠가 있을때 (old_key == True)
            if 주인공.old_key == True:

                return '마왕성_하층_옥상'
                

            # 열쇠가 없을때 (old_key == False)
            elif 주인공.old_key == False:
                
                print(dedent("""
                             가방을 뒤져보지만 열쇠구멍에 넣을만한 마땅한 물건을 찾지 못했습니다. 두꺼운 철제문을
                             뒤로 한채 다시 정문으로 돌아갑니다.
                             """))
                
                return '마왕성_하층_홀'


        # 문따기 시도 X 
        elif 'N' in 선택 or 'n' in 선택:

            print(dedent("""
                         당신은 이곳에서 시간을 낭비하기 싫어 다시 정문으로 돌아갑니다.
                         """))
            
            return '마왕성_하층_홀'

        # 그 외
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            return '마왕성_하층'
        
class Caslte_Lower_Attic(stage):

    def enter(self):

        print(dedent("""
                     가방에서 당신은 이전에 샀던 열쇠 꾸러미를 꺼냅니다. 구멍에 넣고 이리저리 돌려가며
                    문을 열어봅니다.

                     (철컹!)
                    
                     굳게 닫힌 문이 기괴한 소리를 내며 틈을 보입니다. 당신은 그 틈으로 성에 들어갑니다.
                     성의 샛길을 따라걸어 나갑니다. 스산한 공기가 당신 주변을 에워쌉니다. 길의 끝에 도달하니
                     어두운 방에 도착합니다. 아무것도 느껴지지 않습니다.

                     당신은 조심히 근방을 돌아다닙니다. 근처를 조사하던 와중 당신의 발에 무언가 턱하고 
                     걸립니다. 유심히 보니 바닥에 작은 문고리가 있습니다. 문고리를 열어 아래를 보니
                     마물 병사들이 빼곡히 돌아다니고 있음을 확인합니다.
                    
                     그들은 당신의 존재를 알아채지 못했습니다. 누가 천장에 적이 있을거라 생각할까요?
                     당신은 지금이 그들을 기습할 좋은 기회라 생각합니다. 당신은 조심스래 가방을 열어
                     적당히 기습할 물건을 찾습니다.
                     """))
        
        return '마왕성_하층_홀'
         
class Castle_Lower_hall(stage):
    
    def enter(self):

        if 주인공.Bomb == True:

            print(dedent("""
                         가방에는 당신이 거금을 주고 산 폭탄꾸러미가 있었습니다. 당신은 불을 붙혀 적당한
                         타이밍에 아래로 던집니다.

                         (펑!!!! 퍼퍼펑!!!)

                         아래에는 굉음과 함께 적들의 비명소리가 들립니다. 폭발음이 잦아들 때쯤 고요함만이
                         남았습니다.

                         당신은 천장에서 내려와 적이 없음을 확인합니다. 그런데...

                         뒷쪽에서 당신을 향한 적의가 느껴집니다. 당신은 황급히 돌아서 방어합니다.

                         (캉!!)

                         독거미의 큰 앞니가 당신을 향해 덮칩니다. 다행히도 당신은 검으로 거미의 습격을 
                         막아냅니다.

                         (키기긱?! 키긱!)

                         여러개의 붉은 눈과 섬뜩한 소리가 당신을 공포로 몰아세웁니다.
                         """))
            
            타란튤라 = 대왕거미()
            
            return battle(주인공, 타란튤라).enter()

            # 승리 시
            return '마왕성_상층'
        
        else:
            
            print(dedent(f"""
                         가방을 뒤져보았지만 딱히 도움이 될 만한 것을 찾지 못했습니다. 가방을 던질 수 없잖아요?
                         다른 마땅한 수를 찾지 못한 당신은 아래로 뛰어듭니다.
                         
                         {주인공.이름}: 영웅등장!
                         
                         당신은 멋있는 착지와 함께 적들의 시선을 사로잡습니다. 물론 이게 좋은 일은 아니겠죠.
                         당신은 전투를 준비합니다. 과연 당신은 이 전투에서 살아남을 수 있을까요?
                         """))

            for _ in range(4):

                해골병사 = 스켈레톤()

                battle_instance = battle(주인공, 해골병사)
                result = battle_instance.enter()

                if result == '사망':
                    return '사망'

            print(dedent(f"""
                         검으로 갑옷을 베고, 칼로 투구를 쪼개는 당신은 마치 무신이 환생한 것 마냥 적들을 썰어나갑니다.
                         적들을 모두 무찔럿다 생각할 즈음에 천장 구석에서 거미 한마리가 당신을 향해 날카로운 앞니를
                         들이밉니다.
                         
                         {주인공.이름}: 큭...!
                         
                         많은 전투에 피로로 당신은 거미의 기습을 피하지 못했습니다.
                         
                         [ hp -20 ]
                         
                         거미는 앞니를 내세우며 살의를 내뿜습니다. 행운을 빕니다.
                         """))
            
            # 주인공 체력 차감(기습에 의한)
            주인공.hp -= 20

            # 전투
            타란튤라 = 대왕거미()
            
            return battle(주인공, 타란튤라).enter()
            # 승리시 
            return '마왕성_상층'
    
class Castle_Upper(stage):
    
    def enter(self):
        print(dedent(f"""
                     힘겨운 전투로 당신의 몸은 이미 피칠갑되 있습니다. 칼끝에선 전투의 잔혈이 떨어집니다. 
                     당신은 숨을 고르며 눈 앞의 크고 고상한 문양의 철문을 열어재낍니다. 

                     (쿠구구....)

                     거대한 철문이 열리며 어두운 방에 당신은 발을 들입니다. 눈앞에는 내리쬐는 붉은 빛 아래
                     해골로 만들어진 것 같은 옥좌에서 누군가 당신을 유심히 살펴봅니다. 그의 안광은 마치
                     사람을 꿰뚫고 있는듯 합니다. 

                     ???: 흠...

                     마치 흥미가 없다는 듯 당신을 노려봅니다. 온몸을 훓어보며 그가 당신이 쥔 검을 봅니다.

                     ???: 오 그 검은 전설의 칼 아니더냐?

                     {주인공.이름}: 이 칼이 오늘 너를 죽음으로 인도할 것이다!

                     당신은 비장한 목소리와 함께 무기를 부여잡습니다.

                     바알: 하하하!!! 내 소개가 늦었군. 내 이름은 바알 36대 마왕이자, 오늘 그 검의 주인이 될 자이다!

                     우렁찬 소리가 홀을 울립니다. 그의 양손에는 그간 싸워온 전장의 울림이 느껴집니다.
                     지금과는 차원이 다른 존재입니다. 당신은 과연 전설이 될 자격이 있을까요?
                     세계를 구할 영웅의 마지막이 될 지 아니면 전설을 신화로 만들지는 이 전투에 달려
                     있겠군요. 행운을 빕니다.

                     [ Vs 마왕 바알 ]

                     """))
        
        # 전투
        바알 = 마왕()
        return battle(주인공, 바알).enter()

        # 승리 시 
        return '엔딩'

# 엔진
class Engine(object):
    
    def __init__(self, place):
        self.place = place

    def play(self):
        
        On_stage = self.place.prologue()          # 현재 스테이지 = 시작 스테이지
        Ending = self.place.next_stage('엔딩')     # 마지막 스테이지 = 엔딩

        while On_stage != Ending:               # 현재 스테이지가 엔딩이 아니라면
            lastest_stage_name = On_stage.enter()
            On_stage = self.place.next_stage(lastest_stage_name)

        On_stage.enter()                        # 엔딩

# 전투
class battle(object):
    
    # 1. 악당 class 에서 객체 생성
        # ex) 해골병사 = 스켈레톤()

    # 2. battle(객체) 식으로 받기
        # ex) battle(해골병사)

    # 3. 전투창 생성 (보여줘야 할 것 -> 1. 양측 체력 2. 공격/방어/아이템 3. 아이템 누를 시 보유한 아이템 표시) 
        # '-' 한칸당 5의 hp 표시 (/100)

        # | 용사 hp |--------------------|  /   해골병사 hp |--------------------|  | 
        # | 1. 공격                         /   공격력  30                          |
        # | 2. 방어                         /   방어력  20                          |
        # | 3. 가방                         /                                       |


    # 4. 전투 시작(공격 순서 1.용사 2. 악당)
        # 공격을 누를시 
        # 상대 hp 차감 => (내 공격력) - (적 방어력)

        # 방어를 누를시
        # 용사 hp 차감 => (적 공격력) - (내 방어력)
        # 적들은 1/3 확률로 2배의 데미지를 준다! == 방어의 필요성
        # (내 방어력) > (적 공격력) 일 경우 데미지 = 0


    # 4.5 표현 방식
        # if hp 차감에 따라 '-' 칸 줄이기 '-'을 ' '으로 치환 --> 06/29 지금은 일단 숫자로 해결
        # |----------         | (hp 50%)
        # 줄어든 hp 구간 별로 나눠서 if -> 비효율적
        # [차감 hp / 5]개 만큼 ' '으로 치환
        # 숫자가 *7 같은 애매한 숫자의 경우 어떻게? -> 추후 다시 생각

        
    # 5. 패배 시 death 문구 출력

    def __init__(self, 주인공, 적):
        self.주인공 = 주인공
        self.적 = 적
        

    def enter(self):

        print(f"[{self.주인공.이름}] vs [{self.적.이름}]\n")

        # 주인공의 hp 또는 적 hp가 0이 되기 전까지 전투 지속
        while self.주인공.hp > 0 and self.적.hp > 0:

            print(dedent(f"""
                        | 용사 hp                  [{self.주인공.hp}]  /   {self.적.이름} hp                  [{self.적.hp}] 
                        | 1. 공격                         /   공격력  {self.적.Attack_Damage}                           
                        | 2. 방어                         /   방어력  {self.적.Defense_Rate}                          
                        | 3. 가방                         /                                       
                        """))
            
            choose = input("> ")

            Defence_stance = False

            # 공격
            if choose == '1':
                
                print(f"{self.주인공.이름}의 공격!")
                self.적.hp = self.적.hp - (self.주인공.Attack_Damage - self.적.Defense_Rate)
                
                # 적 체력 0 이하로 내려갈 시 0으로 고정
                if self.적.hp < 0:

                    self.적.hp = 0
            # 방어
            elif choose == '2':
                
                print(f"{self.주인공.이름}은 방어 자세를 취했다.")

                # 방어 on --> 상대의 공격을 방어력 만큼 경감 / 공격 시에는 상대의 공격력 만큼 hp 차감
                Defence_stance = True
            
            # 가방
            elif choose == '3':
                print(f"가방 : 1. 물약({self.주인공.Potion}개)\n")

                select = input("> ")
                
                if select == '1':

                    self.주인공.Potion -= 1
                    self.주인공.hp += 30

                    # 회복한 체력은 100을 넘을 수 없다
                    if self.주인공.hp > 100 :
                        self.주인공.hp = 100
            
            # 잘못 입력 시 다시 while 문 첫줄(상태 창)로 이동
            else:
                print("잘못 선택하셨습니다.")
                continue
            
            # 운명 = 8 이상 시 치명타(데미지 2배)
            운명 = randint(1,10)

            print(dedent(f"""
                         운명의 주사위가 굴러갑니다.
                         운명이 가리킨 숫자는 {운명} ! """))
            
            if 운명 > 8 and Defence_stance == True:

                print(f"{self.적.이름}의 강력한 공격!\n")

                print(f"당신은 적의 공격을 방어했다! \n")

                self.주인공.hp = self.주인공.hp - (self.적.Attack_Damage * 2 - self.주인공.Defense_Rate)
            
            elif 운명 > 8 and Defence_stance == False:

                print(f"{self.적.이름}의 강력한 공격!\n")

                self.주인공.hp = self.주인공.hp - (self.적.Attack_Damage * 2)

            elif 운명 < 9 and Defence_stance == True:

                print(f"{self.적.이름}의 공격!\n")

                print(f"당신은 적의 공격을 방어했다! \n")

                self.주인공.hp = self.주인공.hp - (self.적.Attack_Damage - self.주인공.Defense_Rate)

            else:

                print(f"{self.적.이름}의 공격!\n")

                self.주인공.hp = self.주인공.hp - (self.적.Attack_Damage)

            # 전투 패배 시 
            if self.주인공.hp <= 0 :
                
                print("[전투 패배] 당신은 쓰러졌습니다....")
                return '사망'
        
        print("[전투 승리!]")

        if self.적.이름 == '허수아비':
            return '시장'
        
        elif self.적.이름 == '타란튤라':
            return '마왕성_상층'
        
        elif self.적.이름 == '마왕 바알':
            return '엔딩'

# 사망
class death(stage):

    def __init__(self, enemy):
        
        self.enemy = enemy
    
    # 사망 씬 문구 출력
    def enter(self):
        
        Death_Scene = [
        "당신이 지친 순간을 적은 놓치지 않았습니다. 당신의 갑옷의 틈을 찔러넣었습니다.",    # vs 도적
        "괴물을 맞서기엔 당신의 힘은 부족했습니다. 해골들의 휘두름에 사망하였습니다.",      # vs 스켈레톤
        "용사의 칼은 대왕거미의 피부를 뚫기엔 역부족이었습니다. 바위조차 녹이는 독에 몸이 녹습니다",  # vs 대왕거미
        "당신은 최선을 다해 싸웠지만, 마왕을 이기기엔 역부족이었습니다. 당신은 마왕의 힘에 무릎을 꿇습니다." # vs 마왕
    ]
        if self.enemy.이름 == '도적':

            print(Death_Scene[0])

        elif self.enemy.이름 == '스켈레톤':

            print(Death_Scene[1])

        elif self.enemy.이름 == '타란튤라':

            print(Death_Scene[2])

        elif self.enemy.이름 == '마왕 바알':

            print(Death_Scene[3])
        

# 엔딩
class End(stage):

    def enter(self):
        print(f"{주인공.이름}은 모든 역경을 넘어서고 마왕을 무찔렀습니다! 축하합니다!")
        exit(1)
    
class Map(object):

    stages = {
        '마을' : village(),
        '숲속' : forest(),
        '시장' : Market(),
        '상인' : 상인(),
        '호수' : Lake(),
        '마왕성_하층' : Castle_Lower(),
        '마왕성_하층_옥상' : Caslte_Lower_Attic(),
        '마왕성_하층_홀' : Castle_Lower_hall(),
        '마왕성_상층' : Castle_Upper(),
        '사망' : death(),
        '엔딩' : End(),
    } 

    def __init__(self, Starting_Point):
        self.Starting_Point = Starting_Point

    def next_stage(self, stage_name):
        next = Map.stages.get(stage_name)
        return next
    
    def prologue(self):
        return self.next_stage(self.Starting_Point)

# 게임 시작
이름 = input("이름을 입력해 주세요: ")

주인공 = 용사()
주인공.이름 = 이름

# 초기 세팅 값
게임_지도 = Map('마을')         # Starting_Point = '마을'
게임_엔진 = Engine(게임_지도)   # 지도를 엔진에 적용 
게임_엔진.play()                # 게임 시작