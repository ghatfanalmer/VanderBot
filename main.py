import flet as ft

def main(page: ft.Page):
    page.title = "Vander Bot Launcher"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Komponen UI
    key_input = ft.TextField(label="Masukkan License Key", password=True, width=300)
    status_text = ft.Text("")
    
    def handle_login(e):
        # Contoh validasi key (nanti bisa dihubungkan ke database/Google Sheets)
        if key_input.value == "VANDER2026":
            status_text.value = "Login Berhasil! Bot siap dijalankan."
            status_text.color = "green"
            # Di sini nanti bisa disusul fungsi untuk menyalakan bot Telethon
        else:
            status_text.value = "License Key salah!"
            status_text.color = "red"
        page.update()

    page.add(
        ft.Column([
            ft.Text("Vander Bot Authentication", size=20, weight=ft.FontWeight.BOLD),
            key_input,
            ft.ElevatedButton("Login & Start", on_click=handle_login),
            status_text
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
