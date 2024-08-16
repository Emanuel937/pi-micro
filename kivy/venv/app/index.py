from kivy.lang import Builder

from kivymd.app import MDApp


class Example(MDApp):
    def build(self):
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: "numeric-10"

            MDLabel:
                text: 'Screen 1'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'twitter'

            MDLabel:
                text: 'Screen 2'
                halign: 'center'
'''
        )


Example().run()