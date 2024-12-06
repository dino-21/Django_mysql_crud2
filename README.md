

step1  - CRUD  -MYSQL 작업 2


![4](https://github.com/user-attachments/assets/56a49a12-b0d0-4404-ae2f-adb0d2d04f0e)




MySQL Python 드라이버 설치
Django가 MySQL과 통신하려면 mysqlclient 패키지가 필요
pip install mysqlclient



설치 확인
pip show mysqlclient





mysql 환경변수 설정 

DROP DATABASE IF EXISTS django_board;
CREATE DATABASE django_board CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


장고셸에서

마이그레이션 파일 생성 Django가 현재 모델(models.py) 상태에 따라 새로운 마이그레이션 파일을 생성
python manage.py makemigrations pybo2



마이그레이션 적용 생성된 마이그레이션 파일을 
MySQL에 적용
python manage.py migrate pybo2






장고셸
python manage.py shell

pybo2 앱에서 Question 모델 임포트
from pybo2.models import Question

현재 시간을 가져오기 위한 임포트
from django.utils.timezone import now

질문 객체 생성
Question.objects.create(subject="Test", content="This is a test.", create_date=now())



MySQL에서
USE django_board;
select * from pybo2_question;
select * from pybo2_answer;



-----------------------------------


DROP DATABASE IF EXISTS django_board;

CREATE DATABASE django_board CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


-- django_board DB 스키마를 만들어라
CREATE DATABASE django_board;

-- 데이터베이스 삭제
DROP DATABASE IF EXISTS django_board;


-- django_board DB를 사용하겠다
USE django_board;

SHOW TABLES;

-- 데이터베이스 확인
show databases;



DESCRIBE pybo2_question;
desc pybo2_answer;

ALTER TABLE pybo2_question DROP COLUMN modify_date;
ALTER TABLE pybo2_answer DROP COLUMN modify_date;


select * from pybo2_question;

select * from pybo2_answer;


