from typing import Annotated

from fastapi import Depends

from src.api.v1.user.repository import UserRepository
from src.api.v1.user.service import UserService
from src.common.dependencies import SessionDep
from src.models import User


async def get_user_repository(session: SessionDep) -> UserRepository:
    return UserRepository(session, User)


UserRepositoryDep = Annotated[UserRepository, Depends(get_user_repository)]


async def get_user_service(repository: UserRepositoryDep):
    return UserService(repository)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
