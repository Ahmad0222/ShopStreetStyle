from django import template

register = template.Library()


@register.filter
def all_numbers(item):
  data_list = []
  if isinstance(item, dict):
    for item in item:
      for foot_size in item.list():  # this will raise an exception
        data_list.append(foot_size)
    return data_list
