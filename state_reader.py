import json
import typing

import models
import pydantic


class StateFileReader:
    def __init__(
        self,
        file_path: str,
    ) -> None:
        """
        Initializes the StateFileReader instance.

        Args:
            file_path (str): The path to the state file.
        """
        self.file_path = file_path
        self.data = self.load_file()
    
    def load_file(
        self,
    ) -> models.TerraformState:
        """
        Loads the state file and returns its content as a TerraformState object.

        Returns:
            models.TerraformState: The loaded and validated state data.
        """
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
    
            return models.TerraformState(**data)
        
        except (
            FileNotFoundError, 
            json.JSONDecodeError, 
            pydantic.ValidationError
        ) as e:
            print(
                f'Error loading or validating state file: {e}',
            )
            
            return models.TerraformState(
                version=0,
                terraform_version='',
                resources=[],
            )
    
    def list_resources(
        self,
    ) -> typing.List:
        """
        Lists the names of resources in the loaded state file.

        Returns:
            List[str]: A list of resource names.
        """
        return [
            resource.name 
            for resource in self.data.resources
        ]
        
    def get_managed_resources(
        self,
    ):
        return [
            resource for resource in self.data.resources
            if resource.mode == models.ResourceMode.managed
        ]
    
    def resource_exists(
        self,
        resource_name: str,
    ) -> bool:
        """
        Checks if a resource exists in the state file.

        Args:
            resource_name (str): The name of the resource to check.

        Returns:
            bool: True if the resource exists, False otherwise.
        """
        return any(
            resource.name == resource_name 
            for resource in self.data.resources
        )
    
    def get_resource_added_date(
        self,
        resource_name: str,
    ) -> typing.Optional[str]:
        """
        Retrieves the added date of a specific resource, if available.

        Args:
            resource_name (str): The name of the resource.

        Returns:
            typing.Optional[str]: The date the resource was added, or None if not available.
        """
        for resource in self.data.resources:
            if resource.name == resource_name:
                # TODO: add functionality to get resource added date if possible
                return resource.model_dump()
    
        return None
