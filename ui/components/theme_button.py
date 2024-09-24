import flet as ft

def build_theme_button(page, log_viewer):
    theme_icon = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_6,
        on_click=lambda e: toggle_theme(page, log_viewer)
    )
    return theme_icon

def toggle_theme(page, log_viewer):
    if page.theme_mode == ft.ThemeMode.DARK:
        page.theme_mode = ft.ThemeMode.LIGHT
        page.controls[0].controls[0].icon = ft.icons.BRIGHTNESS_6  # Ícone para tema escuro
        log_viewer.text_style.color = ft.colors.BLACK  # Altera a cor do log para preto
    else:
        page.theme_mode = ft.ThemeMode.DARK
        page.controls[0].controls[0].icon = ft.icons.BRIGHTNESS_4  # Ícone para tema claro
        log_viewer.text_style.color = ft.colors.WHITE  # Altera a cor do log para branco

    page.update()  # Atualiza a UI
