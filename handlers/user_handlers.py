from .base import BaseHandler
from models.user_models import User


class UserHandler(BaseHandler):
    model_obj = User


