Termux offre un terminale e un sistema di pacchetti Linux su Android.

<https://lwn.net/Articles/936953/>

## Installazione

- Installare l'Apk di *F-Droid*
    - <https://f-droid.org/en/>
- *F-Droid* è uno store di applicazioni open-source
- Avviare F-Droid, cliccare sulla *lente* e cercare “Termux”
- Installare Termux
    - <https://f-droid.org/packages/com.termux/>

## Configurazione

- Eseguire i seguenti comandi in Termux

```
pkg update
pkg install x11-repo tur-repo
pkg install termux-x11-nightly xfce firefox python-pip python-pygame python-tkinter openssl wget
pip install thonny
wget ~/.local/share/applications/Thonny.desktop https://fondinfo.github.io/termux/Thonny.desktop
```

## Termux:X11

- Termux è essenzialmente un terminale testuale
- Per eseguire applicazioni grafiche, occorre supporto per `X11`
- Scaricare e installare il seguente Apk per Termux:X11:
    - <https://github.com/termux/termux-x11/releases/download/nightly/app-universal-debug.apk>
- Eseguire da Termux il seguente comando, prima di avviare l'app *Termux:X11*

```
termux-x11 :0 -xstartup "dbus-launch --exit-with-session xfce4-session"
```
