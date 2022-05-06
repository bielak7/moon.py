from pywinauto import Application
import time
import os



def login():
    password = input("Podaj hasło: ")

    app = Application(backend="uia").start("C:\Program Files (x86)\Asseco Poland SA\Platnik\P2Start.exe")  # Kod szukjacy execa
    Window = app.window(title="Aktualizacja Programu Płatnik").wait("visible", timeout=10, retry_interval=1)  # timeout was 20
    ## TODO Wymyśleć jak czekać na okienka bez sleepa - usunąć wszystkie sleep. - może wait untill
    time.sleep(10)  # was 10
    error_dlg = Window.children()[0] ## TODO zamnieć wyszukiwanie po indexie [0] na wyszukiwannie po nazwie/innych atrybutach
    error_dlg.children()[0].click()
    time.sleep(5)

    app2 = Application(backend="uia").connect(title="Logowanie do programu",
                                              class_name="05381030-963D-4779-BECA-0D7D49268EDB-Login")
    app2.windows()[0].children()[0].set_text(password) ## TODO dodac opcje wpisywania nazwy uzytkownika
    app2.windows()[0].children()[4].click()

    ac_window = app2.window(title="Aktualizacja programu i danych płatnika").wait("visible", timeout=5,
                                                                                  retry_interval=1)
    ac_window.children()[4].click()

def import_file():
    ## TODO klikanie menu przycisku importuj
    app = Application(backend="uia").connect(title="Płatnik - Moon")
    import_window_step_p1 = app.window(title="Kreator importu dokumentów - krok 1 / 6")
    import_window_step_p1.Dalej.click()
    import_window_step_p2 = app.window(title="Kreator importu dokumentów - krok 2 / 6")
    import_option = import_window_step_p2.child_window(title="Import nowych dokumentów")
    import_option.click_input()
    import_window_step_p2["Dalej >"].click()
    import_window_step_p3 = app.window(title="Kreator importu dokumentów - krok 3 / 6")
    import_window_step_p3["Przeglądaj..."].click()
    dialog = app.Otwieranie  ## do tego momentu jest ok
    ## TODO Pomyslec nad struktura plikow dla programu, gdzie sciagamy pliki i skad aplikacja ma je brac. I jak doprowadzic aplilkacje do tego miejsca
    ## TODO Przejsc sciezke do miejsca gdzie sa pliki/ jesli okienko jest juz w miejscu gdzie sa pliki po prostu je wybrac
    # user = os.getlogin()
    # print(dialog.child_window)
    # side_bar = dialog.children()[3].children()[3]
    # side_bar.click()
    # time.sleep(1)
    # select_window = dialog.children()[4]
    # print(select_window.children())
    # print(select_window.children()[2].children())
    # select_window.children()[2].children()[0].click_input(double=True)
    # time.sleep(1)
    # print(dialog.children())
    dialog.children()[4].get_item('Użytkownicy').click_input(double=True)
    time.sleep(3)
    # print(dialog.children())
    dialog.children()[0].get_item(user).click_input(double=True)
    time.sleep(1)
    dialog.children()[4].get_item('Application Data').click_input(double=True)
    time.sleep(2)
    dialog.children()[0].get_item('MoonWalker').click_input(double=True)
    time.sleep(2)
    #for item in dialog.children()[2].items[1:]:
        #item.select()
        #dialog.send_key("{SPACE}")
    dialog.children()[0].items()[2].click_input(double=True) ## TODO dodac opcje wybierania wielu plikow naraz
    import_window_step_p3["Dalej >"].click() ## Tu jest znów ok
    import_window_step_p4 = app.window(title="Kreator importu dokumentów - krok 4 / 6")
    import_window_step_p4["Dalej >"].click()


if __name__ == '__main__':
    # login()
    import_file()
    # error_dlg = Window.children()[4].click()
    app2 = Application(backend="uia").connect(title="Płatnik - Moon")
    # print(app2.windows())
    # print(app2.windows()[0].children())
    # print(app2.windows()[0].children()[0])
    # print(app2.windows()[0].children()[0].children())
    # pane = app2.windows()[0].children()[0].children()[0]
    # print(pane.children())


    # app4 = Application(backend='uia').connect(class_name='TCorelButton')
    # print(app2.windows())
    # print(app2.windows()[0].children())

    # app2.windows()[0].children()[4].click()
    # print(app2.windows())
    # print(app2.windows()[0].children())
    # print(app2.windows()[0].children()[0].children())
    # print(app2.windows()[0].children()[0].children()[0].expand())

