from pywinauto import Application
import time


if __name__ == '__main__':

    app = Application(backend="uia").start(
        "C:\Program Files (x86)\Asseco Poland SA\Platnik\P2Start.exe")  # Kod szukjacy execa
    window = app.window(title="Aktualizacja Programu Płatnik").wait("visible", timeout=20, retry_interval=1)

    time.sleep(10)
    error_dlg = Window.children()[0]
    error_dlg.children()[0].click()
    time.sleep(5)

    app2 = Application(backend="uia").connect(title="Logowanie do programu", class_name="05381030-963D-4779-BECA-0D7D49268EDB-Login")
    app2.windows()[0].children()[0].set_text("Abcd1234%")
    app2.windows()[0].children()[4].click()
    app2 = Application(backend="uia").connect(title="Płatnik - Moon")
    # print(app2.windows())
    # print(app2.windows()[0].children())
    app2.windows()[0].children()[4].click()
    # print(app2.windows())
    # print(app2.windows()[0].children())
    # print(app2.windows()[0].children()[0].children())
    # print(app2.windows()[0].children()[0].children()[0].expand())

