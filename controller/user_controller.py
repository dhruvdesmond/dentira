import http

from fastapi import APIRouter, Depends

# from controller.context_manager import build_request_context


user_router = APIRouter(prefix="/v1/user", tags=["user"])


@user_router.post("/signup", status_code=http.HTTPStatus.CREATED)
async def signup_user():
    """
    Sign up user
    :param _: build_request_context dependency injection handles the request context
    :param user: user details to add
    :return:
    """
    return "post signup"


@user_router.post("/login", status_code=http.HTTPStatus.OK)
async def login_user():
    """
    Login user
    :param _: build_request_context dependency injection handles the request context
    :param user_login_request: user login details
    :return: GenericResponseModel
    """
    return "post login"
