from fastapi import APIRouter

# from sqlalchemy.orm import Session
# from app.schemas.user import UserCreate
# from app.services.user_service import UserService  # Import the service
# from app.db import get_db

router = APIRouter()


@router.get('/')
def read_root() -> dict[str, str]:
    return {'message': 'Hello World'}


# @router.post("/users/", response_model=UserCreate)
# def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
#     Use the UserService to handle business logic
# user = UserService.get_user_by_email(db, user_in.email)
# if user:
#     raise HTTPException(status_code=400, detail="Email already registered")
#
# return UserService.create_user(db, user_in)
