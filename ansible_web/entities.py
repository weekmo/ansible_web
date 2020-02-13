class Hosts:
    def __init__(self, file_name):
        from configparser import ConfigParser
        self.file_name = file_name
        self.data =  ConfigParser(allow_no_value=True)
        self.data.read(file_name)
        self.as_dict = {}
        self.as_dict['all'] =set(host for group in self.data.sections() for host in self.data[group])
        self.as_dict.update({group:[host for host in self.data[group]] for group in self.data.sections()})
        
    def add_host(self, group, host):
        #assert self.data.has_section(group), "The hosts' group is not exist!"
        if not self.data.has_section(group):
            self.data.add_section(group)
        self.data[group][host] = None
    
    def add_group(self, grop):
        self.data.add_section(grop)

    def write(self, file_name):
        with open(file_name,'w') as f:
            self.data.write(f)

    def get_hosts(self, group=None):
        if group:
            assert group in self.as_dict, "Group is note exist!"
            return self.as_dict[group]
        return self.as_dict

    def get_groups(self):
        return list(self.as_dict.keys())

    def __str__(self):
        return str(self.as_dict)

"""
class Hosts:
    def __init__(self, file_name):
        self.file_name = file_name
        self.hosts = {}

    def read(self):
        import re
        import socket
        group_name=''
        with open(self.file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('['):
                    group_name = re.sub(r'[\[\]]','',line)
                    self.hosts[group_name] = []
                else:
                    try:
                        socket.inet_aton(line)
                        self.hosts[group_name].append(line)
                    except:
                        pass
        return self.hosts
    
    def write(self, data):
        with open(self.file_name, 'w') as f:
            for k,v in data.items():
                f.write("[{}]\n".format(k))
                for host in v:
                    f.write("{}\n".format(host))
                f.write('\n')
                    
class Playbook:

    def __init__(self, name, hosts=None, vars_file=False, details=None):
        import uuid
        self.name = name
        self.hosts = hosts
        self.details = details
        self.id = uuid.uuid4().hex

        if vars_file:
            self.script[0]['vars_files'] = ['vars']

    def shell_script(self, file_name):
        assert isinstance(file_name, str), "'script_file' must be a string"
        self.script = [{
            'hosts': self.hosts,
            'become': 'yes',
        }]
        self.script[0]['task'] = [{'include': file_name,},]
        
    def write_file(self,dir='playbooks/'):
        from yaml import dump
        with open(dir+self.id+".yml", 'w') as f:
            dump(self.script, f)

    def read_file(self, file_name):
        from yaml import full_load
        with open(file_name, 'r') as f:
            self.script = full_load(f)
        

    def __str__(self):
        return str(self.name)
"""