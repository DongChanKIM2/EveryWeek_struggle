# 이름 Random하게 나와주는 라이브러리
from faker import Faker

#faker.__init__() 과 동일한 의미로 초기 실행
faker = Faker()

# name, address는 faker내에서 임의의 이름, 주소 출력
print(faker.name(), faker.address())

# 2번 정답
# 라이브러리를 호출 하기 위한 코드이다
# Faker는 클라스, fake는 인스턴스이다
# name은 faker의 메서드이다.

# Localization and seeding(class와 instance에 각각 seed 기능 존재)
faker = Faker('ko_KR')
faker.seed_instance(4321)
print(faker.name())
faker2 = Faker('ko_KR')
print(faker2.name())


# print(faker_ko.name(), faker_ko.address())

#3
# class MyFaker:
#     def __init__(self, locale):
#         pass

#4. Faker 본인을 호출하기 때문에 seed는 classmethod
#Faker.seed(4321)

