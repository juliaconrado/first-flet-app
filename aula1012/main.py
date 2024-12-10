import flet as ft

def main(page: ft.Page):
    # Callback para atualizar o Slider automaticamente
    def update_slider(e):
        slider.width = int(width_input.value) if width_input.value.isdigit() else 300
        slider.active_color = active_color_input.value or "blue"
        slider.inactive_color = inactive_color_input.value or "grey"
        slider.thumb_color = thumb_color_input.value or "red"
        page.update()

    # Callback para exibir o valor do Slider
    def slider_changed(e):
        label.value = f"Valor selecionado: {slider.value}"
        page.update()

    # Slider inicial
    slider = ft.Slider(
        min=0,
        max=100,
        divisions=10,
        label="{value}%",
        value=50,
        active_color="blue",
        inactive_color="grey",
        thumb_color="red",
        on_change=slider_changed,
        width=300
    )

    # Inputs para personalização (com atualização automática)
    width_input = ft.TextField(
        label="Largura do Slider (em pixels)", 
        value="300", 
        on_change=update_slider
    )
    active_color_input = ft.TextField(
        label="Cor ativa", 
        value="blue", 
        on_change=update_slider
    )
    inactive_color_input = ft.TextField(
        label="Cor inativa", 
        value="grey", 
        on_change=update_slider
    )
    thumb_color_input = ft.TextField(
        label="Cor do ponto de seleção", 
        value="red", 
        on_change=update_slider
    )

    # Label para mostrar o valor do Slider
    label = ft.Text(value="Valor selecionado: 50", size=20)

    # Adicionando elementos na página
    page.add(
        ft.Text("Slider Personalizável", size=30, weight="bold"),
        slider,
        ft.Text("Configurações do Slider:", size=20),
        width_input,
        active_color_input,
        inactive_color_input,
        thumb_color_input,
        label
    )

# Executa a aplicação Flet
ft.app(target=main)
