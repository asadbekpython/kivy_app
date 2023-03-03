from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.switch import Switch
from kivy_garden.mapview import MapView, MapMarkerPopup

class Basic(BoxLayout):
    def __init__(self, **kwargs):
        super(Basic, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.spacing = 15
        self.padding = 100

        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)
        
    def calls(self, instance):
        """Рисует экран экстренных вызовов"""
        # Кнопка для выхода
        self.back_button_1 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (350, 50))
        self.back_button_1.bind(on_press = self.basic_1)

        # Создание кнопок
        self.but_1 = Button(text = '112 - Департамент по чрезвычайным ситуациям', background_color = [0, 0, 0, 0])
        self.but_2 = Button(text = '101 - Служба пожаротушения', background_color = [0, 0, 0, 0])
        self.but_3 = Button(text = '102 - Полиция', background_color = [0, 0, 0, 0])
        self.but_4 = Button(text = '103 - Скорая медицинская помощь', background_color = [0, 0, 0, 0])
        self.but_5 = Button(text = '104 - Аварийная служба газа', background_color = [0, 0, 0, 0])
        self.but_6 = Button(text = '110 - Антитеррористическая служба', background_color = [0, 0, 0, 0])
        self.but_7 = Button(text = '109 - Служба спасения', background_color = [0, 0, 0, 0])
        self.but_8 = Button(text = '115 - Телефон доверия в сложных жизненных ситуациях', background_color = [0, 0, 0, 0])

        # Добавление кнопок
        self.add_widget(self.back_button_1)
        self.add_widget(self.but_1)
        self.add_widget(self.but_2)
        self.add_widget(self.but_3)
        self.add_widget(self.but_4)
        self.add_widget(self.but_5)
        self.add_widget(self.but_6)
        self.add_widget(self.but_7)
        self.add_widget(self.but_8)

        # Удаоение кнопок главного экрана
        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    # Кнопка назад для экстренных вызовов
    def basic_1(self, instance):
        """Рисует главный экран"""
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)

        # Удалание кнопок экстренных вызовов
        self.remove_widget(self.back_button_1)
        self.remove_widget(self.but_1)
        self.remove_widget(self.but_2)
        self.remove_widget(self.but_3)
        self.remove_widget(self.but_4)
        self.remove_widget(self.but_5)
        self.remove_widget(self.but_6)
        self.remove_widget(self.but_7)
        self.remove_widget(self.but_8)

    def inf_tur(self, instance):
        """Рисует экран информация для туристов"""
        # Кнопка выхода назад
        self.back_button_2 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (339, 50))
        self.back_button_2.bind(on_press = self.basic_2)

        # Создание кнопок 
        self.image = Image(source = 'hotel arai plaza.bmp', allow_stretch = True)
        essay = 'Один из знаменитых отелей Тараз является Arai Plaza. '
        essay += '\nВыше приведена картина этой отели.'
        self.btn = Button(text = essay, background_color = [0, 0, 0, 0], size_hint = (None, None), size = (339, 50))

        # Добавление кнопок
        self.add_widget(self.back_button_2)
        self.add_widget(self.image)
        self.add_widget(self.btn)

        # Удаление кнопок главного экрана
        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    def basic_2(self, instance):
        """Рисует главный экран"""
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)
        
        self.remove_widget(self.back_button_2)
        self.remove_widget(self.image)
        self.remove_widget(self.btn)
        
    def inf_web(self, instance):
        """Рисует экран информационные страницы"""
        # Кнопка назад
        self.back_button_3 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (339, 50))
        self.back_button_3.bind(on_press = self.basic_3)

        # Создание кнопок
        self.img = Image(source = 'Jambyl.bmp', allow_stretch = True)
        string = 'Джамбул Джабаев - советский поэт, в честь \n которого и был '
        string += 'переименован город из Тараза \n в Джамбул. Поэт - акын с '
        string += 'детства умел играть на домбре. \n В песнях и стихах он '
        string += 'прословлял и советсткую власть, \n и конкретных вождей '
        string += 'революции.'
        self.butn = Button(text = string, background_color = [0, 0, 0, 0], size_hint = (None, None), size = (339, 70))

        # Добавление кнопок
        self.add_widget(self.back_button_3)
        self.add_widget(self.img)
        self.add_widget(self.butn)

        # Удаление кнопок главного экрана
        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    def basic_3(self, instance):
        """Рисует главный экран"""
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)

        self.remove_widget(self.back_button_3)
        self.remove_widget(self.img)
        self.remove_widget(self.butn)

    def sett(self, instance):
        """Рисует экран настроек"""
        self.back_button_4 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (350, 50))
        self.back_button_4.bind(on_press = self.basic_4)
        
        self.lbl_1 = Label(text = 'Оповещения об угрозах on/off')
        self.sw_1 = Switch(active = True)

        self.add_widget(self.back_button_4)
        self.add_widget(self.lbl_1)
        self.add_widget(self.sw_1)
        
        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    def basic_4(self, instance):
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)

        self.remove_widget(self.back_button_4)
        self.remove_widget(self.lbl_1)
        self.remove_widget(self.sw_1)

    def imp_sms(self, instance):
        self.back_button_5 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (350, 50))
        self.back_button_5.bind(on_press = self.basic_5)
        
        txt = 'Об утверждении Правил оказания социальной помощи, \n'
        txt += 'установления размеров и определения перечня \n'
        txt += 'отдельных категорий нуждающихся граждан по городу \n'
        txt += ' Тараз \n'
        self.sms_button_1 = Button(text = txt, background_color = [0, 0, 0, 0])

        self.add_widget(self.back_button_5)
        self.add_widget(self.sms_button_1)
        
        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    def basic_5(self, instance):
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)

        self.remove_widget(self.back_button_5)
        self.remove_widget(self.sms_button_1)

    def map(self, instance):
        self.back_button_6 = Button(text = '[color=000000]Вернуться назад[/color]', background_color = [255, 0.9, 0, 255], markup = True, size_hint = (None, None), size = (339, 50))
        self.back_button_6.bind(on_press = self.basic_6)
        
        self.mapview = MapView(zoom = 12, lat=42.9, lon=71.3667)
        self.popup_1 = MapMarkerPopup(lat=42.898747, lon=71.384996)
        self.pop_button_1 = Button(text = '[color=ffffff]Мавзолей \n Карахана[/color]', background_color = [1, 1, 1, 1], markup = True)
        self.popup_2 = MapMarkerPopup(lat=42.877504, lon=71.418151)
        self.pop_button_2 = Button(text = '[color=ffffff]Мавзолей \n Тектурмас[/color]', background_color = [1, 1, 1, 1], markup = True)
        self.popup_3 = MapMarkerPopup(lat=42.897195, lon=71.394753)
        self.pop_button_3 = Button(text = '[color=ffffff]Древний \n Тараз[/color]', background_color = [1, 1, 1, 1], markup = True)
        self.popup_4 = MapMarkerPopup(lat=42.901422, lon=71.379433)
        self.pop_button_4 = Button(text = '[color=ffffff] Жамбылский \n театр драмы \n имени Абая[/color]', background_color = [1, 1, 1, 1], markup = True)
        

        self.add_widget(self.back_button_6)
        self.add_widget(self.mapview)
        self.mapview.add_widget(self.popup_1)
        self.popup_1.add_widget(self.pop_button_1)
        self.mapview.add_widget(self.popup_2)
        self.popup_2.add_widget(self.pop_button_2)
        self.mapview.add_widget(self.popup_3)
        self.popup_3.add_widget(self.pop_button_3)
        self.mapview.add_widget(self.popup_4)
        self.popup_4.add_widget(self.pop_button_4)

        self.remove_widget(self.label)
        self.remove_widget(self.button_1)
        self.remove_widget(self.button_2)
        self.remove_widget(self.button_3)
        self.remove_widget(self.button_4)
        self.remove_widget(self.button_5)
        self.remove_widget(self.button_6)

    def basic_6(self, instance):
        self.label = Label(text = '[i][color=19a8ffff]Тараз : +6°C[/color][/i]', markup = True, font_size = '30sp', italic = True)
        self.button_1 = Button(text = '[color=000000]Номера экстренных служб[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_1.bind(on_press = self.calls)
        self.button_2 = Button(text = '[color=000000]Информация для туристов[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_2.bind(on_press = self.inf_tur)
        self.button_3 = Button(text = '[color=000000]Информационные страницы с контентом[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_3.bind(on_press = self.inf_web)
        self.button_4 = Button(text = '[color=000000]Настройка уведомлений[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_4.bind(on_press = self.sett)
        self.button_5 = Button(text = '[color=000000]Специальные правительственные сообщения[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_5.bind(on_press = self.imp_sms)
        self.button_6 = Button(text = '[color=000000]Карта с отображением значимых мест[/color]', background_color = [255, 0.9, 0, 255], markup = True)
        self.button_6.bind(on_press = self.map)

        self.add_widget(self.label)
        self.add_widget(self.button_6)
        self.add_widget(self.button_1)
        self.add_widget(self.button_5)
        self.add_widget(self.button_2)
        self.add_widget(self.button_3)
        self.add_widget(self.button_4)

        self.remove_widget(self.back_button_6)
        self.remove_widget(self.mapview)

        
class MyApp(App):
    def build(self):
         return Basic()

if __name__ == '__main__':
    MyApp().run()
