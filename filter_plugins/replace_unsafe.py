import re

class FilterModule(object):
    def filters(self):
        return {
            'replace_unsafe': self.replace_unsafe
        }
    
    def replace_unsafe(self, value):
        if isinstance(value, dict):
            modified_dict = {}
            for k, v in value.items():
                modified_dict[k] = self.replace_unsafe(v)
            return modified_dict
        elif isinstance(value, list):
            modified_list = []
            for item in value:
                modified_list.append(self.replace_unsafe(item))
            return modified_list
        elif isinstance(value, str):
            # Replace '!unsafe' with '{% raw %}'
            #modified_value = re.sub(r'!unsafe ', '{% raw %} ', value)
            if re.search(r'{{\s*(.*?)\s*}}', value):
               value = '{% raw %} ' + value + ' {% endraw %}'
               return value
            else:
                return value
        else:
            return value