
# TODO: use the class on ansible and playbooks templates
class TemplateController:
    """
    A class to control jinja2 templates to use them 
    in playbooks and asible templates
    """

    def __init__(self, temp, data):
        import yaml
        from jinja2 import Environment, FileSystemLoader
        from django.conf import settings

        self.temp = temp
        self.data = data
        env = Environment(loader=FileSystemLoader(settings.ANSIBLE_TEMP),
                    trim_blocks=True, lstrip_blocks=True)
        temp = env.get_template(temp)
        self.yaml = yaml.full_load(temp.render(data))

    def get_yaml(self):
        """
        Get the rendered template as yaml 'dict'
        """
        return self.yaml

    def write_yaml(self, filename):
        """
        Write the template as yaml file
        """
        import yaml
        with open(filename,'w') as f:
            yaml.dump(self.yaml, f)