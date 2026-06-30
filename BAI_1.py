from fastapi import FastAPI
app = FastAPI()
students = ["An" , "Binh" , "Cuong"]
@app.get("/Students")
def get_student():
    return students



#/getStudents phải sửa lại thành /Students bời vì vi phạm quy tắc rest
#/ JSON không nên trả về dữ liệu string , trả về dict / list , vi phạm quy chuẩn và 
#thực hành không tốt