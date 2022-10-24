import click

@click.command()
@click.argument("myarg", type=int)
def deploy_proxy(myarg):
    print(f"result {myarg}")
