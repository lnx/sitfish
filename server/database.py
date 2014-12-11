#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import datetime

from mongoengine import *

DB_NAME = 'vox'
DB_HOST = 'ec2-54-64-100-152.ap-northeast-1.compute.amazonaws.com'
DB_PORT = 27017
connect(db=DB_NAME, host=DB_HOST, port=DB_PORT)

ACTIVATION_CODE_LEN = 10

class User(Document):

    uid = StringField(primary_key=True)
    name = StringField(default='', required=True)
    email = StringField(default='', required=True, unique=True)
    her = StringField(default='')
    reg_time = DateTimeField(default=datetime.datetime.now())
    activation = BooleanField(default=False)
    activation_code = StringField(default=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(ACTIVATION_CODE_LEN)))
    access_token = StringField(default='')

    def __str__(self):
        return '<%s, %s, %s>' % (self.uid, self.name, self.email)

    def json(self):
        return {'uid': self.uid, 'name': self.name, 'email': self.email, 'her': self.her}



if __name__ == '__main__':
    for u in User.objects():
        print(u)

