### 0615 DRF 과제

## 1. args, kwargs를 사용하는 예제 코드 짜보기

<img width="800" src="https://user-images.githubusercontent.com/104494448/173812069-0dfa0d6e-fc63-4fa3-bd71-50e94c3b912b.png">

## 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기

    Immutable한 객체의 자료형엔 숫자형,bool형,문자형, 튜플과 유니코드가 있고,

    Mutable한 객체의 자료형에는 리스트형, 딕셔너리형 등이 있다. 그리고 따로 생성한 클래스도 일반적으로 Mutable한 객체다.

    Immutable한 객체는 "값"을 집어 넣지만, mutable한 객체는 "주소"를 집어 넣는다.

    아래의 코드를 보고 immutable과 mutable 의 차이를 설명해주겠따.

    mutable에 관한 예제이다.

    a = ["oh shit"]  

    b = a

    b.append("Finally..")

    print(a)

    print(b)

    이렇게 출력이 될 것으로 예상이 될 것이다 

    print(a)는 ["oh shit"]

    print(b)는 ["oh shit", "Finally..")

    하지만 실제로 출력된 값은,

    print(a) ["oh shit", "Finally..")

    print(b) ["oh shit", "Finally..")으로 똑같다.

    이게 왜이러냐면~~

    b는 위의 리스트형태의 값을 갖고 있는 mutable한 객체인 a와 주소값을 공유하기 때문에,

    b의 값도 "oh shit" 가 된다   *b = ["oh, shit"]

    쉽게 설명하자면 a = ['oh shit'] = b 라고 보면 된다.

    메모리에 a와 b의 값이 지정된다고 보면 된다.

    장고의 deepcopy()라는 함수를 이용하면, 뮤터블한 객체도 주소값을 복사하지 않고 값으로 보낼 수 있다.


## 3. DB Field에서 사용되는 Key 종류와 특징 서술하기

<img width="752" alt="Screen Shot 2022-06-15 at 8 04 54 PM" src="https://user-images.githubusercontent.com/104494448/173813171-d889ef30-7724-4d27-873e-6d3913fb9bc6.png">
<img width="650" alt="Screen Shot 2022-06-15 at 8 04 39 PM" src="https://user-images.githubusercontent.com/104494448/173813287-0152945a-448a-42d8-b56d-0c4c58696500.png">
<img width="702" alt="Screen Shot 2022-06-15 at 8 04 30 PM" src="https://user-images.githubusercontent.com/104494448/173813298-6a86faae-be0a-4781-9794-d902f7636a21.png">
<img width="716" alt="Screen Shot 2022-06-15 at 8 04 15 PM" src="https://user-images.githubusercontent.com/104494448/173813312-d4a77426-2e1d-494c-a99b-40e62693f960.png">


## 4. django에서 queryset과 object는 어떻게 다른지 서술하기

     Python object 사전적 정의
     - object는 어떠한 속성값과 행동을 가지고 있는 데이터입니다. 
     - object는 실제로 존재하는 모든 것들입니다.
     - object는 함수와 변수(데이터)를 함께 묶는 방법의 하나입니다.
     - 프로그래밍 용어로 파이썬은 객체지향적(object-oriented)라고 표현합니다. 
       이는 파이썬 내에서 객체를 사용하는 것이 가능하다는 뜻입니다.
     - 속성 (attribute) : 객체의 특징 또는 객체에 관해 알고 있는 사항. 숫자, 문자열 등과 
                          같은 정보로 구성되어 있습니다. 즉 속성은 객체 안에 포함된 
                          변수(데이터)입니다.
     - 메서드 (method) : 파이썬에서 행동 또는 객체에 대해, 객체를 통해 할 수 있는 것. 
                         어떤 일을 하기 위해 호출(call)할 수 있는 코드 덩어리입니다. 
                         즉 메서드는 객체 안에 포함된 함수입니다. 
     - 객체 = 속성(변수) + 메서드(함수) : 그러므로 객체는 어떤 것에 대한 속성과 메서드를 
                                         함께 모으는 한 가지 방법입니다. 여기서 속성은 
                                         정보고, 메서드는 행동입니다.

     Django object란?
     - DB는 기본적으로 테이블로 이루어져 있으며, 필드와 레코드가 존재한다.
     - 레코드는 Django에서 object라는 이름으로 사용된다.
     - 즉, 레코드란 데이터베이스에 저장 되는 값들을 지칭하는 것

     Django queryset란?
     - queryset은 전달받은 모델의 object 목록을 말한다. 
     - DB로부터 데이터를 읽고 필터를 걸거나 정렬등을 할 수 있다. 
     - 리스트와 구조는 같지만 파이썬 기본 자료구조가 아니기에 읽고 쓰기 위해서는 자료형 
       변환을 해줘야 한다.
     - 쿼리셋은 데이터베이스의 여러 레코드(row)를 나타낸다.
