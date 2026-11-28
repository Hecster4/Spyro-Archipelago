from worlds.LauncherComponents import Component, Type, components, launch, icon_paths

def run_client(*args: str) -> None:
    # Ideally, you should lazily import your component code so that it doesn't have to be loaded until necessary.
    from .client.CommonClient import launch_client
    
    launch(launch_client, name="Spyro Client", args=args)
    
    
components.append(
    Component(
        "Spyro Client",
        func=run_client,
        game_name="Spyro the Dragon",
        component_type=Type.CLIENT,
        icon="Spyro"
    )
)
icon_paths["Spyro"] = "ap:worlds.spyro_the_dragon/assets/icon.png"
