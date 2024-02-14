from django.shortcuts import render, redirect
from ..database import UserDatabase
from ..decorators import userValidator
from .base import Base
from pprint import pprint

database = UserDatabase()

class User(Base):
    @userValidator
    def profile(self, request, user, context, **kwargs):
        GET = request.GET
        user_list_keywords = GET.get("keywords", "")
        user_list_page = GET.get("page", 1)
        user_list = database.get_list(data=user, keywords=user_list_keywords)
        paginated_list, user_list_pages = self.paginate(data=user_list, page=user_list_page)

        context['user_list_keywords'] = user_list_keywords
        context['user_list'] = paginated_list
        context['user_list_page'] = user_list_page
        context['user_list_pages'] = user_list_pages

        return self.root(request=request, context=context, template="pages/user/profile.html")
        