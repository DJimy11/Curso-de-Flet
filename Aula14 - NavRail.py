from flet import *

def main(page: Page):
    page.title = 'Menu Lateral'

    rail = NavigationRail(
        #extended=True,
        selected_index=0,
        min_width=100,
        min_extended_width=200,
        label_type=NavigationRailLabelType.ALL,
        leading=FloatingActionButton(icon=icons.CREATE, text='CRIAR'),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER,
                selected_icon=icons.FAVORITE,
                label='FAVORITO'
            ),

            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label='MARCAR'
            ),

            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon=icons.SETTINGS,
                label='DEFINIÇÕES'
            )
        ],
        on_change = lambda e: print(f'Página Selecionada: {e.control.selected_index}')
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column([Text('CORPO DA APLICAÇÃO')],
                       alignment==MainAxisAlignment.START,
                       expand=True
                    ),
            ],
            expand=True
        )
    )




app(target=main)