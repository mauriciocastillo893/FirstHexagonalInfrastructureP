from fastapi import APIRouter
from user.application.ListUsersUseCase import ObtenerUsuariosUseCase

get_list_user_router = APIRouter()

def initialize_endpoints(repositorio):
    listUsersUseCase = ObtenerUsuariosUseCase(repositorio)
    
    @get_list_user_router.get("/")
    async def obtener_usuarios():
        return listUsersUseCase.obtener_usuarios()
