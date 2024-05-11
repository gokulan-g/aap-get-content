import re

class FilterModule(object):
    def filters(self):
        return {
            'recursive_modify': self.recursive_modify
        }

    def recursive_modify(self, value):
        if isinstance(value, dict):
            modified_dict = {}
            for k, v in value.items():
                modified_dict[k] = self.recursive_modify(v)
            return modified_dict
        elif isinstance(value, list):
            modified_list = []
            for item in value:
                modified_list.append(self.recursive_modify(item))
            return modified_list
        elif isinstance(value, str):
            # Check if the value contains '{{ ... }}'
            if re.search(r'{{\s*(.*?)\s*}}', value):
                # If it does, wrap the entire value with '{% raw %}' and '{% endraw %}' tags
                modified_value = '{% raw %} ' + value  + ' {% endraw %}'
                return modified_value
            else:
                return value
        else:
            return value
