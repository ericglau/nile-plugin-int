import click

@click.command()
@click.argument("myarg", type=str)
def deploy_proxy(myarg):
    print(f"result {myarg}")
