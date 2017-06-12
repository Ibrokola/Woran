from django import template
from allauth.account.forms import LoginForm, SignupForm

register = template.Library()

@register.inclusion_tag('home.html')
def signup_form_tag(current_page=None):
    return {'signupform': SignupForm(),
            'redirect_to': current_page}