Termux offre un terminale ed un sistema di pacchetti Linux su Android.

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
pkg install termux-x11-nightly xfce firefox python-pip python-pygame python-tkinter
pip install thonny
```

## Termux:X11

- Termux è essenzialmente un terminale testuale
- Per eseguire applicazioni grafiche, occorre supporto per `X11`
- Scaricare ed installare il seguente Apk per Termux:X11:
    - <https://univpr-my.sharepoint.com/:u:/g/personal/michele_tomaiuolo_unipr_it/EXHaMl4bs-RLv_N_fIlD-MgBrLkRjH3ZSGoFXxEG7nC26A?e=vsRJvO>
- Eseguire da Termux il seguente comando, prima di avviare l'app *Termux:X11*

```
termux-x11 :0 -xstartup "dbus-launch --exit-with-session xfce4-session"
```