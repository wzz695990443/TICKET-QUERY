from pydantic import BaseModel


class test(BaseModel):
    a:str
    b:str
if __name__ == "__main__":
    a = test(a="a",b="b")
    b = None
    print(b or a.model_dump())