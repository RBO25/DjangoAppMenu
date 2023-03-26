from django import template
from treemenu.models import Category


register = template.Library()


@register.inclusion_tag('treemenu/Menu.html', takes_context=True)
def draw_menu(context, menu):

    try:
        categorys = Category.objects.filter(menu__name=menu)
        categorys_values = categorys.values()
        primary_category = [category for category in categorys_values.filter(parent=None)]
        selected_category_id = int(context['request'].GET[menu])
        selected_category = categorys.get(id=selected_category_id)
        selected_category_id_list = get_selected_category_id_list(selected_category, primary_category, selected_category_id)

        for category in primary_category:
            if category['id'] in selected_category_id_list:
                category['child_categorys'] = get_child_categorys(categorys_values, category['id'], selected_category_id_list)
        result_dict = {'categorys': primary_category}

    except:
        result_dict = {
            'categorys': [
                category for category in Category.objects.filter(menu__name=menu, parent=None).values()
                ]
            }

    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)

    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring


def get_child_categorys(categorys_values, current_category_id, selected_category_id_list):
    category_list = [category for category in categorys_values.filter(parent_id=current_category_id)]
    for category in category_list:
        if category['id'] in selected_category_id_list:
            category['child_categorys'] = get_child_categorys(categorys_values, category['id'], selected_category_id_list)
    return category_list


def get_selected_category_id_list(parent, primary_category, selected_category_id):
    selected_category_id_list = []

    while parent:
        selected_category_id_list.append(parent.id)
        parent = parent.parent
    if not selected_category_id_list:
        for category in primary_category:
            if category['id'] == selected_category_id:
                selected_category_id_list.append(selected_category_id)
    return selected_category_id_list