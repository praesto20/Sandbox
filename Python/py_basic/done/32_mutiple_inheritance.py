# 다중 상속

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # 괄호 안에 상속받을 클래스 Unit 입력
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다. " + f"체력 : {self.hp}, 공격력 : {self.damage}")

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격 합니다. 공격력 : {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력 = {self.hp}")
        if self.hp <= 0 :
            print(f"{self.name} : 파괴되었습니다.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. 속도 : {self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable): # 두 클래스를 상속받음
    def __init__(self, name ,hp ,damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200 ,6, 5)
valkyrie.fly(valkyrie.name, "3시")
