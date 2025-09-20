from fastapi import APIRouter, status

from src.api.user.dependencies import UserServiceDep
from src.api.user.schemas import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    summary='Создание пользователя',
    response_model=UserResponseSchema,
)
async def create_user(
    request_data: UserCreateSchema,
    service: UserServiceDep,
):
    return await service.create_user(request_data)


@router.get(
    '/{user_id}/',
    status_code=status.HTTP_200_OK,
    summary='Получение пользователя по идентификатору',
    response_model=UserResponseSchema,
)
async def get_user(
    user_id: int,
    service: UserServiceDep,
):
    return await service.get_user_by_id(user_id)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    summary='Получение списка пользователей',
    response_model=list[UserResponseSchema],
)
async def get_users(service: UserServiceDep):
    return await service.get_users()


@router.patch(
    '/{user_id}/',
    status_code=status.HTTP_200_OK,
    summary='Обновление данных пользователя',
    response_model=UserResponseSchema,
)
async def update_user(
    user_id: int,
    request_data: UserUpdateSchema,
    service: UserServiceDep,
):
    return await service.update_user(user_id, request_data)


@router.delete(
    '/{user_id}/',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Удаление пользователя',
)
async def delete_user(
    user_id: int,
    service: UserServiceDep,
):
    return await service.delete_user(user_id)
