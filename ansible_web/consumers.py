import json
from os import path
from datetime import date
from channels.generic.websocket import WebsocketConsumer
from subprocess import Popen, PIPE
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Playbook


class AnsibleConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        pk = int(text_data_json['pk'])
        playbook = get_object_or_404(Playbook, pk=pk)

        process = Popen(f"ansible-playbook {playbook.script}",cwd=settings.MEDIA_ROOT, stdout=PIPE, universal_newlines=True, shell=True)
        with open(path.join(settings.BASE_DIR,f"logs/ansible-log-{date.today()}.log"),'a') as f:
            while True:
                output = process.stdout.readline()
                txt = output.strip()
                f.write(txt+"\n")
                self.send(text_data=json.dumps({
                    'message': str(txt)
                }))
                return_code = process.poll()
                if return_code is not None:
                    for output in process.stdout.readlines():
                        txt = output.strip()
                        f.write(txt+"\n")
                        self.send(text_data=json.dumps({
                            'message': str(txt)
                        }))
                    self.send(text_data=json.dumps({
                        'message': "Process has finished"
                    }))
                    break
