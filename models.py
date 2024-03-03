import enum
import typing

import pydantic


class SupportedTFVersions(
    enum.Enum,
):
    """
    Enum for supported Terraform versions.
    """
    V0_12 = '0.12'
    V0_13 = '0.13'
    V0_14 = '0.14'
    V1_0 = '1.0'

    @classmethod
    def values(cls) -> typing.List[str]:
        """
        Get a list of all supported Terraform version values.

        Returns:
            typing.List[str]: A list of Terraform version strings.
        """
        return [
            item.value for item in cls
        ]


class ResourceMode(
    str,
    enum.Enum,
):
    """
    Enum for representing the mode of a Terraform resource.
    """
    managed = 'managed'
    data = 'data'


class Resource(
    pydantic.BaseModel,
):
    """
    A Pydantic model representing a Terraform resource.

    Attributes:
        mode (ModeEnum): The mode of the resource showing 'managed' by Terraform or a 'data' source.
        type (str): The type of the resource.
        name (str): The name of the resource.
        provider (str): The provider of the resource.
        instances (Optional[List[dict]]): An optional list of dictionaries, each representing an instance of the resource.
    """
    mode: ResourceMode
    type: str
    name: str
    provider: str
    instances: typing.Optional[list]


class TerraformState(
    pydantic.BaseModel,
):
    """
    A Pydantic model representing the state of a Terraform deployment.

    Attributes:
        version (int): The version of the state file.
        terraform_version (str): The version of Terraform used.
        resources (typing.List[Resource]): A list of resources in the state.
    """
    version: int
    terraform_version: str
    serial: int
    lineage: str
    outputs: dict
    resources: typing.List[
        Resource,
    ]
    
    # @validator('terraform_version')
    # def validate_version(
    #     cls,
    #     version: str,
    # ) -> str:
    #     """
    #     Validates that the provided Terraform version is supported.

    #     Args:
    #         version (str): The Terraform version to validate.

    #     Returns:
    #         str: The validated version.

    #     Raises:
    #         ValueError: If the Terraform version is not supported.
    #     """
    #     if version not in SupportedTFVersions.values():
    #         raise ValueError(
    #             'Unsupported Terraform version',
    #         )
        
    #     return version
