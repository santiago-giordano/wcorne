<p align="center">
  <img width="900" alt="Wireless Corne" src="https://github.com/user-attachments/assets/0e4540cb-65be-4db0-9063-eaaef82d1726" />
</p>

<h1 align="center">Wireless HotSwap MX Ergo Split Corne Keyboard</h1>
<p align="center">Compacto, inalámbrico y pensado para aprovechar al máximo cada tecla</p>

Firmware [ZMK](https://zmk.dev) para un Corne inalámbrico con nice!nano v2 y nice!view. Pensado para el layout de teclado **Estados Unidos - Internacional** del sistema operativo (la ñ y los tildes se escriben con RAlt).

El keymap está en [config/corne.keymap](config/corne.keymap).

### Capas

`▽` = transparente (usa la tecla de la capa de abajo). `–` = sin función.

#### Base

```
Tab    Q  W  E  R  T      Y  U  I  O  P  Bksp
LShft  A  S  D  F  G      H  J  K  L  ;  Del
LCtl   Z  X  C  V  B      N  M  ,  .  /  Caps
          LAlt  Lower  Space      Enter  Raise  RAlt
```

#### Lower (mantener Lower)

```
Esc    !  @  #  $  %      –  –  ↑  –  –  \
LShft  ^  &  *  ↑  ~      –  ←  ↓  →  '  =
LCtl   –  PrtSc  ←  ↓  →  (  )  [  ]  -  `
          LWin  ▽  Space          Enter  ▽  RAlt
```

#### Raise (mantener Raise)

```
Esc    –  –   ↑  –   Calc    +  7  8  9  *  Bksp
LShft  –  ←   ↓  →   –       -  4  5  6  /  Del
LCtl   –  PrtSc  –  –  –     ,  1  2  3  .  =
          LWin  ▽  Space          Enter  ▽  0
```

#### Adjust (mantener Lower + Raise)

```
Boot    BT0  BT1  BT2  BT3  BT4      –  –  –  –  –  Boot
Reset   USB  BLE  –    –    –        –  –  –  –  –  Reset
Studio  –    –    –    –    –        –  –  –  –  –  BT CLR
                  ▽    ▽    ▽        ▽  ▽  ▽
```

- **BT0 a BT4**: elige el perfil Bluetooth. Se guardan hasta 5 dispositivos.
- **USB / BLE**: fuerza la salida por cable o por Bluetooth, aunque el teclado esté enchufado. El cable va en la mitad **izquierda**.
- **BT CLR**: borra el emparejamiento del perfil activo. Está lejos de los perfiles para no apretarlo por error.
- **Boot / Reset**: afectan solo a la mitad donde se aprietan, por eso están en las dos. Boot deja esa mitad lista para flashear.
- **Studio**: desbloquea [ZMK Studio](https://zmk.studio), habilitado en la mitad izquierda.

### Perfiles Bluetooth

| Perfil | Dispositivo |
|---|---|
| BT0 | PC personal (Windows) |
| BT1 | PC personal (Omarchy) |
| BT2 | Celular |
| USB | PC del trabajo |

### Flashear

El firmware se compila con GitHub Actions en cada push (pestaña Actions, artifact `firmware`). Para cambios de keymap alcanza con flashear `corne_left`. La mitad derecha solo se reflashea si cambia algo de su propio firmware.
