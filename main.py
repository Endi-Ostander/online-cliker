from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests

class ClickerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Поле для ввода IP сервера
        self.server_ip = TextInput(
            text="http://192.168.0.111:5000",
            hint_text="Введите URL сервера",
            size_hint=(1, 0.2)
        )
        
        self.score_label = Label(text="Общий счёт: ...", font_size=32)
        self.button = Button(text="Клик!", font_size=48, size_hint=(1, 0.5))
        self.button.bind(on_press=self.send_click)
        
        self.layout.add_widget(self.server_ip)
        self.layout.add_widget(self.score_label)
        self.layout.add_widget(self.button)
        
        self.update_score()
        return self.layout

    def get_server_url(self):
        return self.server_ip.text.strip()

    def update_score(self):
        try:
            r = requests.get(self.get_server_url() + "/score")
            if r.ok:
                self.score_label.text = f"Общий счёт: {r.json().get('score', 0)}"
            else:
                self.score_label.text = "Ошибка получения счёта"
        except Exception as e:
            self.score_label.text = f"Ошибка: {str(e)}"

    def send_click(self, instance):
        try:
            r = requests.post(self.get_server_url() + "/click")
            if r.ok:
                self.update_score()
        except:
            self.score_label.text = "Ошибка клика"

if __name__ == "__main__":
    ClickerApp().run()
