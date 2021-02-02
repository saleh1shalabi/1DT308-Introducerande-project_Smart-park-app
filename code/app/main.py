from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
import time
from kivy.lang.builder import Builder
from kivymd.toast import toast
from datetime import datetime
import paho.mqtt.client as mqtt
from conect import run as sa
from conect import client
from kivy.properties import StringProperty




screens = """

ScreenManager:
    HomeScreen:
    CityScreen:
    AllPaScreen:
    AdminScreen:
    InpScreen:
    ParkScreen:
    AboutScreen:

<AdminScreen>:
    id: admin
    name: 'admin'
    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Choose a city'
        elevation: 10
    
    MDFloatLayout:
        
        
        padding: 50, 0, 0 , 100
        spacing: dp(10)


        MDFillRoundFlatIconButton:
            text: 'Back'
            pos_hint: {'center_x':0.1, 'center_y':0.1}
            icon: 'arrow-collapse-left'
            on_release:
                root.manager.current = 'home'
                root.manager.transition.direction = "up"


        MDTextField:
            id: enter_pass
            icon_right: "account-box"
            hint_text: "Enter Password"
            password: True
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            size_hint: 0.5, 0.1

        MDFillRoundFlatIconButton:
            id: pass
            text: 'Enter'
            pos_hint: {'center_x':0.5, 'center_y':0.4}
            icon: 'arrow-right'
            on_release:
                root.pass_check()
                    
<InpScreen>:
    id: inp
    name: 'inp'
    MDToolbar:
        pos_hint: {"top": 1}
        title: 'Enter New Numbers'
        elevation: 10
    
    MDFloatLayout:
        
        padding: 50, 0, 0 , 100
        spacing: dp(10)
        




        MDFillRoundFlatIconButton:
            text: 'Done'
            pos_hint: {'center_x':0.1, 'center_y':0.1}
            icon: 'arrow-collapse-left'
            on_release:
                root.manager.current = 'home'
                root.manager.transition.direction = "down"


        MDTextField:
            id: places
            icon_right: "parking"
            hint_text: "Availble Places"
            pos_hint: {'center_x':0.5, 'center_y':0.3}
            size_hint: 0.5, 0.1
        MDTextField:
            id: parked
            icon_right: "car"
            hint_text: "Parked Cars"
            pos_hint: {'center_x':0.5, 'center_y':0.4}
            size_hint: 0.5, 0.1
        MDFillRoundFlatIconButton:
            id: pass
            text: 'Enter'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            icon: 'arrow-right'
            on_release:
                root.new_val()
    
<HomeScreen>:
    id: home
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'

        MDToolbar:
            
            pos_hint: {"top": 1}
            title: 'Your Best Park'
            elevation: 10

        MDFloatLayout:
            padding: 0,0,0,60
            spacing: dp(10)
            MDLabel:
                text: 'PARK'
                font_size: "32sp"

                halign: 'center'
                pos_hint: {'center_x':0.5, 'center_y':0.9}
                bold: True
                padding: 10, 10
                spacing: dp(10)
            FitImage:
                source: "unnamed.png"
                size_hint_x: None
                size_hint_y: None
                pos_hint: {'center_x':0.5, 'center_y':0.75}


                halign: 'center'
                valign: 'middle'


            MDFillRoundFlatIconButton:
                text: 'Start'
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                icon: 'parking'
                on_release: 
                    root.manager.current = 'city'
                    root.manager.transition.direction = "right"
            
            MDFillRoundFlatIconButton:
                text: 'Adminstrator'
                pos_hint: {'center_x':0.5, 'center_y':0.4}
                icon: 'account'

                on_release: 
                    root.manager.current = 'admin'
                    root.manager.transition.direction = "down"


            MDFillRoundFlatIconButton:
                text: 'About Us'
                pos_hint: {'center_x':0.5, 'center_y':0.3}
                icon: 'information'

                on_release: 
                    root.manager.current = 'about'
                    root.manager.transition.direction = "right"


            MDFillRoundFlatIconButton:
                text: 'Close App'
                pos_hint: {'center_x':0.5, 'center_y':0.1}
                icon: 'close'
                on_release: root.ss()
        
<CityScreen>:
    id: city
    name: 'city'
    
    MDBoxLayout:
        orientation: 'vertical'

        padding: 0, 0, 0 , 50
        spacing: dp(10)

        MDToolbar:
            pos_hint: {"top": 1}
            title: 'Choose a parking'
            elevation: 10
            
        MDBoxLayout:
            
            padding: 10, 0, 0 , 50
            spacing: dp(10)

            
            
            MDFloatLayout:
                padding: 10,0,0,10  

                MDLabel:
                    text: 'City:'
                    
                    pos_hint: {'x':0.3, 'y':0.2}
                    font_size: "24sp"

                MDIcon:
                    
                    icon: "city-variant-outline"
                    font_size: "32sp"
                    pos_hint: {'x':0.05, 'center_y':0.7}
                
                
                
                
                ScrollView:
                    pos_hint: {"x": 0.5, 'y':-0.3}
                    MDList:
                        spacing: 20, 20
                        MDFlatButton:
                            text: "Kalmar"
                            on_release:
                                root.manager.current = 'all_pa'
                                root.manager.transition.direction = "up"    
                                        
                        MDFlatButton:
                            text: "Göteborg"
                            on_release:
                                root.show()                    
                        MDFlatButton:
                            text: "Örebro"
                            on_release:
                                root.show()
                        MDFlatButton:
                            text: "Stockholm"
                            on_release:
                                root.show()
                        MDFlatButton:
                            text: "Karlskrona"
                            on_release:
                                root.show()

                        MDFlatButton:
                            text: "Växjö"
                            on_release:
                                root.show()
        MDFillRoundFlatIconButton:
            text: 'Back'
            pos_hint: {'center_x':0.1}
            icon: 'arrow-collapse-left'
            on_release:
                root.manager.current = 'home'
                root.manager.transition.direction = "left"

<AllPaScreen>:
    id: all_pa
    name: 'all_pa'

   

    MDBoxLayout:
        orientation: 'vertical'
        
        padding: 0, 0, 0 , 10
        spacing: dp(10)

        MDToolbar:
            pos_hint: {"top": 1}
            title: 'Choose a parking'
            elevation: 10
        MDBoxLayout:
            orientation: 'vertical'
        
            padding: 10, 0, 0 , 10
            spacing: dp(10)
       
        
            MDFloatLayout:
                padding: 10, 0, 0 , 0
                spacing: dp(10)
                
                
                MDIcon:
                    
                    icon: "parking"
                    font_size: "32sp"
                    pos_hint: {'x':0.1, 'center_y':0.7}
                
                
                MDLabel:
                    text: 'Park:'
                    
                    pos_hint: {'x':0.3, 'y':0.2}
                    font_size: "24sp"
                
                ScrollView:

                    pos_hint: {"x": 0.5, 'y':-0.3}
                    MDList:
                        spacing: 20
                        MDFlatButton:
                            text: "Cellgraven"
                            id: cell
                            on_release:
                                root.s()
                                root.manager.current = 'park'
                                root.manager.transition.direction = "right"
                                    
                        MDFlatButton:
                            text: "LNU"
                            on_release:
                                root.show()                    
                        MDFlatButton:
                            text: "Centrum"
                            on_release:
                                root.show()
                        MDFlatButton:
                            text: "Giraffen"
                            on_release:
                                root.show()
            MDFillRoundFlatIconButton:
                
                text: 'Back'
                pos_hint: {'center_x':0.1, 'center_y':0.1}
                icon: 'arrow-collapse-left'
                on_release:
                    root.manager.current = 'city'
                    root.manager.transition.direction = "up"
<ParkScreen>:
    id: park
    name: 'park'
    


    MDBoxLayout:
        orientation: 'vertical'
        padding: 0, 0, 0 , 100
        spacing: dp(10)
        font_size: "32sp"

        MDToolbar:
            pos_hint: {"top": 1}
            title: 'Kalmar - Cellgraven'
            elevation: 10
        
        MDBoxLayout:
            orientation: 'horizontal'
            
            padding: 50, 100, 0, 0
            
            MDIcon:
                icon: "update"
            
            MDIcon:

                icon: "car-side"
            MDIcon:
                
                icon: "parking"

        MDBoxLayout:

            padding: 50, 0, 0, 100
            
            orientation: 'horizontal'
            MDLabel:
                id: tidss
                text: root.tid(0)

            
            MDLabel:
                id: cars
                text: "cars"
           
            MDLabel:
                id: ledig
                text: "ledig"
            

        
        MDFillRoundFlatIconButton:
            text: 'update'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            icon: 'arrow-collapse-left'
            on_release: root.update()
        MDFillRoundFlatIconButton:
            text: 'Back'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            icon: 'arrow-collapse-left'
            on_release:
                root.manager.current = 'all_pa'
                root.manager.transition.direction = "down"

<AboutScreen>:
    
    id: about
    name: 'about'

   
         
    MDBoxLayout:
        orientation: 'vertical'
        padding: 0,0,0,10
        
        MDToolbar:
            
            pos_hint: {"top": 1}
            title: "About Us"
            elevation: 10
        MDBoxLayout:
            orientation: 'vertical'
            padding: 10,10,50,0
            


        
            ScrollView:
                spacing: dp(20)
                do_scroll_x: False
                do_scroll_y: True
                pos_hint: {"x": 0.05, 'center_y':0.5}
                
                
                MDList:

                    MDLabel:
                        
                        text: "Saleh"
                        font_size: "24"
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                        bold: True

                    MDLabel:
                        
                        text: root.Saleh
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None    
                    
                    
                    MDLabel:
                        text: "Emelie"
                        font_size: "24"
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                        bold: True

                    MDLabel:

                        text: root.Emilie
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                    
                    MDLabel:
                        font_size: "24"
                        text: "Elin"
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None 
                        bold: True
        
                    MDLabel:
                        text: root.Elin
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None 

                    MDLabel:
                        text: "Om Produkten"
                        font_size: "24"
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                        bold: True

                    MDLabel:
                        text: root.ab_ou_t
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                        padding_bottom: 20

                  
                    MDLabel:
                        
                        text: "Snygg på Utsidan!"
                        font_size: "36"
                        bold: True

                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None

                    Image:
                        padding_right: 10
                        source: "2.jpg"
                        pos_hint: {"center_x": 0.5, 'center_y':1}
                        size_hint_x: 0.9
                        size_hint_y: None
                        size: self.width, 500
                        


                    MDLabel:
                        text: "Inte Så Mycket på InSidan"
                        font_size: "36"
                        bold: True
                        halign: 'center'
                        valign: 'middle'
                        text_size: self.width, None
                        height: self.texture_size[1]
                        size_hint_x: 0.9
                        size_hint_y: None
                    Image:
                        padding_right: 10
                        source: "3.jpg"
                        pos_hint: {"center_x": 0.5, 'center_y':1}
                        size_hint_x: 0.9
                        size_hint_y: None
                        size: self.width, 500
                    

                    

                        

                        

                        


        MDBoxLayout:
            orientation: 'vertical'
            padding: 40,0,0,10 
            size_hint: 1, 0.1
            MDFillRoundFlatIconButton:
                
                text: 'Back'
                pos_hint: {'center_x':0.1, 'center_y':1}
                icon: 'arrow-collapse-left'
                on_release:
                    root.manager.current = 'home'
                    root.manager.transition.direction = "left"
"""



class HomeScreen(Screen):
    client = mqtt.Client()
    # exit function
    def ss(self):
        self.client.loop_stop()
        exit()
    

class CityScreen(Screen):
    # shows when a a city is chosen if not kalmar
    def show(self):
        toast("Not yet avilable")
        


class AllPaScreen(Screen):
    # shown when other park is chosen
    def show(self):
        toast("Not yet avilable")
    
    def s(self):    # get data from server befor going in 
        ParkScreen().update()


class InpScreen(Screen):


    def new_val(self):
        " function that publish new value of CARS ans PLACES to the main device so it can update "

        park = self.ids.parked.text 
        plac = self.ids.places.text
        

        if park == "" or plac == "":  
            toast("Pleas Both Values")
            self.ids.parked.text = ""
            self.ids.places.text = ""

        elif not park.isdigit() or not plac.isdigit():
            toast("Pleas Enter correct Values")
            self.ids.parked.text = ""
            self.ids.places.text = ""

        elif int(park) < 0 or int(plac) <= 0: 
            toast("Pleas Enter correct Values")
            self.ids.parked.text = ""
            self.ids.places.text = ""

        else:
            # puplishing new values 
            result1 = client.publish("saleh_shalabi/feeds/reset_Cars",park)
            stat= result1[0]
            while stat != 0: # check that it sended 
                result1 = client.publish("saleh_shalabi/feeds/reset_Cars",park)

            result2 = client.publish("saleh_shalabi/feeds/reset_Plac",plac)
            stat= result2[0]
            while stat != 0:
                result2 = client.publish("saleh_shalabi/feeds/reset_Plac",plac)

            self.ids.parked.text = ""
            self.ids.places.text = ""
            toast("New Info Sented")




            


class AdminScreen(Screen):

    def pass_check(self): # password Check when admin wants to change values 
        
        all_pas = "This-is-park"  # THE PASSWORD 
        pas = self.ids.enter_pass.text
        if pas != all_pas:
            toast("Not Correct")
            self.ids.enter_pass.text = ""
        else:
            toast("Correct!")
            self.ids.enter_pass.text = ""
            self.manager.current = "inp"

          



class ParkScreen(Screen):
 
    

    def im(self, dt):
        # cars number updater
        from conect import Cars_TOT
        x = Cars_TOT
        if x != str(Cars_TOT):
            x = "No info yet"

        return x


    def LM(self, dt):
        # place num updater
        from conect import Places
        x = Places
        if x != str(Places):
            x = "No info yet"
        return x


    def tid(self,dt):
        # time updater
        now = datetime.now()
        curr_tid = now.strftime("%H:%M")
    
        return str(curr_tid)
    
    


    def update(self):
        # when update button bushed
        from conect import Msg_S_U
        Msg_S_U() # send update to main device
        time.sleep(0.1) # wait befor getting new values
        self.ids.cars.text = f"latest update:\n{self.im(0)}"
        self.ids.ledig.text = f"latest update:\n{self.LM(0)}"
        self.ids.tidss.text = f"latest update:\n    {self.tid(0)}"
    

class AboutScreen(Screen):
    from abou import Emilie, Elin, Saleh, ab_ou_t





sm = ScreenManager()
sm.add_widget(HomeScreen(name= 'home'))
sm.add_widget(CityScreen(name='city'))
sm.add_widget(AllPaScreen(name='all_pa'))
sm.add_widget(ParkScreen(name='park'))
sm.add_widget(AboutScreen(name='about'))
sm.add_widget(AboutScreen(name='admin'))
sm.add_widget(InpScreen(name='inp'))







class MyApp(MDApp):
    title = "Your Best Parking App"
   

    def build(self):
        # bulding the app
        screen = Builder.load_string(screens)
        
        return screen  






sa() # run mqtt server



MyApp().run() # run app





