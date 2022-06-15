#모듈과 파일입출력 예제 연습

# 1. 모듈

from exmodule import modulesum as ad
i = ad( 3,4 )
print(i)

# 2. 파일 입출력
# 읽기
f = open("C:\\python_csvdata\\test3.csv","r",encoding ="utf-8")
while True:
    contents = f.readline() #한줄을 읽어낸다
    if (contents == ""): #내용이 없으면 반복문 종료
        break
    contents2 = contents.split(",")
    num = contents2[1] #이름만
    name = contents2[24] #주소만
    print(num + " , " + name)
f.close()

#쓰기
f = open("C:\\python_csvdata\\test2.txt","w")

f.writelines("안녕하세요.")

f.close()

#클래스 생성자

class Student:
    name = ""
    age = 0
    status = ""
    
    def __init__(self,name,age,status):
        self.name = name
        self.age = age
        self.status = status
        
    def change_status(self, status):
        self.status = status


#상속

class EngStudent(Student):
    room = 201
    studyclass = "python"
    
    def __init__(self,name,age,status):
        super(EngStudent, self).__init__(name,age,status)
