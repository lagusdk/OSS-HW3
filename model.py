from pydantic import BaseModel

#정수형인 id, 문자형인 item만 허용하는 pydantic 모델의 예시
class Todo(BaseModel):
    id: int
    item: str