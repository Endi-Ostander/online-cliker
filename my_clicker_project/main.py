
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

SERVER_URL = "http://192.168.0.111:5000"

class ClickerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.score_label = Label(text="Общий счёт: ...", font_size=32)
        self.button = Button(text="Клик!", font_size=48, size_hint=(1, 0.5))
        self.button.bind(on_press=self.send_click)
        self.layout.add_widget(self.score_label)
        self.layout.add_widget(self.button)
        self.update_score()
        return self.layout

    def update_score(self):
        try:
            r = requests.get(SERVER_URL + "/score")
            if r.ok:
                self.score_label.text = f"Общий счёт: {r.json().get('score', 0)}"
            else:
                self.score_label.text = "Ошибка получения счёта"
        except:
            self.score_label.text = "Сервер недоступен"

    def send_click(self, instance):
        try:
            r = requests.post(SERVER_URL + "/click")
            if r.ok:
                self.update_score()
        except:
            self.score_label.text = "Ошибка клика"

if __name__ == "__main__":
    ClickerApp().run()
