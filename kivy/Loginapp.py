import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
#-----------------------------------
class Login(App):
    Window.size=(300,500)
    def build(self):
        self.name1=Label(text='[b]please enter your Firstname:[/b]',markup=True)
        self.txt1=TextInput(multiline=False)
        self.family=Label(text='[b]please enter your Lastname:[/b]',markup=True)
        self.txt2=TextInput(multiline=False)
        self.country=Label(text='[b]please enter your Country:[/b]',markup=True)
        self.txt3=TextInput(multiline=False)
        self.btn=Button(background_color=[1,0,0,1],text='Submit')
        self.ckb=CheckBox(active=True)
        self.box=BoxLayout(orientation= 'vertical')
        self.box.add_widget(self.name1)
        self.box.add_widget(self.txt1)
        self.box.add_widget(self.family)
        self.box.add_widget(self.txt2)
        self.box.add_widget(self.country)
        self.box.add_widget(self.txt3)
        self.box.add_widget(self.btn)
        self.box.add_widget(self.ckb)
        self.btn.bind(on_press=self.press)
        return self.box
    def press(self,e):
        if (self.txt1.text !='') and (self.txt2.text !='') and (self.txt3.text !=''):
            print(f'he is {self.txt1.text}{self.txt2.text} and he comes from{self.txt3.text}')
            self.btn.disabled=True
            self.btn.text='Thank you!'
            self.txt1.text=''
            self.txt2.text=''
            self.txt3.text=''
        else:
            print('Error')
if __name__=='__main__':
    Login().run()
