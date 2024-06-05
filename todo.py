from fastapi import APIRouter, Path
from model import Todo  #요청 및 응답 점검: model.py

todo_router = APIRouter()   #API router를 app에 연결

todo_list = []
todo_counter = 0

#새로운 경로: /todo
#새로운 method: post
@todo_router.post("/todo")  
async def add_todo(todo: Todo) -> dict:
    global todo_counter
    todo.id = todo_counter = todo_counter + 1  #id 중복 없애기
    todo_list.append(todo)
    return{
        "msg": "todo added successfully"
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return{
        "todos": todo_list  #list를 그대로 리턴
    }

#경로 parameter
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title = "the ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo" : todo}
    return {"msg" : "todo with supplied ID doesn't exist"}

#삭제 기능 구현
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int=Path(..., title="the ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return{"msg": f"Todo with ID {todo_id}deleted successfully"}
    return{"msg": "Todo with supplied ID doesn't exist"}