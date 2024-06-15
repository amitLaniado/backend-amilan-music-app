from fastapi import APIRouter, HTTPException, status
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
        arrange_register(user)
        return { "user_name": user.user_name, "email": user.email }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserOut)
async def handle_login(user: UserLogin):
    try:
        result_user = arrange_login(user)
        if not result_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return result_user
    except HTTPException as http_exc:
        # Re-raise HTTP exceptions to maintain their status codes and details
        raise http_exc
    except Exception as e:
        # Handle generic exceptions
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An error occurred during login: {str(e)}"
        )
