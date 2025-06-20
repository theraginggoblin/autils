from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[__name__])

    config = providers.Configuration(strict=True)

    number = providers.Object(1)

@inject
def main(a_number: int = Provide[Container.number]) -> None:
    print(f"a_number is: {a_number}")

if __name__ == "__main__":
    container = Container()

    container.config.from_dict(
        {
            "aws": {
                 "access_key_id": "KEY",
                 "secret_access_key": "SECRET"
             },
        },
    )

    assert container.config() == {
        "aws": {
            "access_key_id": "KEY",
            "secret_access_key": "SECRET",
        },
    }
    assert container.config.aws() == {
        "access_key_id": "KEY",
        "secret_access_key": "SECRET",
    }
    assert container.config.aws.access_key_id() == "KEY"
    assert container.config.aws.secret_access_key() == "SECRET"
    print(container.config())
    main()
    main(a_number=50)