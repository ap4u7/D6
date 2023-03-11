from django import template

register = template.Library()



CENSORED = [
    'ово',
]


@register.filter()
def censor(value):
    if isinstance(value, str):
        for word in CENSORED:
            if word in value:
                value = value.replace(word, word[:1] + '**')
    return value
