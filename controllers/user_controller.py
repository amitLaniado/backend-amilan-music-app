from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError
from models import UserRegister, UserLogin, UserOut
from services.user_service import arrange_register, arrange_login

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# @router.get("/")
# async def handle_users():
#     # users = await fetch_users()
#     users = await get_users()
#     return users

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def handle_register(user: UserRegister):
    try: 
        print(f"user: {user}")
        new_user_id = arrange_register(user)
        return { "user_id": new_user_id }
    except ValidationError as ve:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=ve.errors())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserOut)
async def handle_login(user: UserLogin):
    try:
        user_id = arrange_login(user)
        return { "user_id": user_id }
    except HTTPException as http_exc:
        # Re-raise HTTP exceptions to maintain their status codes and details
        raise http_exc
    except Exception as e:
        # Handle generic exceptions
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred during login: {str(e)}"
        )
