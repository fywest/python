class UserData(object):
    def __init__(self,str_id,str_name):
        self.id=str_id
        self._name=str_name

    def __repr__(self):
        return 'ID:{0} Name:{1}'.format(self.id,self._name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def __init__(self,str_id,str_name):
        super().__init__(str_id,str_name)

    def __call__(self):
        print('ID:{0} Name:{1}'.format(self.id,self._name))
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        try:
            if len(value)>3:
                self._name=value
            else:
                raise ValueError

        except:# ValueError
            print('ERROR')


    def __repr__(self):
        return 'ID:{0} Name:{1}'.format(self.id,self._name)
    
    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id,name):
        return '{0}\'s id is {1}'.format(name,id)

if __name__=='__main__':
#user1=UserData(101,'Jack')
#user2=UserData(102,'Louplus')
    user1=NewUser(101,'Jack')
    user1()
    user1.name='Lou'
    user1.name='Jackie'
    user2=NewUser(102,'Louplus')
    print(user1.name)
    print(user2.name)

    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))


