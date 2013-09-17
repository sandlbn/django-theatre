from django.db.models.base import ModelBase


def build_menu(menu_model):
    if isinstance(menu_model, ModelBase):
        menu = u''
        main_elements = menu_model.objects.filter(
            parent=False
        ).order_by(
            'position'
        )
        for element in main_elements:
            tmp_element, tmp_child_elements = []
            child_elements = menu.models.objects.filter(
                parent_id=element.id
            ).order_by(
                'position'
            )
            if child_elements.count() > 0:
                tmp_child_elements.append(
                    '<li class="dropdown"> \
                    <a class="dropdown-toggle" \
                    data-toggle="dropdown" \
                    href="#">'
                )
                tmp_child_elements.append(element.name)
                tmp_child_elements.append(
                    '<b class="caret"></b> \
                    </a><ul class="dropdown-menu">'
                )

                for child_element in child_elements:
                    tmp_child_elements.append(
                        u''.join([
                            '<li><a href="',
                            child_element.get_absolute_url,
                            '">',
                            child_element.get_name,
                            '</li>'
                        ])
                    )
                tmp_child_elements.append('</ul></li>')
            menu.join(tmp_child_elements)
        else:

            menu.join(['<li><a href="',
                       element.get_absolute_url,
                       '">',
                       element.name,
                       '</li>'
                       ])
        return menu
