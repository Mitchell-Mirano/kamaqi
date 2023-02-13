PROJECT_EXCEPTIONS=\
"""
from fastapi import HTTPException,status

diferent_passwords_exception=HTTPException(
                             status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Not equal passwords")

credentials_exception = HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Could not validate credentials incorrect email or password",
                        headers={"WWW-Authenticate": "Bearer"})

access_token_exception=HTTPException(
                       status_code=status.HTTP_401_UNAUTHORIZED,
                       detail="Could not validate credentials,Send access token",
                       headers={"WWW-Authenticate": "Bearer"})

refresh_token_exception=HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Could not validate credentials,Send refresh token",
                        headers={"WWW-Authenticate": "Bearer"})

email_password_exception=HTTPException(
                         status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="incorrect email or password",
                         headers={"WWW-Authenticate": "Bearer"})


email_not_found_exception=HTTPException(
                          status_code=status.HTTP_401_UNAUTHORIZED,
                          detail="Email not found",
                          headers={"WWW-Authenticate": "Bearer"})


not_registred_user_exception=HTTPException(
                             status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="The user is not registred",
                             headers={"WWW-Authenticate": "Bearer"})

invalid_code_exception=HTTPException(
                       status_code=status.HTTP_401_UNAUTHORIZED,
                       detail="Incorrect code",
                       headers={"WWW-Authenticate": "Bearer"})

inactive_user_exception=HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail="Inactive user")

registred_user_exception=HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                         detail="The user is already registered")

unauthorized_user_exeption=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                           detail="Unautorized user",
                           headers={"WWW-Authenticate": "Bearer"})
"""