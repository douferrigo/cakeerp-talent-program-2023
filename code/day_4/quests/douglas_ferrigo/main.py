from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)

@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]

@app.get("/api/cursos/{id_curso}")
def find_id(db: Session = Depends(get_db), id_curso = int):
    curso = CursoRepository.find_by_id(db, id_curso)
    if curso:
        return CursoResponse.from_orm(curso)
    else:
        return {"message" : "Curso não encontrado"}
    
@app.delete("/api/cursos/{id_curso}")
def delete_id(db: Session = Depends(get_db), id_curso = int):
    curso = CursoRepository.find_by_id(db, id_curso)
    if curso:
        CursoRepository.delete_by_id(db, id_curso)
        return {"message": f"Curso de ID {id_curso} deletado com sucesso"}
    else:
        return {"message" : "Curso não encontrado"}
    
@app.patch("/api/cursos/{id_curso}")
def update_id(request: CursoRequest, db: Session = Depends(get_db),  id_curso = int):
    curso = CursoRepository.find_by_id(db, id_curso)
    if curso:
        curso.titulo = request.titulo
        curso.descricao = request.descricao
        curso.carga_horaria = request.carga_horaria
        curso.qtd_exercicios = request.qtd_exercicios
        Session.commit(db)
        return {"message": f"Curso de ID {id_curso} modificado com sucesso"}
    else:
        return {"message" : "Curso não encontrado"}
    
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
